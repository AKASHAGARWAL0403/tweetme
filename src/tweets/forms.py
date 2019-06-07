from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    content = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message", 
                            "class": "form-control"}
                    ))
    class Meta:
        model = Tweet
        fields = ['content']

    #  def clean_content(self):
    #      content = self.cleaned_data.get('content')
    #      if content == "abc":
    #          raise forms.ValidationError("It cannot be abc")
    #      return content