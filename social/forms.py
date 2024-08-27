from django import forms
from .models import Tweet, Profile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Post(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Title",
            "class": "form-control"
        }
    ), label = "")

    image = forms.ImageField(label="Image", required=False)

    body = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
            attrs={
            "placeholder": "Share your thoughts.",
            "class": "form-control",
            "rows": 2,
            }), 
        label="", 
    )

    class Meta:
        model = Tweet
        exclude = ("user", "likes",)
        fields = ['title', 'image', 'body']


class SignUp(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Email Address"
        }
    ))

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"First Name"
        }
    ))

    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Last Name"
        }
    ))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class ProfileInfo(forms.ModelForm):
    profile_picture = forms.ImageField(label="Profile Picture")
    profile_bio = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={
        "class":"form-control",
        "placeholder":"Profile bio"
    }))

    instagram = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Instagram"
    }))

    linkedin = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"LinkedIn"
    }))

    facebook = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Facebook"
    }))

    homepage = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Personal website"
    }))

    class Meta:
        model = Profile
        fields = ('profile_picture', 'profile_bio', 'instagram', 'linkedin', 'facebook', 'homepage', )


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
            attrs={
            "placeholder": "Share your thoughts.",
            "class": "form-control",
            "rows": 1,
            }), 
        label="", 
    )

    class Meta:
        model = Comment
        fields = ['body',]
