from django import forms

class CommentForm(forms.Form):
    auther= forms.CharField(max_length=100,widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}))
    body= forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}) )
    
