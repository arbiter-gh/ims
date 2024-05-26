from django import forms
from .models import *


class uform(forms.ModelForm):
    class Meta:
        model = user
        # fields = "__all__"
        fields = ["f_name", "l_name", "email", "phone", "gender"]


class ad_update_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ["f_name", "l_name", "email", "phone", "gender", "password"]


class ad_update_pform(forms.ModelForm):
    class Meta:
        model = term_insurance
        fields = [
            "insuor",
            "life_cover",
            "cover_till_age",
            "claim_settelment",
            "pay_monthly",
        ]


class ad_update_h_form(forms.ModelForm):
    class Meta:
        model = health_insurance
        fields = [
            "policy_name",
            "cover_amount",
            "policy_period",
            "pay_monthly",
        ]
