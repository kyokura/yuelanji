from django.shortcuts import render,render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from .models import Marticle, Sarticle
from datetime import datetime
from django.http import Http404
# Create your views here.
def home(request):
    form=SignUpForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/thankyou/')
    
    return render_to_response("signup.html",locals(),
                              context_instance=RequestContext(request))
#museum article starts from here-------------------------------------------
def museum(request):
    post_list=Marticle.objects.all()
    return  render(request,'museum.html',{'post_list':post_list})
def detail(request,id):
    try:
        post =Marticle.objects.get(id=str(id))
    except Marticle.DoesNotExist:
        raise Http404
    return render (request,'post.html',{'post':post})
def search_tag(request,tag):
    try:
        post_list =Marticle.objects.filter(category=tag)
    except Marticle.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})

def k_tag(request):
    try:
        post_list =Marticle.objects.filter(category='k')
    except Marticle.DoesNotExist:
        raise Http404
    return render(request,'ktag.html',{'post_list':post_list})
def x_tag(request):
    try:
        post_list =Marticle.objects.filter(category='x')
    except Marticle.DoesNotExist:
        raise Http404
    return render(request,'ktag.html',{'post_list':post_list})
#museum article ends here------------------------------------------------


#commercial article starts form here-------------------------------------

def commercial(request):
    post_list=Sarticle.objects.all()
    return  render(request,'commercial.html',{'post_list':post_list})
def detail2(request,id):
    try:
        post =Sarticle.objects.get(id=str(id))
    except Sarticle.DoesNotExist:
        raise Http404
    return render (request,'post.html',{'post':post})

def search_tag2(request,tag2):
    try:
        post_list =Sarticle.objects.filter(category=tag2)
    except Sarticle.DoesNotExist:
        raise Http404
    return render(request,'tag2.html',{'post_list':post_list})

def z_tag(request):
    try:
        post_list =Sarticle.objects.filter(category='z')
    except Sarticle.DoesNotExist:
        raise Http404
    return render(request,'ztag.html',{'post_list':post_list})
def q_tag(request):
    try:
        post_list =Sarticle.objects.filter(category='q')
    except Sarticle.DoesNotExist:
        raise Http404
    return render(request,'ztag.html',{'post_list':post_list})
#commercial article ends here--------------------------------------------


def thankyou(request):
    
    return render_to_response("thankyou.html",locals(),
                              context_instance=RequestContext(request))
def more(request):
    
    return render_to_response("more.html",locals(),
                              context_instance=RequestContext(request))