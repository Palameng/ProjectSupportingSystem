# -*- coding: utf-8 -*-
from django import forms
from .models import Missions


class AddProjectForm(forms.Form):
    projectName = forms.CharField(required=True)
    projectType = forms.CharField(required=True)
    projectDetail = forms.CharField(required=True)


class MissionForm(forms.ModelForm):
    model = Missions
    pass
