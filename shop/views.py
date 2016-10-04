from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from shop.models import Category, Product, Order
from shop.forms import AppForm
import random
from django.contrib import auth
# Create your views here.

def shop(request):
	context = {}
	context['allcategories'] = Category.objects.all()
	context['flcats'] = Category.objects._mptt_filter(level = 0)

	if 'basketlist' in request.session:
		prods = Product.objects.filter(pk__in=request.session['basketlist'])
		context['pc'] = len(prods)
	else:
		context['pc'] = 0

	return render(request, 'shop/shop.html', context)

def get_category_cont(request, category_id):
	context = {}
	context['allcategories'] = Category.objects.all()
	context['content'] = Category.objects._mptt_filter(parent = category_id)
	context['isprod'] = False
	context['category'] = Category.objects.get(id = category_id)
	context['parent'] = context['category'].parent
	if not context['content']:
		context['content'] = Product.objects.filter(category = category_id)
		context['isprod'] = True

	if 'basketlist' in request.session:
		prods = Product.objects.filter(pk__in=request.session['basketlist'])
		context['pc'] = len(prods)
	else:
		context['pc'] = 0

	print(context['content'])
	return render(request, 'shop/get_category_cont.html', context)

def get_product_cont(request, product_id):
	context = {}
	context['prod'] = Product.objects.get(id = product_id)

	if 'basketlist' in request.session:
		prods = Product.objects.filter(pk__in=request.session['basketlist'])
		context['pc'] = len(prods)
	else:
		context['pc'] = 0

	return render(request, 'shop/get_product_cont.html', context)

def basket(request):
	context = {}
	context['countlist'] = {}
	context.update(csrf(request))
	context['form'] = AppForm(request.GET)
	context['message'] = ''
	if 'basketlist' not in request.session:
		prods = list()
	else:
		prods = Product.objects.filter(pk__in=request.session['basketlist'])

	context['pc'] = len(prods)

	if request.GET:
		l = list()
		for p in prods:
			s = 'input_count_' + str(p.id)
			l.append(request.GET[s])
		context['countlist'] = l

		if context['form'].is_valid():
			context['message'] = 'Заказ отправлен'
			context['form'].save()
			order = Order.objects.latest('id')
			i = 0
			s = ''
			for p in prods:
				s = s + 'Продукт: ' + str(p.name)  + ' Количество: ' + str(l[i]) + ';   '
				i = i+1
			order.prodlist = s
			order.save()
			request.session.set_expiry(1)
		else:
			context['message'] = 'Контактные данные не заполнены или заполнены не правильно'

	context['prods'] = prods
	print(context['countlist'])
	return render_to_response('shop/basket.html', RequestContext(request, context))

def add(request, product_id):
	context = {}
	request.session.set_expiry(3600)
	if 'basketlist' not in request.session:
		request.session['basketlist'] = list()

	if int(product_id) in request.session['basketlist']:
		print('None')
	else:
		request.session['basketlist'].append(int(product_id))

	prods = Product.objects.filter(pk__in=request.session['basketlist'])
	context['pc'] = len(prods)

	context['prod'] = Product.objects.get(id=product_id)

	return render_to_response('shop/get_product_cont.html', RequestContext(request, context))

def delete(request, product_id):
	context = {}
	request.session.set_expiry(3600)
	prods = list()
	if 'basketlist' in request.session:
		request.session.modified = True
		request.session['basketlist'][request.session['basketlist'].index(int(product_id))] = -1
		print(request.session['basketlist'])
		context['message'] = "Товар удален"

	prods = Product.objects.filter(pk__in=request.session['basketlist'])
	context['pc'] = len(prods)
	context['prods'] = prods

	return render_to_response('shop/basket.html', RequestContext(request, context))