from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

def index(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/index.html',content)

def restaurantDetail(request):
    return render(request,"shareRes/restaurantDetail.html")

def restaurantCreate(request):
    categories = Category.objects.All()
    content = {'categories': categories}
    return render(request,"shareRes/restaurantCreate.html",content)

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}

    return render(request,"shareRes/categoryCreate.html",content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()

    return HttpResponseRedirect(reverse('cateCreatePage'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category(id = category_id)
    delete_category.delete()

    return HttpResponseRedirect(reverse('cateCreatePage'))