from django import forms
from .models import Profile

class NewProjectForm(forms.Form):
    title = forms.CharField(label='Title',max_length=60)
    image = forms.ImageField()
    url = forms.URLField(label='URL', required=True)
    description = forms.CharField(widget=forms.Textarea)

class VoteForm(forms.Form):
    CHOICES = (('1',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('10',10))
    design = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    usability = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    content = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','projects']
