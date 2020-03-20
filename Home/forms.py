from django import forms
from .models import Doctor,Chemist,LabChemist

class DoctorCreate(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

class ChemistCreate(forms.ModelForm):

    class Meta:
        model = Chemist
        fields = '__all__'

class LabChemistCreate(forms.ModelForm):

    class Meta:
        model = LabChemist
        fields = '__all__'