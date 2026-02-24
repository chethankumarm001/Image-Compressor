from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    components = forms.IntegerField(min_value=1, max_value=200, initial=50)