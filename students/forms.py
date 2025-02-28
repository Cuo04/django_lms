from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# create your forms here

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length = 100)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('phone','dob','address','image')
    