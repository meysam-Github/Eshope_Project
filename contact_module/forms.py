from django import forms

from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'row' : 5,
                'id' : 'message',
            })
        }

        labels = {
            'full_name' : 'نام و نام خانوادگی شما',
            'email' : 'ایمیل شما',
            'title' : 'عنوان یا طرح موضوع'
        }

        error_messages = {
            'full_name' : {
                'required' : 'نام و نام  خانوادگی اجبای میباشد'
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField()
