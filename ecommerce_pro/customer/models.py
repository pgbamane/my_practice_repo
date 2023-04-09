from django.db import models
from django.db.models.signals import post_save, Signal
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)


class Profile(models.Model):
    birth_date = models.DateField()
    education = models.CharField(max_length=120)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    address = models.ManyToManyField(Address)


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print("------------- Model save() method called -------------")
        super().save()


@receiver(post_save, sender=Customer)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("----------- Create Profile object ---------")
        user = User(username=instance.name + "#121", first_name=instance.name, email="prisha@gmail.com")
        user.save()
        profile = Profile(birth_date="1995-07-23", education="B.tech",
                          user=user)
        profile.save()
        print("----------- End of Signal -----------")
