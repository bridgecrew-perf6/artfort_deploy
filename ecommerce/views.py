from django.shortcuts import render
from django.http import HttpResponse
from Product.models import Category,Product,BannerImages
from ecommerce.models import Setting
from math import ceil

# Create your views here.
def home(request):
	slide_images=BannerImages.objects.all()
	setting=Setting.objects.get(id=1)
	nSlides=len(slide_images)
	print(nSlides)
	context={
	       'slide_images':slide_images,
	       'rang':range(1,nSlides),
	       'setting':setting
	}
	return render(request,'ecommerce/home.html',context)

def contact(request):
	setting=Setting.objects.get(id=1)
	context={
	       'setting':setting
	}
	return render(request,'ecommerce/contact.html',context)