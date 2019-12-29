from django import forms


CHOICES=[('Y','Yes'),('N','No')]
class HomeForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=[('M','Male'),('F','Female')])
    deabetes = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,label='')
    smoker = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    teat_porhigh = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    blood_dressure = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    family_history = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    wais = forms.FloatField()
    hip = forms.FloatField()
    weight =forms.FloatField()
    height =forms.FloatField()
    sy_stolic_blood = forms.FloatField()
    total_cholstrol = forms.FloatField()
    hdl_cholstorol = forms.FloatField()