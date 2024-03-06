from django import forms
class AddproductusingForm(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.IntegerField()


