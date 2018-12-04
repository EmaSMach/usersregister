# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .validators import validate_first_name, validate_last_name, validate_email


class Address(models.Model):
    """
    A class representing an address.
    """
    address = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.address.encode('utf-8')

    class Meta:
        verbose_name_plural = 'Addresses'


class Users(models.Model):
    """
    User data model representation.
    """
    first_name = models.CharField(max_length=100, validators=[validate_first_name])
    last_name = models.CharField(max_length=100, validators=[validate_last_name])
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=False, validators=[validate_email])
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    #address = models.TextField(max_length=100, null=True, blank=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(null=False, blank=False)
    timezone = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'Users'


class Gender(models.Model):
    """
    A class representing a gender.
    """
    MALE = 'M'
    FEMALE = 'F'

    GENDER_OPTIONS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_OPTIONS,
        default=MALE,
        null=True,
        blank=True,
    )


class Medias(models.Model):
    """
    Social media model.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Medias'
