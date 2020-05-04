from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class State(models.Model):

    state_vals = (('CA', 'CA'),
                  ('WI', 'WI'),
                  ('NJ', 'NJ'),
                  ('TX', 'TX'),
                  ('LA', 'LA'),
                  ('FL', 'FL'),
                  ('AZ', 'AZ'),
                  ('MD', 'MD'),
                  ('ID', 'ID'),
                  ('MA', 'MA'),
                  ('UT', 'UT'),
                  ('NY', 'NY'),
                  ('MN', 'MN'),
                  ('WV', 'WV'),
                  ('AR', 'AR'),
                  ('IN', 'IN'),
                  ('IL', 'IL'),
                  ('GA', 'GA'),
                  ('OH', 'OH'),
                  ('NV', 'NV'),
                  ('NC', 'NC'),
                  ('MO', 'MO'),
                  ('KS', 'KS'),
                  ('VA', 'VA'),
                  ('WA', 'WA'),
                  ('TN', 'TN'),
                  ('CT', 'CT'),
                  ('CO', 'CO'),
                  ('SC', 'SC'),
                  ('RI', 'RI'),
                  ('NM', 'NM'),
                  ('IA', 'IA'),
                  ('PA', 'PA'),
                  ('MI', 'MI'),
                  ('NH', 'NH'),
                  ('ME', 'ME'),
                  ('KY', 'KY'),
                  ('DE', 'DE'),
                  ('MS', 'MS'),
                  ('WY', 'WY'),
                  ('AL', 'AL'),
                  ('VT', 'VT'),
                  ('OR', 'OR'),
                  ('OK', 'OK'),
                  ('MT', 'MT'),
                  ('HI', 'HI'),
                  ('DC', 'DC'),
                  ('NE', 'NE'),
                  ('ND', 'ND'))
    name = models.CharField(choices=sorted(state_vals),max_length=2)

    def __str__(self):
        return self.name

class City(models.Model):

    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class Loan(models.Model):

    # rural = 2
    # urban = 1
    # undefined = 0
    # new_bus = 1
    # exiting_bus = 2

    NewExist_vals = (
         ('New Business','New Business'),
         ('Existing Business','Existing Business'))
    UrbanRural_vals = (
         ('Undefined','Undefined'),
         ('Urban','Urban'),
         ('Rural','Rural'))
    BankState_vals = (('NC', 'NC'),
                           ('IL', 'IL'),
                           ('RI', 'RI'),
                           ('TX', 'TX'),
                           ('VA', 'VA'),
                           ('WI', 'WI'),
                           ('MA', 'MA'),
                           ('UT', 'UT'),
                           ('NY', 'NY'),
                           ('CA', 'CA'),
                           ('MN', 'MN'),
                           ('WV', 'WV'),
                           ('AR', 'AR'),
                           ('MD', 'MD'),
                           ('NV', 'NV'),
                           ('MO', 'MO'),
                           ('ND', 'ND'),
                           ('KS', 'KS'),
                           ('IN', 'IN'),
                           ('OH', 'OH'),
                           ('TN', 'TN'),
                           ('LA', 'LA'),
                           ('CT', 'CT'),
                           ('AL', 'AL'),
                           ('DE', 'DE'),
                           ('WA', 'WA'),
                           ('NE', 'NE'),
                           ('CO', 'CO'),
                           ('ID', 'ID'),
                           ('PA', 'PA'),
                           ('SD', 'SD'),
                           ('DC', 'DC'),
                           ('NH', 'NH'),
                           ('GA', 'GA'),
                           ('MS', 'MS'),
                           ('FL', 'FL'),
                           ('WY', 'WY'),
                           ('IA', 'IA'),
                           ('NJ', 'NJ'),
                           ('VT', 'VT'),
                           ('OR', 'OR'),
                           ('OK', 'OK'),
                           ('AZ', 'AZ'),
                           ('SC', 'SC'),
                           ('MI', 'MI'),
                           ('HI', 'HI'),
                           ('KY', 'KY'),
                           ('NM', 'NM'))

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    bank_state = models.CharField(choices=sorted(BankState_vals),max_length=2)
    term = models.PositiveIntegerField(validators=[MaxValueValidator(360)])
    number_emp = models.PositiveIntegerField(validators=[MaxValueValidator(360000)])
    new_exist = models.CharField(choices=sorted(NewExist_vals),max_length=60)
    urban_rural =  models.CharField(choices=sorted(UrbanRural_vals),max_length=60)
    disbursement_gross = models.IntegerField(validators=[MaxValueValidator(3600000)])
    prediction_prob = models.FloatField()

    def __str__(self):
        return self.id


class FedChargeOff(models.Model):
    DefaultRate = models.FloatField()
    Year = models.PositiveIntegerField(validators=[MaxValueValidator(2100)])
    Quarter = models.PositiveIntegerField(validators=[MaxValueValidator(4)])

    def __str__(self):
        return self.id
