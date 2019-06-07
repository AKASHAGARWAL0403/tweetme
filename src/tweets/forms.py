from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['user' , 'content']

    #  def clean_content(self):
    #      content = self.cleaned_data.get('content')
    #      if content == "abc":
    #          raise forms.ValidationError("It cannot be abc")
    #      return content