from django.shortcuts import render

# Create your views here.
def sing_up(request):
    """" view for handling signing up"""
    return render(request,'sign-up.html')

def log_in(request):
    """ view for handling loging in"""
    return render(request, 'login.html')
