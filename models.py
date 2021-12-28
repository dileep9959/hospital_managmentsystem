from django.db import models


# Create your models here.
class docter(models.Model):
    name=models.CharField('name',max_length=50)
    mobile=models.CharField('mobile',max_length=13)
    special=models.CharField('special',max_length=50)

    def __str__ (Self):
        return Self.name,Self.mobile



class patient(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=13)  
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

    
    def __str__ (Self):
        return Self.name

class appointment(models.Model):
    docter=models.ForeignKey(docter,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()

    # def __str__ (self):
    #     return str(self.docter,self.patient)
