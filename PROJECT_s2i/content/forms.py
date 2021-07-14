from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'on_chain',)

    
    # Controllo testo inserito dagli utenti 
    def clean(self):
        content = self.cleaned_data.get('content')
        title = self.cleaned_data.get('title')
        ban = ['hack', 'HACK', 'HaCk', 'hAcK', 'haCK', 'HAck', 'hACk', 'HacK', 'Hack', 'hAck', 'haCk', 'hacK']
        for word in ban:
            if word in content or word in title:
                raise forms.ValidationError("You typed in some banned words!")
        return self.cleaned_data
