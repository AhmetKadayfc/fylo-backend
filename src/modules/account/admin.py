from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .models import User


#Override UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')


admin.site.register(User)
