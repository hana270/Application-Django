from django import forms
from employee import models

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = models.Employee
        fields = "__all__"
        