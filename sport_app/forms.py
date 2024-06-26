from django import forms
from . import models


class SportListForm(forms.ModelForm):
    class Meta:
        model = models.ReviewsProduct
        fields = "__all__"
