from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .form import LoginForm, SignupForm, MyprofileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from .models import Blog, Comment, Profile
from django.utils import timezone

u_id = 0
# import googlemaps
# gmaps = googlemaps.Client(key=settings.GMAPS_API_KEY) # google map api key


# Create your views here.
def forget(request):
	if request.method == 'POST':
		user = User.objects.get(email=request.POST.get('email'))
		import pdb; pdb.set_trace()
		if user is not None:
			print("Sending Email")
			mail_title = 'Test Email'
			message = 'This is a reset password link [ http://127.0.0.1:8000/set_new_pass/?user_id='+str(user.id)+' ].' 
			recipients = ['kuldeepkhatke03@gmail.com',]
			import pdb; pdb.set_trace()
			send_mail(mail_title, message, settings.EMAIL_HOST_USER, recipients, fail_silently=False)
			print("Email Sent")
			messages.add_message(request,50,"Reset Password link sent to Your Email...")
			return render(request, 'blogapp/forget.html')
		else:
			messages.warning(request,'Invalid Email Id...')
			return render(request, 'blogapp/forget.html')

	else:
		return render(request, 'blogapp/forget.html')

def set_new_pass(request):
	global u_id
	if request.method == 'POST':
		import pdb; pdb.set_trace()
		user = User.objects.get(id=u_id)
		u_id = 0
		if user is not None:
			if request.POST.get('n_pass') == request.POST.get('c_pass'):
				user.set_password(request.POST['n_pass'])
				user.save()

				messages.add_message(request,50,'Your password Updated Successfully...')
				return render(request,'blogapp/login')
			else:
				messages.add_message(request,50, "Plz enter valid confirm password")
				return render(request,'blogapp/set_new_pass.html')
	import pdb; pdb.set_trace()
	u_id = request.GET['user_id']
	return render(request, 'blogapp/set_new_pass.html', {})



from django.conf import settings
from django.core.mail import send_mail

@login_required
def dashboard(request):
	blogs = Blog.objects.all()
	return render(request, 'blogapp/dashboard.html', {'blogs': blogs})

@login_required
def index(request):
	blogs = Blog.objects.all()
	return render(request, 'blogapp/index.html', {'blogs':blogs})

@login_required
def about(request):
	return render(request, 'blogapp/about.html', {})

@login_required
def contact(request):
	return render(request, 'blogapp/contact.html', {})

@login_required
def recipes(request):
	blogs = Blog.objects.all()
	import pdb; pdb.set_trace()
	return render(request, 'blogapp/recipes.html', {'blogs': blogs})

@login_required
def recipe_single(request):
	b_id = request.GET['id']
	blog = Blog.objects.get(id=b_id)
	return render(request, 'blogapp/recipe-single.html', {"blog": blog})

@login_required
def edit_recipe(request):
	if request.method == "POST":
		b = Blog.objects.get(id=request.POST['b_id'])
		b.title = request.POST['b_title']
		b.b_text = request.POST['b_text']
		b.save()
		return redirect('../recipe-single/?id='+str(b.id))

	b_id = request.GET['id']
	blog = Blog.objects.get(id=b_id)
	return render(request, 'blogapp/edit_recipe.html', {"blog": blog})

@login_required
def createblog(request):
	if request.method == 'POST':
		user = User.objects.get(email=request.user.email)
		Blog.objects.create(created=timezone.now(),user=user,title=request.POST['title'], b_text=request.POST['b_text'], image= request.POST['b_image'])
		messages.add_message(request,50,'Blog Uploded...')
		return redirect('/dashboard')
	return render(request, 'blogapp/createblog.html', {})

@login_required
def feed(request):
	blogs = Blog.objects.all()
	return render(request, 'blogapp/feed.html', {'blogs': blogs})

def Login(request):
	
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		
		# if login_form.is_valid():
  		# users = User.objects.all()
		email=request.POST.get('email')
		password=request.POST.get('password')
		user_ob=User.objects.get(email=email)
		# import pdb; pdb.set_trace()
		username = user_ob.username
		user = authenticate(username=username, password=password)
		
		if user is not None:
			login(request, user)
			#return render(request, 'blogapp/dashboard.html',{})
			return redirect('/dashboard/')
		else:
			messages.warning(request,'User DoesNotExist')
		# else:
		# 	messages.warning(request,'Please enter valid data')
		return Httpresponse(messaged, status=302 )
		return render(request, 'blogapp/login.html' , {'login_form': login_form } )

	if request.user.is_active:
		return redirect('/dashboard/')
	
	login_form = LoginForm() 
	return render(request, 'blogapp/login.html' , {'login_form': login_form} )	
	

	

#********************************************************************
@login_required
def logout_view(request):
	logout(request)
	return redirect('/login/')


def signup(request):

	if request.method == 'POST':
		signup_form = SignupForm(request.POST)
		# try:
		if signup_form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']
			check_existance = User.objects.filter(email=email).exists()
			
			if check_existance:
				messages.warning(request, "Email already exist, Please enter unique email")
				return redirect('/blogapp/signup/')

			else:
				signup_form.save()
				user = authenticate(username=username, password=password)
				Login(request)
				return render(request, 'blogapp/dashboard.html', {})

		context = {'signup_form': signup_form }
		return render(request, 'blogapp/signup.html' , context )
		
	else:
		signup_form = SignupForm() 
		context = {'signup_form': signup_form }
		return render(request, 'blogapp/signup.html' , context )




@login_required
def myprofile(request):
	import pdb; pdb.set_trace()
	if request.method == 'POST':
		user = User.objects.get(email=request.user.email)
		user.first_name=request.POST['fnm']
		user.last_name=request.POST['lnm']
		user.save()
		# import pdb; pdb.set_trace()

		request.session['fnm']=user.first_name
		request.session['lnm']=user.last_name
		
		messages.add_message(request,50,"Profile Updated Successfully...")
		return render(request, 'blogapp/dashboard.html', {})
		
	else:
		return render(request, 'blogapp/myprofile.html' , {} )


@login_required
def resetpass(request):
	if request.method == 'POST':
		# import pdb; pdb.set_trace()
		#user = User.objects.get(email=request.user.email)
		# if request.user.check_password(request.POST['o_pass']):
		if check_password(request.POST['o_pass'], request.user.password):
			user = User.objects.get(id=request.user.id)
			user.set_password(request.POST['n_pass'])
			user.save()
			
			# user.save()
			messages.add_message(request,50,'Your password Updated Successfully...')
			return render(request,'blogapp/dashboard.html')
		else:
			messages.add_message(request,50, "Plz enter valid current password")
			return render(request,'blogapp/resetpass.html')
		
	else:
		return render(request, 'blogapp/resetpass.html')