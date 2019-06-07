from django.forms.utils import ErrorList
from django import forms

class UserLoginCheckMixin(object):
    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            print(form.instance.user)
            return super(UserLoginCheckMixin , self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
            return self.form_invalid(form)

class TweetUpdateCheckMixin(UserLoginCheckMixin , object):
    def form_valid(self,form):
        if form.instance.user == self.request.user:
            return super(TweetUpdateCheckMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You cannot update this tweet"])
            return self.form_invalid(form)
            