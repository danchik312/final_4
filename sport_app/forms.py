from django import forms
from . import models


class Sport_list_Form(forms.ModelForm):
    class Meta:
        model = models.ReviewsProduct
        fields = "__all__"
