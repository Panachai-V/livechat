from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Group(models.Model):
    groupname = models.CharField(max_length=30)
    groupID = models.IntegerField
    username = models.ManyToManyField(User) #ForiengKey IS_IN relation

    def __str__(self):
        return self.groupID

class MessageLog(models.Model):
    msgtext = models.CharField(max_length=1000)
    msgID = models.IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)

    chatID = models.ManyToManyField(User) #ForiengKey PRIVATE_CHAT
    groupID = models.ManyToManyField(Group) #ForiengKey GROUP_CHAT

    def __str__(self):
        return self.msgID