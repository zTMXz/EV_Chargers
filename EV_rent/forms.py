from django import forms
from .models import Car, ServiceRequest, RentalRequest
from users.models import User

# class ServiceRequestForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     #car_model = forms.ModelChoiceField(queryset=Car.objects.all())
#     car_model = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea)
#     photos = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['car_model', 'description', 'photos']


    person = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    car_model = forms.ModelChoiceField(queryset=Car.objects.filter(is_broken=False))
    photos = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ['num_days']

    person = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    # car_model = forms.ModelChoiceField(queryset=Car.objects.filter(is_rented=False))


