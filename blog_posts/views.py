import os
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, get_object_or_404

from .models import BlogPost


def blog_posts(request):
  posts = BlogPost.objects.order_by('-upload_date')

  paginator = Paginator(posts, 6)
  page = request.GET.get('page')
  paged_posts = paginator.get_page(page)

  if request.method == 'POST':
    ful_name    = request.POST['full_name']
    email       = request.POST['email']
    subject     = request.POST['subject']
    message     = request.POST['message']

    # Send email
    send_mail(
      subject,
      'You have a new message from ' + ful_name + '.' + '\n' + message,
      email,
      [os.environ.get('EMAIL')],
      fail_silently=False
    )

    messages.success(request, '! Your message has been sent. We will get back to you as soon as possible!')
    return redirect('blog_posts')

  context = {
    'title': 'Blog Posts',
    'queryset': paged_posts,
  }
  return render(request, 'blog_posts/blog_posts.html', context)


def blog_post(request, slug):
  post = get_object_or_404(BlogPost, slug=slug)

  if request.method == 'POST':
    ful_name    = request.POST['full_name']
    email       = request.POST['email']
    subject     = request.POST['subject']
    message     = request.POST['message']

    # Send email
    send_mail(
      subject,
      'You have a new message from ' + ful_name + '.' + '\n' + message,
      email,
      [os.environ.get('EMAIL')],
      fail_silently=False
    )
    messages.success(request, '! Your message has been sent. We will get back to you as soon as possible!')
    return redirect('blog_post', slug)

  context = {
    'title': 'Blog Post ' + post.title,
    'queryset': post,
  }
  return render(request, 'blog_posts/blog_post.html', context)
