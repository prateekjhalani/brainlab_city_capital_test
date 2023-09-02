from django.db import models


class BaseModel(models.Model):
    """
    Base model which can inherit in every model
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    iso2 = models.CharField(max_length=16)
    iso3 = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'
        verbose_name = 'country'
        verbose_name_plural = 'countries'
