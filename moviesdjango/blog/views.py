from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Category,Post

class HomeView(View):
    """Вывод всех постов с категориями"""
    def get(self,request):
        post_list = Post.objects.filter(published_date__lte=datetime.now(),published=True)
        categories_list = Category.objects.all()
        return render(request,'blog/home.html',{'posts':post_list,'categories':categories_list})
 
class  PostDetailView(View):
    """Полная статья"""
    def get(self,request,category,slug):
        post = Post.objects.get(slug=slug)
        categories_list = Category.objects.all()
        return render(request,'blog/post_detail.html',{'post':post,'categories':categories_list})
    
class CategoryView(View):
    """Вывод статей по его категориям"""
    def get(self,request,slug):
        category_list = Category.objects.get(slug=slug)
        return render(request,'blog/post_list.html',{'categories':category_list})
        
    
    

        
