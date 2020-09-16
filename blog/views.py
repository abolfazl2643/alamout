from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from django.views.generic.detail import BaseDetailView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse
from .form import commentform
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .form import commentform
from django.views.generic.detail import SingleObjectMixin
from django.views import View



class UpdatePost(UpdateView,LoginRequiredMixin):
    model = Post
    template_name = "blog/update.html"
    fields = ['title', 'article']
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk' : self.kwargs.get('pk')})
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.author:
            return HttpResponse('you can not see this page !')
        return super().post(request, *args, **kwargs)


class DeletePost(DeleteView):
    model = Post
    template_name = "blog/post_detail.html"
    success_url = '/'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.author:
            return HttpResponse('you can not delete this post')
        return super().post(request, *args, **kwargs)


class post_list(ListView):
    model = Post
    template_name='blog/post_list.html'
    paginate_by = 2
    def get_queryset(self):
        self.post = Post.objects.filter(author = self.request.user)
        return self.post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    

class post_create(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'article']
    template_name = 'blog/post_create.html'
    success_url = '/' 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def post_detail(request,pk):
#     post = get_object_or_404(Post,pk=Post.objects.get(id=pk).id)
#     comments = post.comments.all()
#     template = 'blog/post_detail.html'
#     new_comment = None
#     user = User.objects.get(username=request.user).username
#     if request.method == 'POST':
#         comment_form = commentform(request.POST)
#         if comment_form.is_valid() : 
#             new_comment = comment_form.save(commit = False)
#             new_comment.author = user
#             new_comment.post = post 
#             new_comment.save()
#     else : 
#         comment_form = commentform()
#     return render(request ,'blog/post_detail.html', {'post':post , 'comments':comments ,
#      'comment_form':comment_form , 'new_comment':new_comment,'user':user })


class Post_Comment_List(SingleObjectMixin, ListView):
    template_name = 'blog/post_comment.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.object
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Post'] = self.object
        return context    
    def get_queryset(self):
        return Post.objects 

class post_comment(ListView):
    model = Comment
    template_name = 'blog/post_comment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Post'] = Post.objects.all()
        return context  


class Comment_Detail_View(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = commentform
        context['comments'] = Comment.objects.filter(post_id=self.kwargs.get('pk'))
        return context


class Limited_PostDetail_User_View(SingleObjectMixin,View):
    model = Post
    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        if  request.user != self.object.author :
            return HttpResponseForbidden()  
        self.object = self.get_object()
        return HttpResponseRedirect(reverse('post_detail',kwargs={'pk':self.object.pk}))    


class Comment_Form_View(CreateView):
    model = Comment
    template_name = "blog/post_detail.html"
    fields = ['massage']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk = self.kwargs.get('pk'))
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk' : self.kwargs.get('pk')})

   
def search(request):
    if request.GET.get('a') and request.GET.get('a') == 'abolfazl':
        message = 'yes we have it'
    else:
        message = 'You submitted nothing!'
    return HttpResponse(message)    

    


