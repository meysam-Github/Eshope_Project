from django import forms
from account_module.models import User

class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address']
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
                'id' : 'message',
            })
        }

        labels = {
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی',
            'avatar' : 'تصویر پروفایل',
            'address': 'آدرس'
        }

        error_messages = {
            'full_name' : {
                'required' : 'نام و نام  خانوادگی اجبای میباشد'
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField()
