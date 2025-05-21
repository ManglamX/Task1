from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    is_draft = forms.BooleanField(
        required=False,
        initial=False,
        label='Save as draft',
        help_text='Check this if you want to save the post as a draft. Draft posts are only visible to you.'
    )
    
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 10}),
        } 