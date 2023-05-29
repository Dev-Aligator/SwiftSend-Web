from django.forms import ModelForm
from .models import Room
class ImageRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('photo',)