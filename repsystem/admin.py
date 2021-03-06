from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from repsystem.models import Action, History, Level, Reputation


USER_MODEL = get_user_model()


class ReputationAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'level')


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'required_rep')


class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'message')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'creation_date')


class ReputationInline(admin.StackedInline):
    model = Reputation
    can_delete = False
    verbose_name_plural = 'reputation'


class ExtendedUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ReputationInline]
    list_display = UserAdmin.list_display + ('get_score', 'get_level', )

    def get_queryset(self, request):
        return super(ExtendedUserAdmin, self).get_queryset(request).select_related('reputation')

    def get_score(self, obj):
        return str(obj.reputation.score)
    get_score.short_description = 'Reputation'
    get_score.admin_order_field = 'reputation__score'

    def get_level(self, obj):
        return '{} ({})'.format(obj.reputation.level.id, obj.reputation.level.name)
    get_level.short_description = 'Level'
    get_level.admin_order_field = 'reputation__level'


admin.site.unregister(USER_MODEL)
admin.site.register(USER_MODEL, ExtendedUserAdmin)

admin.site.register(Reputation, ReputationAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(History, HistoryAdmin)
