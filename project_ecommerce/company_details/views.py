from django.shortcuts import render
from .models import Contact_detail, Terms_and_condition

# Create your views here.
def contact_us(request):
    """ contact us views """
    contacts = Contact_detail.objects.all()
    context = {"contacts": contacts}
    return render(request, 'main/contact.html', context)

def terms_and_conditions(request):
    terms = Terms_and_condition.objects.filter().first()
    context = {"terms": terms}
    return render(request, 'terms&conditions.html', context)