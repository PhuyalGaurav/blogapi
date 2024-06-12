from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        if UserChangeForm.Meta.fields == '__all__':
            fields = '__all__'
        else:
            fields = list(UserChangeForm.Meta.fields.split(',')) + ["name"]

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields