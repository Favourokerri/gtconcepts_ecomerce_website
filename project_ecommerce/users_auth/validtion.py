""" this is to handel an validation in views"""
from django.contrib import messages
import re

def validate_password(request, password, confirm_password):
    """ validation of password"""
    #if len(password) < 8:
        #messages.warning(request, 'your password must be at least\
         #             8 characters long')
        #return False
    
    if password != confirm_password:
        messages.warning(request, 'password dose not match')
        return False
    
   # if not re.search("[0-9]", password):
    #    messages.warning(request, "Password must contain at least one digit.")
     #   return False

    
    else:
        return True

