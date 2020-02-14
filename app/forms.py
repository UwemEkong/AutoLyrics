from django import forms
from app.models import Song

class SongForm(forms.ModelForm):
    Artist = forms.ChoiceField(choices= Song.ARTIST_CHOICES)
    class Meta:
        model = Song
        fields = ['title']  
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Give Your Song a Title...'}),
        }