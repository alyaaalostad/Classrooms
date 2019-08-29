from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher= models.ForeignKey(User,on_delete=models.CASCADE, default=1)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Students(models.Model):
	name= models.CharField(max_length=50)
	exam_grade= models.FloatField()
	GENDERS = (
	('male', 'Male')
		('female', 'Female'))
	gender = models.CharField(choices= GENDERS, max_length= 50, default='female')
	date_of_birth = models.DateField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

	def __str__(self):
		return self.name