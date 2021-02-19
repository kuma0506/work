from django.db import models


class Country(models.Model):
    """国名"""
    CountryName_Ja = models.CharField('国名（日本語）', max_length=255)
    CountryName_En = models.CharField('国名（英語）', max_length=255)

    def __str__(self):
        return self.CountryName_Ja


class CountryAcs(models.Model):
    """国名"""
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __int__(self):
        return self.Country


