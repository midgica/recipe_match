from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Food, Unit

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')



##class ConversionForm(forms.Form):
##    all_foods = []
##    all_units = []
##    for each in Food.objects.all().order_by('name'):
##        all_foods.append(each)
##    for each in Unit.objects.all().order_by('abbr'):
##        all_units.append(each)
##    food = forms.MultipleChoiceField(choices=all_foods)
##    amount = forms.DecimalField(max_digits=10, decimal_places=3)
##    units_in = forms.MultipleChoiceField(choices=all_units)
##    units_out = forms.MultipleChoiceField(choices=all_units)
##
##    class Meta:
##        fields = ('food', 'amount', 'units_in', 'units_out')
