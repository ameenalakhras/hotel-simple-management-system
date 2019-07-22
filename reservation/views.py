from django.shortcuts import render
# from django.core.mail import send_mail
from django.shortcuts import redirect, render

from mail.views import send_mail


def send_message(request):

    to_emails = 'amin602123@gmail.com'
    subject = 'HI'
    html_content = '<strong> just using the thing <strong>'

    received, info = send_mail(to_emails=to_emails, subject=subject, html_content=html_content)
    if received:
        print(f"status code {info['status_code']}, response message : {info['body']}")
    else:
        print(f"an error has occurred : {info}")
    return redirect("/")