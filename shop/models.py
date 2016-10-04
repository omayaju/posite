from django.db import models
from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import mptt
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
	name = models.CharField(verbose_name = 'Имя категории', max_length = 200, null=True, blank=True)
	description = models.TextField(verbose_name='Описание категории', null=True, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name = 'В категории: ')
	img = models.ImageField(upload_to="images/", null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Категория'
		verbose_name_plural = u'Категории'
		ordering = ('tree_id', 'level')

	class MPTTMeta:
		order_insertion_py = ['name']

mptt.register(Category, order_insertion_py = ['name'])

class Order(models.Model):
	pername = models.CharField(verbose_name = 'Имя заказчика', null=True, max_length = 200)
	perphone = models.CharField(verbose_name = 'Контактный телефон', null=True, max_length = 200)
	peremail = models.EmailField(verbose_name = 'E-mail', null=True, max_length = 200)
	prodlist = models.TextField(verbose_name='Заказной лист', null=True)

	def __str__(self):
		return u'Заказ №' + str(self.id)

	class Meta:
		verbose_name = u'Заказ'
		verbose_name_plural = u'Заказы'
		ordering = ['-id']

class Product(models.Model):
	name = models.CharField(verbose_name='Название продукта', max_length=200, null=True, blank=True)
	sdesc = models.CharField(verbose_name='Краткое описание', max_length=200, null=True, blank=True)
	compos = models.TextField(verbose_name='Состав', null=True, blank=True)
	cost = models.BigIntegerField(verbose_name='Стоимость', null=True, blank=True)
	app = models.TextField(verbose_name='Показания к применению и применение', null=True, blank=True)
	care = models.TextField(verbose_name='Уход', null=True, blank=True)
	description = models.TextField(verbose_name='Описание товара', null=True, blank=True)
	category = TreeForeignKey(Category, null=True, blank=True, related_name='cat', verbose_name='В категории: ')
	img = models.ImageField(verbose_name = 'Основное изображение', upload_to="images/", null=True, blank=True)
	back = models.ImageField(verbose_name='Акционный фон', upload_to="images/", null=True, blank=True)

	ACTION_CHOISE = (
		("Да", 'Да'),
		("Нет", 'Нет'),
	)

	action = models.CharField(verbose_name = 'Акционный?', null=True, max_length = 3, choices = ACTION_CHOISE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Продукт'
		verbose_name_plural = u'Продукты'