from django import forms
class contactForm(forms.Form):
    name= forms.CharField(max_length=100, label="User name")
    email= forms.EmailField(label="User Email")
    file = forms.FileField(label="File")
    # age=forms.IntegerField()
    # weight= forms.FloatField()
    # balance= forms.DecimalField()
    # check= forms.BooleanField()
    # birthDay= forms.DateField()
    # appointment= forms.DateTimeField()
    # CHOICES= (('male', 'male'), ('female', 'female'))
    # CHOICES_ONE=(("S", "SMALL"),("M", "MEDIUM"),("L", "LARGE"))
    # gender= forms.ChoiceField(choices=CHOICES)
    # size= forms.ChoiceField(choices=CHOICES_ONE)