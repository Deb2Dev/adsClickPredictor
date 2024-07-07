from django import forms

class inputs(forms.Form):
    age = forms.IntegerField( 
                     help_text = "Enter Age"
                     ) 
    
    salary = forms.IntegerField( 
                     help_text = "Enter full figure in digits"
                     ) 