import os
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
  if request.method == 'POST':
    full_name    = request.POST['full_name']
    email       = request.POST['email']
    subject     = request.POST['subject']
    message     = request.POST['message']

    # Send email
    send_mail(
      subject,
      'You have a new message from ' + full_name + '.' + '\n' + message + '\n Contact email: ' + email,
      email,
      [os.environ.get('EMAIL')],
      fail_silently=False
    )

    messages.success(request, '! Your message has been sent. We will get back to you as soon as possible!')
    return redirect('index')
