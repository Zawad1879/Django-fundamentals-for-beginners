from django.shortcuts import render
from django.urls import reverse
from .forms import PostForm
from .models import post
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context = {}
    form = PostForm(request.POST or None)
    title = 'Please create a post'

    if form.is_valid():
        confirm_message = "Thank you for filling up the form!"
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        obj = post(title = title, description = description)
        obj.save()
        form = None
        return HttpResponseRedirect(reverse('post:post_list'))


    context = {'title':title, 'form':form}
    template = 'post/post.html'
    return render(request,template,context)

def delete(request, post_id):
    post.objects.filter(id=post_id).delete()
    return HttpResponseRedirect(reverse('post:post_list'))


def post_list(request):
    allposts = post.objects.all()
    confirm_message = "Thank you for filling up the form!"
    context = {'title':'List of posts','confirm_message':confirm_message, 'allposts':allposts}
    template = 'post/post.html'
    return render(request,template,context)
