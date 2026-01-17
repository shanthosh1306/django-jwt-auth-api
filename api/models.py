from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ProfileUser(AbstractUser): 
    pass    #If we you want to create custom field for user you can create here