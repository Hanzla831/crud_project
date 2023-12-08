from .models import Student
from django import forms


class StudentResgistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','id':'text'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }