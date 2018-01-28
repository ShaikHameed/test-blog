from el_pagination.decorators import page_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, SiteImage, SiteLink, Comment, Paragraph



def index(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/index.html'
	latest_post_list = Post.objects.all()
	context = {'latest_post_list': latest_post_list}
	
	return render(request, template, context)
	#return HttpResponse("Testing..")

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})

def add_comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	p = Comment()
	p.comment_author = request.POST.get('i1')
	p.comment_text = request.POST.get('i2')
	p.post_id = post.id
	p.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(post.id, )))

def add_like(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.votes += 1
	post.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(post.id, )))

