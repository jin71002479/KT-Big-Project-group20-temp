from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_content = models.TextField()
    contact_pub_date = models.DateTimeField()

class Reply(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    reply_content = models.TextField()
    reply_create_date = models.DateTimeField()