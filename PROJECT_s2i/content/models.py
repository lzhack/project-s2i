from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=250)
    on_chain = models.BooleanField(default=True)
    hash = models.CharField(max_length=32, default=None, blank=True, null=True)
    txId = models.CharField(max_length=66, default=None, blank=True, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

    def __str__(self):
        return self.title