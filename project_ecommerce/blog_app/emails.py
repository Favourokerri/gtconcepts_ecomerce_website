from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def send_mail_after_blog_post(blogs, user_emails):
    subject = "New blog_post"
    
    for email in user_emails:
        html_content = render_to_string('email/email_template_blog.html', {'blogs': blogs})
        
        msg = EmailMultiAlternatives(subject, 'New order notification', settings.EMAIL_HOST_USER, [email])
        msg.attach_alternative(html_content, "text/html")
        
        msg.send()
