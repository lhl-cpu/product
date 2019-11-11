from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
	title = models.CharField(default='抖音：记录美好生活',max_length=50)
	text = models.TextField(default='App简介')
	url = models.CharField(default='Http://',max_length=100)
	icno = models.ImageField(default='default.png',upload_to='images/')
	image = models.ImageField(default='1.jpg',upload_to='images/')

	votes = models.IntegerField(default=1)
	pub_date = models.DateTimeField()
	hunter = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title