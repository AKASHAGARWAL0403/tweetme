from django.shortcuts import render
from .models import Hashtag
from django.views import View
# Create your views here.

class HashtagView(View):
    def get(self , request , hashtag , *args , **kwargs):
        hash_obj , created = Hashtag.objects.get_or_create(tag=hashtag)
        return render(request , "hashtags/tag_view.html" , {"obj" : hash_obj})