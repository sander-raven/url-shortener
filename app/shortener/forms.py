from django import forms

from shortener.models import ShortURL


class ShortURLForm(forms.ModelForm):
    short_code = forms.CharField(required=False)

    class Meta:
        model = ShortURL
        fields = ('original_url', 'short_code')
