from django import forms

CHOICES = [('Y', 'Yes'), ('N', 'No')]
FEACHER_CHOICES = [('f5', 'Feature 5'), ('f6', 'Feature 6'), ('f7', 'Feature 7'), ('f8', 'Feature 8')]
FAMOUS_CHOICES = [('W', 'Who'), ('P', 'Pars'), ('S', 'Score')]
USER_METHODS_CHOICES = [('A', 'age'), ('H', 'hdl'), ('B', 'bmi'),
                        ('D', 'diabets'), ('L', 'LDL'), ('R', 'RACE'),
                        ('T', 'totalcholestorul'), ('W', 'whr'), ('F', 'family histor'),
                        ('S', 'sbp'), ('AU', 'automatice')]


class HomeForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[('M', 'Male'), ('F', 'Female')])
    deabetes = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    smoker = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    teat_porhigh = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    blood_dressure = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    family_history = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    wais = forms.FloatField()
    hip = forms.FloatField()
    weight = forms.FloatField()
    height = forms.FloatField()
    sy_stolic_blood = forms.FloatField()
    total_cholstrol = forms.FloatField()
    hdl_cholstorol = forms.FloatField()


class AiToolsP1Form(forms.Form):
    sample_file = forms.FileField()


class AiToolsP2Form(forms.Form):
    features = forms.MultipleChoiceField(choices=FEACHER_CHOICES, widget=forms.CheckboxSelectMultiple,label='')


class AiToolsP3Form(forms.Form):
    famous_method = forms.MultipleChoiceField(choices=FAMOUS_CHOICES, widget=forms.CheckboxSelectMultiple,label='')


class AiToolsP4Form(forms.Form):
    your_method = forms.MultipleChoiceField(choices=USER_METHODS_CHOICES, widget=forms.CheckboxSelectMultiple,label='')
