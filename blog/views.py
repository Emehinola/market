from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from . models import Blog, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# blog view
def blog(request):
    posts = Blog.objects.all() # getting query from the database
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2) # splitting the blog posts 2 posts per page
    
    try:
        post_pagination = paginator.page(page)
    except PageNotAnInteger:
        post_pagination = paginator.page(1)
    except EmptyPage:
        post_pagination = paginator.page(paginator.num_pages)

    context = {
        'blogs': posts,
        'post_pagination': post_pagination
    }
    return render(request, 'blog/blog.html', context)

# single blog news
def single(request, id):
    details = Blog.objects.get(id=id)
    commentForm = CommentForm(request.POST) # form
    if request.method == "POST":
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.author = request.user # getting user that writes comment
            comment.post_id_id = id # getting post to which the comment belongs
            comment.save() # saving the comment form
            commentForm = CommentForm() # creating unbound/empty form after submitting a comment
            return redirect(f'/blog/single/{id}')
    else:
        commentForm = CommentForm()

    try: # checking if there is no comment yet
        comments = Comment.objects.all()
    except details.DoesNotExist:
        comments = None
   
    # GETTING THE NEXT AND PREVIOUS POST 
    try: # checking if current post has previous or next one
        next_post = Blog.objects.filter(id=int(id)+1)
        previous_post = Blog.objects.filter(id=int(id)-1)
    except next_post.DoesNotExist & previous_post.DoesNotExist:
        pass
    
    context = {
        'post': details,
        'comments': comments,
        'form': commentForm,
        'next_post': next_post,
        'previous_post': previous_post
    }
    return render(request, 'blog/single-blog.html', context)