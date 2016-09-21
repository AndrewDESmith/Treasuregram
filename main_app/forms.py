from django import forms
from .models import Treasure

# Import the Treasure model and inherit from ModelForm (instead of Form), so that we can link the form to the model:
class TreasureForm(forms.ModelForm):
    # The Meta class allows us to define properties that help us to link the form and model together:
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'location', 'material', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(label = 'User Name', max_length = 64)
    password = forms.CharField(widget = forms.PasswordInput())
