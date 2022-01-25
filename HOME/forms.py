
from django import forms
from django.forms import ModelForm


from HOME.models import Post



class Post_Form(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(  attrs={'class': 'form-control'}),
            'title': forms.TextInput(  attrs={'class': 'form-control'}),
            'body': forms.Textarea(  attrs={'class': 'form-control'})
 

        }



class Edit_Post_Form(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(  attrs={'class': 'form-control'}),
            'title': forms.TextInput(  attrs={'class': 'form-control'}),
            'body': forms.Textarea(  attrs={'class': 'form-control'})
        }


