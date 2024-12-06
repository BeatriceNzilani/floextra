from django import forms
from FloexrtaDecorapp.models import Bookings,ImageModel


class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

