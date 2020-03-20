from django.db import models

# Create your models here.
class Doctor(models.Model):
	drName = models.CharField(max_length=50)
	drmobNo = models.CharField(max_length=50)
	drEmail = models.CharField(max_length=50,primary_key=True,unique=True)
	drPassword = models.CharField(max_length=50)
	drLicense = models.CharField(max_length=50)
	drCity = models.CharField(max_length=50)
	drPincode = models.IntegerField()
	domain = models.CharField(max_length=20)
	
	def __str__(self):
		return self.drEmail

class Chemist(models.Model):
	cName = models.CharField(max_length=50)
	cmobNo = models.CharField(max_length=50)
	cEmail = models.CharField(max_length=50,primary_key=True,unique=True)
	cAddress = models.CharField(max_length=50)
	cCity = models.CharField(max_length=50)
	cPincode = models.CharField(max_length=50)
	cPassword = models.CharField(max_length=30)
	domain = models.CharField(max_length=20)
	
	def __str__(self):
		return self.cEmail
	

class LabChemist(models.Model):
	lName = models.CharField(max_length=50)
	lmobNo = models.CharField(max_length=50)
	lEmail = models.CharField(max_length=50,primary_key=True,unique=True)
	lLicense = models.CharField(max_length=50)
	lAddress = models.CharField(max_length=50)
	lCity = models.CharField(max_length=50)
	lPincode = models.CharField(max_length=30)
	lPassword = models.CharField(max_length=20)
	domain = models.CharField(max_length=20)
	
	def __str__(self):
		return self.lEmail
	