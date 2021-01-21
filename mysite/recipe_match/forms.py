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



class ConversionForm(forms.Form):
    all_foods = Food.objects.all().order_by('name')
    all_units = Unit.objects.all().order_by('abbr')
    all_foods_list = [(None, "---")]
    for each in all_foods:
        all_foods_list.append((each, each.name))
    all_units_list = [(None, "---")]
    for each in all_units:
        all_units_list.append((each, each.abbr))

    
    food = forms.ChoiceField(choices=all_foods_list)
    amount = forms.DecimalField(max_digits=10, decimal_places=3)
    units = forms.ChoiceField(choices=all_units_list)
    convert_to = forms.ChoiceField(choices=all_units_list)

    class Meta:
        fields = ('food', 'amount', 'units', 'convert_to')

    def __init__(self, *args, **kwargs):
        super(ConversionForm, self).__init__(*args, **kwargs)
        self.fields['food'].required = False
        self.fields['amount'].required = False
        self.fields['units'].required = False
        self.fields['convert_to'].required = False

