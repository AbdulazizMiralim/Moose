from django.shortcuts import render, redirect
from .models import Post, Comments, Contact
from django.core.paginator import Paginator
import requests

BOT_TOKEN = '6329710513:AAEexH--8D2WbX4EY5EkzFydx_9UzEfa67s'
CHAT_ID = 532415249


def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-view_count')[:2]
    data = {
        'posts': posts, 'home': 'active'

    }
    return render(request, 'index.html', context=data)


def blog_view(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
        d = {
            'posts': posts,
            'blog': 'active',
        }
        return render(request, 'blog.html', context=d)

    posts = Post.objects.filter(is_published=True)
    page_obj = Paginator(posts, 2)

    d = {
        'blog': 'active',
        'posts': page_obj.get_page(page)

    }
    return render(request, 'blog.html', context=d)


def blog_singel_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        comment = Comments.objects.create(post_id=pk, name=data['name'], email=data['email'], message=data['message'])
        comment.save()
        return redirect(f'/blog/{pk}/')
    post = Post.objects.filter(id=pk).first()
    post.view_count += 1
    post.save(update_fields=['view_count'])
    comments = Comments.objects.filter(post_id=pk)
    data = {
        'post': post, 'blog': 'active',
        'comments': comments
    }
    return render(request, 'blog-single.html', context=data)


def about_view(request):
    return render(request, 'about.html', context={'about': 'active'})


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        object = Contact.objects.create(full_name=data['name'], email=data['email'], subject=data['subject'],
                                        message=data['message'])
        object.save()
        text = f"""
        project: MOOSE 
        id: {object.full_name}
        subject: {object.subject}
        message: {object.message}
        timestmep: {object.created_at} 
        """
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sentMessage/?chat_id={CHAT_ID}&text={text}'
        response = requests.get(url)
        print(response)
        return redirect('/contact')

    return render(request, 'contact.html', context={'contact': 'active'})
