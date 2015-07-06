# Import the forms library to create forms
from django import forms

# Create a form class extending django.forms.Form.
# Various field types like CharField, EmailField and etc., are
# available in forms library. By specifying the field types and
# other conditions in the below form class, we automatically get
# all the necessary validation of the submitted data.
#
# See https://docs.djangoproject.com/en/1.6/ref/forms/fields/ for
# the complete list of all the available fields.
class ContactForm(forms.Form):
  subject = forms.CharField()
  email = forms.EmailField()
  message = forms.CharField()
