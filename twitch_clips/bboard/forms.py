from django import forms


class PostForm(forms.Form):
    url = forms.URLField(label="URL", widget=forms.URLInput())

