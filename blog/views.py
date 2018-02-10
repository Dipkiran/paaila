from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render

def createpost(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Created !!!")
        return HttpResponseRedirect(instance.get_absolute_url())


    context = {
        "form":form,
    }
    return render(request, 'add.html',context)


def listitems(request):
    queryset_list = Post.objects.all()
    query =request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

            ).distinct()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_req_var = "page"
    page = request.GET.get(page_req_var)
    queryset = paginator.get_page(page)
    context={
        "object_list" : queryset,
        "page_req_var" : page_req_var
    }
    return render(request, 'list.html',context)

def postdetail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context={
        "title": instance.title,
        "instance" : instance
    }
    return render(request, 'postdetail.html',context)


def update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "title": instance.title,
        "instance" : instance,
        "form" : form
    }
    return render(request, 'add.html',context)

def delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request,"Successfully deleted")
    return redirect("blog:list")
