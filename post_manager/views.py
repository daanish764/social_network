from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.views.generic.edit import FormMixin

from . models import Post, Comment, Like
from . forms import CommentForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

# Create your views here.

def index(request):
    return HttpResponse("Index")

class PostCreateView(CreateView):
    model = Post 
    fields = ['title', 'text']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post 

class PostDeleteView(DeleteView):
    model = Post 

    success_url = reverse_lazy('post:index')

    def get_form(self, form_class=None):
       form = super(PostDeleteView, self).get_form(form_class)
       form.helper = FormHelper()
       form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
       self.form_x = form
       return form


class PostDetailView(FormMixin, DetailView):
    model = Post 

    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user
            comment.post_id=self.object
            comment.save()
            return redirect('post:view', pk=self.object.id)
        else:
            return self.form_invalid(form)

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post_id.pk
    comment.delete()
    return HttpResponseRedirect(reverse('post:view', kwargs={'pk': post_id}))
