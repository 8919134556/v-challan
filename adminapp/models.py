from django.db import models
from datetime import datetime

from matplotlib.pyplot import title




class Vechile_Register(models.Model):
    id = models.AutoField(primary_key=True)

    gender = models.CharField(verbose_name='Gender', db_column="gender", max_length=50, blank=False,
                                  null=False)
    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_lastname = models.CharField(verbose_name='User_Lastname', db_column="user_lastname", max_length=50, blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    
    user_phone = models.BigIntegerField(verbose_name='User_Phone', db_column="user_phone", blank=False,
                                  null=False)
    vechile_year = models.CharField(verbose_name='Vechile_Year', db_column="vechile_year", max_length=50, blank=False,
                                  null=False)
    vechile_make = models.CharField(verbose_name='Vechile_Make', db_column="vechile_make", max_length=50, blank=False,
                                  null=False)
    vechile_model = models.CharField(verbose_name='vechile_model', db_column="vechile_model", max_length=50, blank=False,
                                  null=False)
    vechile_color = models.CharField(verbose_name='Vechile_Color', db_column="vechile_color", max_length=50, blank=False,
                                  null=False)
    
    vechile_mileage = models.CharField(verbose_name='Vechile_Mileage', db_column="vechile_mileage", max_length=50, blank=False,
                                  null=False)
    vechile_number = models.CharField(verbose_name='vechile_number', db_column="vechile_number", max_length=50, blank=False,
                                  null=False)
    vechile_type= models.CharField(verbose_name='vechile_type', db_column="vechile_type", max_length=50, blank=False,
                                  null=True)

    country= models.CharField(verbose_name='Country', db_column="country", max_length=50, blank=False,
                                  null=True)
    state= models.CharField(verbose_name='State', db_column="state", max_length=50, blank=False,
                                  null=True)
    city= models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,
                                  null=True)
    
    street_name= models.CharField(verbose_name='Street_Name', db_column="street_name", max_length=50, blank=False,
                                  null=False)
    house_number= models.CharField(verbose_name='House_Number', db_column="house_number", max_length=50, blank=False,
                                  null=False)
        
 
    user_image = models.FileField(verbose_name='User_Image', db_column="user_image", upload_to='User/Profile-image/', blank=True,)

    vechile_image = models.FileField(verbose_name='Vechile_image', db_column="Vechile_image", upload_to='User/Vechile-image/', blank=True,)

   
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Vechile_Register'
    

class Fines(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(verbose_name='Title', db_column="title", max_length=50, blank=False,
                                  null=True)
    prison= models.CharField(verbose_name='prison', db_column="prison", max_length=50, blank=False,
                                  null=True)
    descrption= models.CharField(verbose_name='Descrption', db_column="descrption", max_length=50, blank=False,
                                  null=True)
    amount= models.CharField(verbose_name='amount', db_column="amount", max_length=50, blank=False,
                                  null=True)
    image = models.FileField(verbose_name='Image', db_column="image", upload_to='admin/fine-image/', blank=True,)

    datetime_created = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='Fines'