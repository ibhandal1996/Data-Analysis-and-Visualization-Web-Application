from django.db import models


class MockData(models.Model):
    PID = models.CharField(max_length=5, unique=True)
    Histology_A_0 = models.PositiveIntegerField()
    Histology_B_0 = models.PositiveIntegerField()
    Histology_C_0 = models.PositiveIntegerField()
    Biomarker_M_0 = models.FloatField()
    Biomarker_H_0 = models.FloatField()
    Biomarker_T_0 = models.FloatField()
    Biomarker_L_0 = models.FloatField()
    Biomarker_A_0 = models.FloatField()
    Histology_A_12 = models.PositiveIntegerField()
    Histology_B_12 = models.PositiveIntegerField()
    Histology_C_12 = models.PositiveIntegerField()
    Biomarker_M_12 = models.FloatField()
    Biomarker_H_12 = models.FloatField()
    Biomarker_T_12 = models.FloatField()
    Biomarker_L_12 = models.FloatField()
    Biomarker_A_12 = models.FloatField()

    def __str__(self):
        return f'{self.PID}'

