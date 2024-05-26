from django.db import models

# Create your models here.


class user(models.Model):
    user_type = models.CharField(max_length=20)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "user"


class term_insurance(models.Model):
    insuor = models.CharField(max_length=50)
    life_cover = models.PositiveIntegerField()
    cover_till_age = models.PositiveIntegerField()
    claim_settelment = models.FloatField()
    pay_monthly = models.PositiveIntegerField()

    class Meta:
        db_table = "term_insurance"

    # def __str__(self):
    #    return f'Policy name: {self.insuor}'


class health_insurance(models.Model):
    policy_name = models.CharField(max_length=50)
    cover_amount = models.PositiveIntegerField()
    policy_period = models.PositiveIntegerField()
    pay_monthly = models.PositiveIntegerField()

    class Meta:
        db_table = "health_insurance"
    
