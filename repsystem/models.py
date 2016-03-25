from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    required_rep = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.id)


class Reputation(models.Model):
    score = models.PositiveIntegerField(default=0)
    level = models.ForeignKey(Level, default=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.score)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_delete_ban(sender, instance, created, **kwargs):
    if created:
        Reputation.objects.create(user=instance)
