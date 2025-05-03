from django import forms
from django.forms import MultiWidget, TextInput

class BoardMembers(forms.Form):
    CHOICES = [('President', 'President'), ('President-Elect', 'President-Elect'), ('Spiritual Leader', 'Spiritual Leader'), ('Asst. Spiritual Leader', 'Asst. Spiritual Leader'),
               ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Registrar', 'Registrar'), ('Team Selection', 'Team Selection'), ('Agape', 'Agape'), ('Kitchen', 'Kitchen'),
               ('Columbus Cluster Leader', 'Columbus Cluster Leader'), ('Manchester Cluster Leader', 'Manchester Cluster Leader'), ('Angels/Candlelight', 'Angels/Candlelight'), 
               ('Purchaser/Book Table', 'Purchaser/Book Table'), ('Worship', 'Worship'), ('Music', 'Music'), ('Communication', 'Communication'), ('Face to Face', 'Face to Face')]
    member_position = forms.ChoiceField(label="Member Position", choices=CHOICES)
    member_name = forms.CharField(label="Member Name", max_length=200)

class Clusters(forms.Form):
    CHOICES = [('Columbus', 'Columbus'), ('Manchester', 'Manchester'), ('Phenix City', 'Phenix City')]
    cluster = forms.ChoiceField(label="Cluster", choices=CHOICES, required=True)
    location = forms.CharField(label="Location", max_length=200, required=True)
    start_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    start_time = forms.TimeField(widget=forms.TimeInput, required=True)
    end_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    end_time = forms.TimeField(widget=forms.TimeInput, required=True)
    