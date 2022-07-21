from django.db import models
from datetime import datetime
from adminapp.models import*

from matplotlib.pyplot import title




class V_Fines(models.Model):
    id = models.AutoField(primary_key=True) 

    user = models.ForeignKey(Fines,max_length=100,null=True,on_delete=models.CASCADE) 
   
    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_lastname = models.CharField(verbose_name='User_Lastname', db_column="user_lastname", max_length=50, blank=False,
                                  null=False)  
    vechile_year = models.CharField(verbose_name='Vechile_Year', db_column="vechile_year", max_length=50, blank=False,
                                  null=False)
    vechile_make = models.CharField(verbose_name='Vechile_Make', db_column="vechile_make", max_length=50, blank=False,
                                  null=False)
    vechile_color = models.CharField(verbose_name='Vechile_Color', db_column="vechile_color", max_length=50, blank=False,
                                  null=False)
    vechile_number = models.CharField(verbose_name='vechile_number', db_column="vechile_number", max_length=50, blank=False,
                                  null=False)
    vechile_type= models.CharField(verbose_name='vechile_type', db_column="vechile_type", max_length=50, blank=False,
                                  null=True)
    causes= models.CharField(verbose_name='causes', db_column="causes", max_length=50, blank=False,
                                  null=True)
    vechile_image = models.FileField(verbose_name='Vechile_image', db_column="Vechile_image", upload_to='User/fins/', blank=True,)
    
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='V_Fines'