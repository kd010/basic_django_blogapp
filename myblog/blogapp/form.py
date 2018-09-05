from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS	


# Create the form class.
class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']

class SignupForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		
		error_messages = {
			NON_FIELD_ERRORS :{
				'unique_together': "%(model_name)s's %(field_labels)s are not unique."
			}
		}


	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	if '.com' not in email:
	# 		raise forms.ValidationError('Please enter email having extension (.com)')
	# 	return 'email'


	def save(self):
		username = self.cleaned_data['username']
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		user = User.objects.create()
		user.username = username
		user.email = email
		user.set_password(password)
		user.save()	

	# def clean_email(self):
	# 	import pdb; pdb.set_trace()
		
	# 	# if not '.com' in email:
		
	# 	raise forms.ValidationError("Please enter an valid email address which ends with .com")

class MyprofileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']