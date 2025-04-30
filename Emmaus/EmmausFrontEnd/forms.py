from django import forms


class BoardMembers(forms.Form):
    CHOICES = [('President', 'President'), ('President-Elect', 'President-Elect'), ('Spiritual Leader', 'Spiritual Leader'), ('Asst. Spiritual Leader', 'Asst. Spiritual Leader'),
               ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Registrar', 'Registrar'), ('Team Selection', 'Team Selection'), ('Agape', 'Agape'), ('Kitchen', 'Kitchen'),
               ('Columbus Cluster Leader', 'Columbus Cluster Leader'), ('Manchester Cluster Leader', 'Manchester Cluster Leader'), ('Angels/Candlelight', 'Angels/Candlelight'), 
               ('Purchaser/Book Table', 'Purchaser/Book Table'), ('Worship', 'Worship'), ('Music', 'Music'), ('Communication', 'Communication'), ('Face to Face', 'Face to Face')]
    member_position = forms.ChoiceField(label="Member Position", choices=CHOICES)
    member_name = forms.CharField(label="Member Name", max_length=300)