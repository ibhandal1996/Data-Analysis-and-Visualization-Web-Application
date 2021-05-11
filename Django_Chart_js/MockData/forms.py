from django import  forms

from .models import MockData


class MockDataForm(forms.ModelForm):
    class Meta:
        model = MockData
        fields = ('PID', 'Histology_A_0', 'Histology_B_0', 'Histology_C_0',
                  'Biomarker_M_0', 'Biomarker_H_0', 'Biomarker_T_0', 'Biomarker_L_0',
                  'Biomarker_A_0', 'Histology_A_12', 'Histology_B_12',
                  'Histology_C_12', 'Biomarker_M_12', 'Biomarker_H_12', 'Biomarker_T_12',
                  'Biomarker_L_12', 'Biomarker_A_12')