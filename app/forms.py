from django import forms

class SongForm(forms.Form):
    Title = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Give Your Song a Title...'}))
    Artist = forms.ChoiceField(choices=[
        
        ('Kanye West', 'Kanye West'),
        ('Bruno Mars', 'Bruno Mars'),
        ('The Beatles', 'The Beatles'),
        ('Alicia Keys', 'Alicia Keys'),
        ('Bob Marley', 'Bob Marley'),
        ('Lil Wayne', 'Lil Wayne'),
        ('Adele', 'Adele'),
        ('Justin Bieber', 'Justin Bieber'),
        ('Britney Spears', 'Britney Spears'),
        ('DJ Khaled', 'DJ Khaled')
        
        ])