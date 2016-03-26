from django.db.models import F

from .models import Action, Reputation


def perform_action(user, action_name):
    action = Action.objects.get(name=action_name)
    reputation = Reputation.objects.get(user=user)
    reputation.score = F('score') + action.value
    reputation.save()
