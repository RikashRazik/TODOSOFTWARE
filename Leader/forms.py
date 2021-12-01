# --------------------------
# The module consists Api's & Functions for managing activities of client
# ------------------------
# Coded by: Safe and strong  IT Team
# © Safe and strong Business Pvt Ltd
# --------------------------

from django import forms

from Leader.models import profile, suser, dailywork


class Register(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'





class Worklog(forms.ModelForm):
    class Meta:
        model=dailywork
        fields='__all__'


class Userregister(forms.ModelForm):
    class Meta:
        model=suser
        fields='__all__'
