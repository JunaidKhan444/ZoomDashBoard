from django import forms

class EditForm(forms.Form):
    Meeting_Topic = forms.CharField(max_length=100)
    Meeting_Start_Date = forms.DateTimeField()
    Duration = forms.IntegerField()
    Password = forms.CharField(max_length=50)
    