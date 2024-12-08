from django import forms
from account_module.models import User

class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        # fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'row' : 3,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'row' : 6,
                'id' : 'message'
            })
        }

        labels = {
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی',
            'avatar' : 'تصویر پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره شخص',
        }