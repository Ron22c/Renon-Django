from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q
from blog import models
from blog import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView,
                                                CreateView, UpdateView,
                                                DeleteView)

### Post Section ###

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    # context_object_name = post_list
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    # context_object_name = post
    model = models.Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = models.Post

class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = models.Post

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('post_list')

class DraftPostView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull = True).order_by('create_date')

### Comment Section ###

@login_required
def publish_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit= False)
            comment.post = post
            comment.save()
            return redirect('post_detail',  pk = post.pk)
    else:
        form = forms.CommentForm()

    return render(request, 'blog/comment_form.html', context = {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.approve()
    return redirect('post_detail', pk=post_pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def search(request):
    if request.method == 'GET':
        post_title =  request.GET.get('search')
        _post = models.Post.objects.filter(title__icontains=post_title)
        return render(request,"post_list.html",{"post_list":_post})
    else:
        return render(request,"post_list.html",{})
