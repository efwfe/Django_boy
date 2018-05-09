# _*_coding:utf-8_*_
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class AcountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION",True)

    def is_open_for_signup(self,request, sociallogin):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)