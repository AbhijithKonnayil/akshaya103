from django.db import models

class accountsin(models.Model):
	#date=models.DateField()
	#time=models.DateTimeField()
	reciept=models.CharField(max_length=100)
	#bank_acc=models.CharField(max_length=50)
	#payment_fees=models.FloatField()
	service_fees=models.FloatField()
	#customer_name=models.CharField(max_length=50)
	#username=models.CharField(max_length=50)
	#password=models.CharField(max_length=50)
	#contact_no=models.CharField(max_length=10)
	#total_fees=models.FloatField()
	#remark=models.CharField(max_length=200)
	#staff=models.CharField(max_length=50)
	def __str__(self):
		return self.reciept +  ' ' + str(self.service_fees)

 