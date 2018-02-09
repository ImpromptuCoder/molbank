from django import forms
# from django.forms import Textarea, Textbox
from .models import molbank
from django.contrib.auth.models import User
class contactForm(forms.Form):
    text_smiles = forms.CharField()
    text_smiles = forms.CharField()

class addForm(forms.ModelForm):
	class Meta:
		model = molbank
		fields = ["ID","SMILES","SAMPLE_CODE"]
		labels = {
			'ID': 'Enter the ID',
			'SMILES': 'Enter the Smiles',
			'SAMPLE_CODE': 'Enter the Sample Code'
		}

class loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput )

# class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         labels = {
#             'name': _('Writer'),
#         }
#         help_texts = {
#             'name': _('Some useful help text.'),
#         }
#         error_messages = {
#             'name': {
#                 'max_length': _("This writer's name is too long."),
#             },
#         }


