from .models import *
from django import forms


class ImagesCreateForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extension = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extension:
            raise forms.ValidationError('Полученный url ссылается на неизвестное расширение')
        return url

