from django.db import models

# Create your models here.

class News(models.Model):
    heading1=models.CharField(max_length=255)
    info1=models.CharField(max_length=255)

    heading2=models.CharField(max_length=255)
    info2=models.CharField(max_length=255)

    heading3=models.CharField(max_length=255)
    info3=models.CharField(max_length=255)

    heading4=models.CharField(max_length=255)
    info4=models.CharField(max_length=255)

    heading5=models.CharField(max_length=255)
    info5=models.CharField(max_length=255)

    heading6=models.CharField(max_length=255)
    info6=models.CharField(max_length=255)


class Imag(models.Model):
    im1=models.ImageField(upload_to='images/') 
    heading1=models.CharField(max_length=255)
    info1=models.CharField(max_length=255)

    im2=models.ImageField(upload_to='images/') 
    heading2=models.CharField(max_length=255)
    info2=models.CharField(max_length=255)

    im3=models.ImageField(upload_to='images/') 
    heading3=models.CharField(max_length=255)
    info3=models.CharField(max_length=255)

    im4=models.ImageField(upload_to='images/') 
    heading4=models.CharField(max_length=255)
    info4=models.CharField(max_length=255)

    