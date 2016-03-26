from django.db.models import F

from .models import Action, History, Reputation


def perform_action(user, action_name):
    action = Action.objects.get(name=action_name)
    History.objects.create(user=user, action=action)

    reputation = Reputation.objects.get(user=user)
    reputation.score = F('score') + action.value
    reputation.save()


def get_user_history(user):
    return History.objects.filter(user=user).order_by('creation_date').select_related('action')
