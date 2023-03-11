from django import forms
from .models import Car, ServiceRequest, RentalRequest

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
        fields = ['first_name', 'last_name', 'email', 'car_model', 'description', 'photos']

    car_model = forms.ModelChoiceField(queryset=Car.objects.all())
    photos = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ['first_name', 'last_name', 'email', 'car_model', 'num_days']

    car_model = forms.ModelChoiceField(queryset=Car.objects.all())


