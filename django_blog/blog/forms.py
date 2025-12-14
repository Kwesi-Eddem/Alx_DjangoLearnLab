from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from taggit.forms import TagWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        help_text="Comma-separated tags"
    )
    class Meta:
        model = Post
        fields = ('title','content')
        widgets = {
            'tags': TagWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        if self.instance.pk:
            current = ', '.join(self.instance.tags.values_list('name', flat=True))
            self.fields['tags_input'].initial = current

    def save(self, commit=True):
        post = super().save(commit=commit)
        tags_raw = self.cleaned_data.get('tags_input', '')
        names = [t.strip() for t in tags_raw.split(',') if t.strip()]
        # Create or get Tag objects and set M2M
        tag_objs = []
        for name in names:
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag_obj)
        # If commit=False, ensure post has a PK before setting M2M
        if commit:
            post.tags.set(tag_objs)
        else:
            # Defer setting; caller must set after saving post
            self._deferred_tags = tag_objs
        return post




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }