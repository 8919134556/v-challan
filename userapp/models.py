from django.db import models
from datetime import datetime


class Payments(models.Model):
    id = models.AutoField(primary_key=True)

    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)

    vechile_make = models.CharField(verbose_name='Vechile_Make', db_column="vechile_make", max_length=50, blank=False,
                                  null=False)
    
    causes= models.CharField(verbose_name='causes', db_column="causes", max_length=50, blank=False,
                                  null=True)
    
    amount= models.CharField(verbose_name='amount', db_column="amount", max_length=50, blank=False,
                                  null=True)
    
    vechile_color = models.CharField(verbose_name='Vechile_Color', db_column="vechile_color", max_length=50, blank=False,
                                  null=False)
    
    vechile_number = models.CharField(verbose_name='vechile_number', db_column="vechile_number", max_length=50, blank=False,
                                  null=False)
    
    order_id = models.CharField(verbose_name='order_id', db_column="order_id", max_length=50, blank=False,
                                  null=True)
    
    status = models.CharField(verbose_name='status', db_column="status", max_length=50, blank=False,
                                  null=True)
    
    tex_id = models.BigIntegerField(verbose_name='tex_id', db_column="tex_id", blank=False,
                                  null=True)
    
    payment_mode = models.CharField(verbose_name='payment_mode', db_column="payment_mode", max_length=50, blank=False,
                                  null=True)
    
    bank_tex_id = models.CharField(verbose_name='bank_tex_id', db_column="bank_tex_id", max_length=50, blank=False,
                                  null=True)
    
    bank_name = models.CharField(verbose_name='bank_name', db_column="bank_name", max_length=50, blank=False,
                                  null=True)
    
    datetime_created = models.DateTimeField(default=datetime.now)


    class Meta:
        db_table='Payments'
    

class Complient(models.Model):
    id = models.AutoField(primary_key=True)

    tic_id = models.CharField(verbose_name='Tic_id', db_column="tic_id", max_length=50, blank=False,
                                  null=False)

    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)

    vechile_num = models.CharField(verbose_name='Vechile_Num', db_column="vechile_num", max_length=50, blank=False,
                                  null=False)
    
    causes= models.CharField(verbose_name='causes', db_column="causes", max_length=50, blank=False,
                                  null=True)
    
    amount= models.CharField(verbose_name='amount', db_column="amount", max_length=50, blank=False,
                                  null=True)
    
    complient= models.CharField(verbose_name='Complient', db_column="complient", max_length=50, blank=False,
                                  null=True)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    

    datetime_created = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='Complient'