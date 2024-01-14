from django import forms

class Write(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100)
    