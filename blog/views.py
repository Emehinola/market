from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import login_required
from . models import Blog, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView, DetailView

# blog  class based view
class PostListView(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = "blog/blog.html"

class PostDetailView(DetailView):
    model  = Blog
    template_name = "blog/single-blog.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        context['form'] = form
        return context

class CommentCreate(CreateView):
    model = Comment
    form_class  = CommentForm()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

# single blog news
# def single(request, id):
#     details = Blog.objects.get(id=id)
#     commentForm = CommentForm(request.POST) # form
#     if request.method == "POST":
#         if commentForm.is_valid():
#             comment = commentForm.save(commit=False)
#             comment.author = request.user # getting user that writes comment
#             comment.post_id_id = id # getting post to which the comment belongs
#             comment.save() # saving the comment form
#             commentForm = CommentForm() # creating unbound/empty form after submitting a comment
#             return redirect(f'/blog/single/{id}')
#     else:
#         commentForm = CommentForm()

#     try: # checking if there is no comment yet
#         comments = Comment.objects.all()
#     except details.DoesNotExist:
#         comments = None
   
#     # GETTING THE NEXT AND PREVIOUS POST 
#     try: # checking if current post has previous or next one
#         next_post = Blog.objects.filter(id=int(id)+1)
#         previous_post = Blog.objects.filter(id=int(id)-1)
#     except next_post.DoesNotExist & previous_post.DoesNotExist:
#         pass
    
#     context = {
#         'post': details,
#         'comments': comments,
#         'form': commentForm,
#         'next_post': next_post,
#         'previous_post': previous_post
#     }
#     return render(request, 'blog/single-blog.html', context)