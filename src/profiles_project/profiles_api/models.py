from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model. """

    def create_user(self, email, first_name, last_name, password=None):
        """ Creates a new user profile object. """

        if not email:
            raise ValueError('Users must provide an email address.')

        email = self.normalize_email(email)
        
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password) 
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """ Creates and saves a new superuser with given details. """

        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represnts a "user profile" in our system. """

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """ Used to get a users full name. """

        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """ Used to get a users short name. """

        return self.first_name

    def ___str___(self):
        """ Django uses this when it needs to conver the object to a string. """

        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update. """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def ___str___(self):
        """ Return the model as a string. """

        return self.status_text
