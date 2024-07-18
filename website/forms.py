from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"First name", "class":"form-control"}),
        label="")
    
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"Last name", "class":"form-control"}),
        label="")
    
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"E-mail", "class":"form-control"}),
        label="")
    
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"Phone", "class":"form-control"}),
        label="")
    
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"Address", "class":"form-control"}),
        label="")
    
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"City", "class":"form-control"}),
        label="")
    
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"State", "class":"form-control"}),
        label="")
    
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"Zipcode", "class":"form-control"}),
        label="")
    
    class Meta:
            model = Record
            exclude = ("user",)


