from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def send_mail_after_order(request, email, order_items):
    subject = "Your orders"
    html_content = render_to_string('email_template1.html', {'order_items': order_items})
    msg = EmailMultiAlternatives(subject, 'New order notification', settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_mail_after_order_to_admin(request, email, orders, order_items):
    subject = "New order"
    admin_users = User.objects.filter(is_staff=True)
    
    for admin in admin_users:
        context = {'orders': orders,
                   'order_items': order_items
                   }
        html_content = render_to_string('email_template2.html', context)
        
        msg = EmailMultiAlternatives(subject, 'New order notification', settings.EMAIL_HOST_USER, [admin.email])
        msg.attach_alternative(html_content, "text/html")
        
        msg.send()