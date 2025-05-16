from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Patient, Doctor

User = get_user_model()

class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    profile_picture = forms.ImageField(required=False)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    address_line1 = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=50, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 
                  'user_type', 'address_line1', 'city', 'state', 'pincode',
                  'password1', 'password2')
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        
        return cleaned_data
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        user.address_line1 = self.cleaned_data['address_line1']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.pincode = self.cleaned_data['pincode']
        
        if self.cleaned_data.get('profile_picture'):
            user.profile_picture = self.cleaned_data['profile_picture']
        
        if commit:
            user.save()
            
            # Create corresponding user type profile
            if user.user_type == 'patient':
                Patient.objects.create(user=user)
            elif user.user_type == 'doctor':
                Doctor.objects.create(user=user)
                
        return user 