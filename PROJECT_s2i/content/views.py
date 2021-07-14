from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PostForm
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
import redis


# Create your views here.
def homepage(request):
    first_3_posts = Post.objects.filter().order_by('-datetime')[0:3]
    return render(request, 'content/homepage.html', {'posts':first_3_posts})


def info(request):
    return render(request, 'content/info.html', {})

@login_required
def user_id(request, id):
    user_by_id = User.objects.filter(id=id)[0]
    return render(request, 'content/user_id.html', {'user_by_id':user_by_id})


@user_passes_test(lambda u: u.is_superuser)
def posts_mng(request):
    users = User.objects.all()
    posts = Post.objects.all()
    return render(request, 'content/posts_mng.html', {'posts':posts, 'users':users})


@login_required
def posts(request):
    
    # CONTROLLO IP 
    # !----- Necessita SERVER REDIS attivo -----!
    # curr_ip = request.META.get("REMOTE_ADDR")
    # client = redis.StrictRedis(host=#, port=#, db=0) <---- INSERIRE HOST E PORT ----!
    # curr_user = request.user
    # if client.get(f'{curr_user}'):
    #     user_ip = client.get(f'{curr_user}').decode('utf-8')
    #     if curr_ip != user_ip:
    #         print(f"ATTENZIONE! L'ip dell'utente {curr_user} è cambiato da '{user_ip}' a '{curr_ip}'")
    # client.set(f'{curr_user}', f'{curr_ip}'.encode('utf-8'))
    
    posts_list_dt = Post.objects.filter().order_by('-datetime')
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.datetime = timezone.now()
            post.save()
            if post.on_chain: 
                post.writeOnChain()
            id=post.id
            return redirect('content:post_detail', id=id)
    else:
        form = PostForm()
    
    return render(request, 'content/posts.html', {'posts':posts_list_dt, 'form': form})


@login_required
def post_detail(request, id):
    posts_by_id = Post.objects.filter(id=id)
    return render(request, 'content/post_detail.html', {'posts': posts_by_id})




@login_required
def APIs(request):
    return render(request, 'content/APIs.html')


def api_posts_1h(request):
    response = []
    range = datetime.datetime.now(timezone.utc) - datetime.timedelta(hours=1)
    posts_list_1h = Post.objects.filter(datetime__gt=range)
    for post in posts_list_1h:
        response.append(
            {
                'datetime': post.datetime,
                'author': f"{post.user.first_name} {post.user.last_name}",
                'title': post.title,
                'content': post.content,                
                'hash' : post.hash,
                'txId' : post.txId
            }
        )
    return JsonResponse(response, safe=False)


def api_posts_str(request, str):
    posts_list = Post.objects.all()
    counter = 0
    for post in posts_list:
        if str in post.content:
            for word in post.content.split(" "):
                if word == str:
                    counter += 1
    return JsonResponse(counter, safe=False)
# ################### API tutti i post #######################
# def api_posts(request):
#     response = []
#     posts_lists = Post.objects.filter().order_by('datetime')
#     for post in posts_list:
#         response.append(
#             {
#                 'datetime': post.datetime,
#                 'author': f"{post.user.first_name} {post.user.last_name}",
#                 'title': post.title,
#                 'content': post.content,                
#                 'hash' : post.hash,
#                 'txId' : post.txId
#             }
#         )
#     return JsonResponse(response, safe=False)
#  ################### API tutti i post #######################
