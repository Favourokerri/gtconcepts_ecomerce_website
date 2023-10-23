from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users_auth.validtion import validate_password
from user_profile.models import Profile
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import IntegrityError, OperationalError
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def send_mail_after_registration(email, auth_token):
    """ function that handels email for verifying accounts"""
    subject = "welcome to Gt concept. verify account to log in"
    message = f'Hi click, or paste this link to verify your account https://gtsplacest3.onrender.com/user/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)

def sign_up(request):
    """
        View for handling signing up
        we created profile_obj in order
        to store the is_verified field of the user
    """
    if request.method == 'POST':
        email = request.POST['email']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        hashed_password = make_password(password)
        
        # Check if password is valid
        if validate_password(request, password, confirm_password):
            try:
                user_obj = User.objects.create(username=email, email=email, first_name=first_name, password=hashed_password)
                profile_obj = Profile.objects.create(user=user_obj, auth_token=str(uuid.uuid4()))
                profile_obj.save()
                send_mail_after_registration(email, profile_obj.auth_token)
                messages.success(request, "your account has been registered successfully check email for verification")
                return redirect('token_send')
            except IntegrityError: # user alredy exits
                messages.error(request, 'This user already exists')
            except OperationalError as e:
                messages.error(request, "please input only vald characters no emojis")

    
    return render(request, 'registration/sign-up.html')

def token_send(request):
    """ view for our token page """
    return render(request, 'registration/token.html')

def resend_verification(request):
    """ resends verification if user dose not see it at first"""
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile_obj = Profile.objects.get(user__username=email)
            send_mail_after_registration(email, profile_obj.auth_token)
            messages.success(request, 'verification email has been sent successfully')
        except Profile.DoesNotExist:
            messages.warning(request, 'this email is not registered. please register')
            return redirect('signup')
        except OperationalError as e:
            messages.error(request, "please input only vald characters no emojis")

    return render(request, 'registration/resend_verification.html')

def verify_account(request, auth_token):
    """ for verification of account"""
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'Your account has been verified successfully log in')
        return redirect('login')

    
def log_in(request):
    """ view for handling loging in"""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        #get profie details to check if user is verified
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    profile = Profile.objects.create(user=user, auth_token=str(uuid.uuid4()))
                    profile.save()
                if profile.is_verified:
                    login(request, user)
                    messages.success(request, "login successfull")
                    return redirect('index')
                else:
                    messages.warning(request, 'account must be verified before login')
                    return redirect('token_send')
            else:
                messages.error(request, 'usernane and or password incorrect')
                return redirect('login')
        except OperationalError as e:
            messages.error(request, 'pleases input only valid characters no emojis')
        
    return render(request, 'registration/login.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    try:
        template_name = 'reset_password/password_reset.html'
        email_template_name = 'reset_password/password_reset_email.html'
        subject_template_name = 'registration/password_reset_subject.txt'  # Change this line
        success_message = "We've emailed you instructions for setting your password, " \
                        "if an account exists with the email you entered. You should receive them shortly." \
                        " If you don't receive an email, " \
                        "please make sure you've entered the address you registered with, and check your spam folder."
        success_url = reverse_lazy('index')
    except OperationalError as e:
            redirect('login')

def log_out(request):
    """ handel logout"""
    logout(request)
    messages.success(request, "logout successfully")
    return redirect('index')
