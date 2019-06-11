from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404 , redirect
from django.views import View
from .models import UserModel

User = get_user_model()

class UserProfileView(DetailView):
    queryset = User.objects.all()
    template_name = "account/user_detail.html"

    def get_object(self,*args,**kwargs):
        return get_object_or_404(User , username = self.kwargs.get("username"))

    def get_context_data(self,*args,**kwargs):
        context = super(UserProfileView , self).get_context_data(*args , **kwargs)
        toggle_user = get_object_or_404(User , username__iexact=self.kwargs.get("username"))
        is_following = UserModel.objects.is_following(self.request.user , toggle_user)
        context['is_following'] = is_following
        #context['recommended'] = UserModel.objects.recommended(self.request.user , 10)
        return context  

class UserFollowView(View):
    def get(self , request , username , *args , **kwargs):
        toggle_user = get_object_or_404(User , username__iexact=username)
        if request.user.is_authenticated:
            is_following =  UserModel.objects.to_toggle_user(request.user , toggle_user)
        return redirect("profile:user_profile" , username=username)