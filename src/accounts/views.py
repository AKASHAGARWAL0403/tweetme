from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

User = get_user_model()

class UserProfileView(DetailView):
    queryset = User.objects.all()
    template_name = "account/user_detail.html"

    def get_object(self,*args,**kwargs):
        return get_object_or_404(User , username = self.kwargs.get("username"))