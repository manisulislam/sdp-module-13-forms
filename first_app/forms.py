from django import forms
from django.core import validators
class contactForm(forms.Form):
    name= forms.CharField(max_length=100, label="User name",help_text="total length must be 50 characters",required=False, widget=forms.Textarea(attrs={'id':"text_area","class":"class_1 class_2","placeholder":"Enter your name :"}))
    email= forms.EmailField(label="User Email")
    file = forms.FileField(label="File")
    age=forms.CharField(widget=forms.NumberInput)
    # weight= forms.FloatField()
    # balance= forms.DecimalField()
    # check= forms.BooleanField()
    birthDay= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment= forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES= (('male', 'male'), ('female', 'female'))
    CHOICES_ONE=(("S", "SMALL"),("M", "MEDIUM"),("L", "LARGE"), ("XL", "EXTRA LARGE"))
    gender= forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    size= forms.ChoiceField(choices=CHOICES_ONE, widget=forms.RadioSelect)

# class student_data(forms.Form):
#     name= forms.CharField(max_length=100, widget=forms.TextInput)
#     email= forms.CharField(max_length=100, widget=forms.EmailInput)
    # def clean_name(self):
    #     name= self.cleaned_data['name']
    #     if len(name)<10:
    #         raise forms.ValidationError("name must be greater than 10 characters")
    #     return name
    # def clean_email(self):
    #     email= self.cleaned_data['email']
    #     if ".com" not in email:
    #         raise forms.ValidationError("email must be in .com")
    #     return email
    # def clean(self):
    #     cleaned_data= super().clean()
    #     valName= self.cleaned_data['name']
    #     valEmail= self.cleaned_data['email']
    #     if len(valName)<10:
    #         raise forms.ValidationError("name must be greater than 10 characters")
    #     if ".com" not in valEmail:
    #         raise forms.ValidationError("email must be in .com")
        
       
class student_data(forms.Form):
    name= forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message="enter at least 10 characters")])
    email= forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="enter valid email ")])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18, message="enter at least 18 years"), validators.MaxValueValidator(24, message="age must be 24 years")])
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=["pdf"], message="only pdf file is allowed")])
    
    
class passwordValidatorProject(forms.Form):
    name= forms.CharField(max_length=100)
    password= forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)