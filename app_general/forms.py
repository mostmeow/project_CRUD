from django import forms

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

import datetime

from . models import *


class UserForm(forms.Form):
    name = forms.CharField(required=True, label='ชื่อ', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ชื่อ'}))
    # name = forms.CharField(required=True, label='ชื่อ', widget=forms.TextInput(attrs={'class': 'myfieldclass', 'placeholder':'ชื่อ'}))

class FriendForm(forms.ModelForm):
    like = forms.ModelMultipleChoiceField(queryset=LikeModel.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = FriendModel
        fields = {'like'}