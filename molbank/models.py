from django.db import models

# Create your models here.
class molbank(models.Model):
    ID = models.CharField(default='DUMMY_ID',primary_key=True,max_length=10)
    SMILES = models.CharField(default='DUMMY_SMILES',max_length=150)
    SAMPLE_CODE = models.CharField(default='DUMMY_SAMPLE_CODE',max_length=20)

# class all_products(models.Model):
#     def get_all_products():
#         items = []
#         with open('EXACT FILE PATH OF YOUR CSV FILE','r') as fp:
#             # You can also put the relative path of csv file
#             # with respect to the manage.py file
#             reader1 = csv.reader(fp, delimiter=',')
#             for value in reader1:
#                 items.append(value)
#         return items