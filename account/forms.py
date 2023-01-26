from .models import *
from django import forms

class PostForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        max_length = 80,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "form-group relative mb-30 form-control input-white",
        "placeholder": "Enter name",
    }))
    
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
        "class": " form-group relative mb-30 form-control input-white",
         "placeholder": "Enter email",
         
    }))
    
    class Meta:
        model = NewslettersModel
        fields = ['name', 'email',]
        
        
        
        
class BecomeAnAgentForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        max_length = 80,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "form-group relative mb-30 form-control input-white",
        "placeholder": "Enter name",
    }))
    
    phoneNumber = forms.CharField(
        label='',
        max_length = 20,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "form-group relative mb-30 form-control input-white",
        "placeholder": "Enter phone number",
    }))
     
    state = forms.CharField(
        label='',
        max_length = 2000,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "form-group relative mb-30 form-control input-white",
        "placeholder": "Enter state",
    }))
    
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
        "class": " form-group relative mb-30 form-control input-white",
         "placeholder": "Enter email",
         
    }))
    
    class Meta:
        model = BecomeAnAgent
        fields = ['name','phoneNumber','state','email',]
        



class ConactForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        max_length = 80,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "col-md-4 form-group relative mb-30 mb-sm-20 form-control input-lg input-white shadow-5",
        "placeholder": "Enter name",
    }))
    
    phoneNumber = forms.CharField(
        label='',
        max_length = 20,
        required = True,
        widget=forms.TextInput(attrs={
        "class": "col-md-4 form-group relative mb-30 mb-sm-20 form-control input-lg input-white shadow-5",
        "placeholder": "Enter phone number",
    }))
    
    email = forms.EmailField(
        label='',
        required = True,
        widget=forms.TextInput(attrs={
        "class": "col-sm form-group relative  mb-sm-20 form-control input-lg input-white shadow-5",
        "placeholder": "Enter email",
         
    }))
    
    message = forms.CharField(
        label='',
        max_length = 80000,
        required = True,
        widget=forms.Textarea(attrs={
        "class": "col-md-12 form-group relative mb-30 mb-sm-20 form-control input-white shadow-5",
        "placeholder": "Enter message",
    }))
    
    
    class Meta:
        model = ContaclFormModel
        fields = ['name', 'email','phoneNumber','message',]