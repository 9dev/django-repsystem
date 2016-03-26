from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    required_rep = models.IntegerField(unique=True)

    def __str__(self):
        return '{} ({})'.format(self.id, self.name)


class Reputation(models.Model):
    score = models.PositiveIntegerField(default=0)
    level = models.ForeignKey(Level, default=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.score)


class Action(models.Model):
    name = models.CharField(max_length=100, unique=True)
    message = models.CharField(max_length=1000)
    value = models.IntegerField()


@receiver(post_save, sender=Reputation)
def post_save_reputation(sender, instance, created, **kwargs):
    if not created:
        reputation = Reputation.objects.get(pk=instance.pk)
        levels = Level.objects.filter(required_rep__lte=reputation.score)

        if levels.count() > 0:
            new_level = levels.order_by('-required_rep')[0]
            if instance.level != new_level:
                Reputation.objects.filter(pk=instance.pk).update(level=new_level)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        Reputation.objects.create(user=instance)
