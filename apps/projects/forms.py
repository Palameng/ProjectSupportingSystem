# -*- coding: utf-8 -*-
from django import forms
from .models import Projects


class AddProjectForm(forms.Form):
    projectName = forms.CharField(required=True)
    projectType = forms.CharField(required=True)
    # projectStuffs = forms.CharField(required=True)
    projectDetail = forms.CharField(required=True)



