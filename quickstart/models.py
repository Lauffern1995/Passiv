from django.db import models


class Company(models.Model):
    name = models.CharField('Company Name', max_length=155)

    def __str__(self):
        return self.name
    
class Salesperson(models.Model): 
    name = models.CharField('Salesperson Name', max_length=155)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
        
class Sale(models.Model): 
    amount = models.IntegerField(blank=True, null=True)
    salesperson = models.ForeignKey(Salesperson, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
         return '$'+str(self.amount) + ' SOLD BY ' + self.salesperson.name
