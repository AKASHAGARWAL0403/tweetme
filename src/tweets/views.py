from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Tweet
from .forms import TweetForm
from .mixins import UserLoginCheckMixin , TweetUpdateCheckMixin
from django.db.models import Q
from django.urls import reverse

# Create your views here.

class TweetCreateView(UserLoginCheckMixin , CreateView):
    form_class = TweetForm
    template_name = "tweet/create_view.html"
    #login_url = "/admin/"

class TweetUpdateView(LoginRequiredMixin , TweetUpdateCheckMixin , UpdateView):
    form_class = TweetForm
    template_name = "tweet/update_view.html"
    queryset = Tweet.objects.all()
    login_url = "/admin/"

class TweetDeleteView(LoginRequiredMixin  , DeleteView):
    queryset = Tweet.objects.all()
    success_url = "/tweet/"
    login_url = "/admin/"
    template_name = "tweet/delete_view.html"

    # def get_object(self,*args,**kwargs):
    #     obj = super(TweetDeleteView , self).get_object(*args,**kwargs)
    #     if obj.user == self.request.user:
    #         return obj
        

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweet/detail_view.html"

    def get_object(self,*args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        print(obj)
        return obj

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name  = "tweet/list_view.html"
    context_object_name = "object_list"

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['create_form'] = TweetForm()
        context['create_url'] = reverse("tweets:create_view")
        return context