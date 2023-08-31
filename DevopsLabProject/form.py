from django import forms

NUMS= [
    ('rock', 'Rock'),
    ('paper', 'Paper'),
    ('scissor', 'Scissor'),

    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))