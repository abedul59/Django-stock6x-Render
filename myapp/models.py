from django.db import models

# Create your models here.
class Stock6Sign202404(models.Model):  
    cStockID = models.CharField(max_length=5, default='')
    cStockName = models.CharField(max_length=5, default='')
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10, default='')
    cSign2 = models.CharField(max_length=10, default='')
    cSign3 = models.CharField(max_length=10, default='')
    cSign4 = models.CharField(max_length=10, default='')
    cSign5 = models.CharField(max_length=10, default='')
    cSign6 = models.CharField(max_length=10, default='')
    cAverageScore = models.CharField(max_length=15, default='')  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15, default='')  #不能改成FloatField，會發生錯誤

    sCore2403= models.CharField(max_length=10, default='')
    sCore2402= models.CharField(max_length=10, default='')
    sCore2401= models.CharField(max_length=10, default='')
    sCore2312= models.CharField(max_length=10, default='')
    sCore2311= models.CharField(max_length=10, default='')
    sCore2310= models.CharField(max_length=10, default='')
    sCore2309= models.CharField(max_length=10, default='')
    sCore2308= models.CharField(max_length=10, default='')
    sCore2307= models.CharField(max_length=10, default='')
    sCore2306= models.CharField(max_length=10, default='')
    sCore2305= models.CharField(max_length=10, default='')
    sCore2304= models.CharField(max_length=10, default='')







    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID