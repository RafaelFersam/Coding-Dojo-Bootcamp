from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postdata):
        email_check =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['f_name'])<2:
            errors['f_name']="First Name must be longer than 2 characters!"
        if len(postdata['l_name'])<2:
            errors['l_name']="Last Name must be longer than 2 characters!"
        if not email_check.match(postdata['email']):
            errors['email']="Email must be valid format"
        if len(postdata['pw'])<8:
            errors['pw']="password must be at least 8 characters!"
        if postdata['pw'] != postdata['conf_pw']:
            errors['conf_pw'] ="Password and confirm password must match!"
        return errors

class User(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()