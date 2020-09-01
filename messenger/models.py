from django.db import models

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='recipient')
    timesent = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1500)
    room_name = models.CharField(max_length=250, blank=True, null=True)


    class Meta:
        ordering = ('timesent', 'room_name')

    def __str__(self):
        return self.content
