from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User
# Register your models here.


class MyuserChangeForm(UserChangeForm):
    class meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_messages = UserCreationForm.error_messages.update(
        {"duplicate_username":"this username has already been taken"}
    )
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(self.error_messages["duplicate_username"])

@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyuserChangeForm
    add_form =MyUserCreationForm
    fieldsets = (("User Profile",{"fielf":("name",)}),) + AuthUserAdmin.fieldsets
    list_display = ('Username','name','is_superuser')
    search_fields = ["name"]