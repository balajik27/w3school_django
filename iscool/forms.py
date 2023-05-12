from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
class custom(UserCreationForm):
    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2')
