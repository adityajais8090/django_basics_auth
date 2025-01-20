from django import forms

class VoteForm(forms.Form):

    CHOICES = (
        (1, "Options 1"),
        (2, "Options 2"),
        (3, "Options 3"),
    )

    choice = forms.ChoiceField(choices = CHOICES, widget= forms.RadioSelect())