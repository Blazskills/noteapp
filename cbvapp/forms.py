from django.contrib import messages
from django.forms import ModelForm, fields
from django.forms.widgets import NumberInput
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect
from .models import Note, User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio','social_handle','email', 'password1','is_superuser','is_staff']
  
  
class NoteCreationForm(forms.ModelForm):
    class Meta:
        model =Note
        fields=['Note_Priority', 'Note_Color', 'Note_Title', 'Description', 'Reminder_Date']
        widgets = {
            'Note_Title': forms.TextInput(attrs={'class': 'input','class':"form-control", 'id':"exampleInputEmail1", 'placeholder':"Enter Note Title", 'type': 'text'}),
            'Description': forms.Textarea(attrs={'class': 'textarea','class':"form-control", 'row':10, 'id':"exampleInputEmail1", 'placeholder':"Enter Note Details", 'type': 'text'}),
            'Note_Color': forms.Select(attrs={'class':"custom-select" , 'required' : True} ),
            'Note_Priority': forms.Select(attrs={'class':"custom-select" , 'required' : True} ),
            'Reminder_Date': forms.TextInput(attrs={'class': 'input','class':"form-control", 'id':"exampleInputEmail1", 'type': 'date'}),



            }
  
  
class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model =Note
        fields=['Note_Priority', 'Note_Color', 'Note_Title', 'Description', 'Reminder_Date']
        widgets = {
            'Note_Title': forms.TextInput(attrs={'class': 'input','class':"form-control", 'id':"exampleInputEmail1", 'placeholder':"Enter Note Title", 'type': 'text'}),
            'Description': forms.Textarea(attrs={'class': 'textarea','class':"form-control", 'row':10, 'id':"exampleInputEmail1", 'placeholder':"Enter Note Details", 'type': 'text'}),
            'Note_Color': forms.Select(attrs={'class':"custom-select" , 'required' : True} ),
            'Note_Priority': forms.Select(attrs={'class':"custom-select" , 'required' : True} ),
            'Reminder_Date': forms.TextInput(attrs={'class': 'input','class':"form-control", 'id':"exampleInputEmail1", 'type': 'date'}),
        }

    # def clean(self):
    #     super(SignUpForm, self).clean()
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     email = self.cleaned_data.get('email')       
    #     try:
    #         usercheck=User.objects.get(email=email)
    #         if usercheck:
    #              messages.success(request, "Email already exist")
    #              return redirect("blog:register")
    #             #  print('already exist')
    #     except:  
    #         if len(password1) < 8:
    #             print('password too short')
    #             messages.error(request, "password too short")
    #             return redirect("blog:register")
    #         if password1 != password2:
    #             print('password does not match')
    #             raise forms.ValidationError("Your passwords do not match")
    #             # self._errors['password1'] = self.error_class(['password does not match'])
    #         return self.cleaned_data
        
        
        
    #     def clean_password2(self):
    # password1 = self.cleaned_data.get('password1')
    # password2 = self.cleaned_data.get('password2')

    # if not password2:
    #     raise forms.ValidationError("You must confirm your password")
    # if password1 != password2:
    #     raise forms.ValidationError("Your passwords do not match")
    # return password2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# from formValidationApp.models import *





# class SignUpForm2(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'bio','social_handle','email', 'password1','is_superuser','is_staff' ]
#     def clean(self):
#         super(PostForm, self).clean()
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if len(password1) < 5:
#             print('password too short')
#             self._errors['password1'] = self.error_class(['Minimum 5 characters required'])
#         if password1 != password2:
#             print('password does not match')
#             self._errors['password1'] = self.error_class(['password does not match'])




# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'bio','social_handle','email', 'password1','is_superuser','is_staff' ]

