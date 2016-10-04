from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from shop.models import Product
import random
from django.contrib import auth
# Create your views here.

def index(request):
	context = {}
	prods = Product.objects.filter(action = "Да")
	for p in prods:
		p.description = p.description[:100] + " ..."
	context['actionprods'] = prods

	if 'basketlist' in request.session:
		prods2 = Product.objects.filter(pk__in=request.session['basketlist'])
		context['pc'] = len(prods2)
	else:
		context['pc'] = 0

	return render(request, 'main/index.html', context)

def about(request):
	context = {}
	if 'basketlist' in request.session:
		prods2 = Product.objects.filter(pk__in=request.session['basketlist'])
		context['pc'] = len(prods2)
	else:
		context['pc'] = 0

	return render(request, 'main/about.html', context)