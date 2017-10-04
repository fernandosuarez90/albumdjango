# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	


	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name				


class Photo(models.Model):


	category = models.ForeignKey(Category, null=True, blank=True)
	title = models.CharField(max_length=50, default='No title')
	photo = models.ImageField(upload_to='photos/')		
	pub_date = models.BooleanField(default=False)
	comment = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
			return reverse('photo-list')