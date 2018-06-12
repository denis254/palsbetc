from django.contrib import admin

from . models import FreeTipsGames,SingleBetGames,VipTips, PunterPick, RollOver, Notification

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(FreeTipsGames)

admin.site.register(SingleBetGames)

admin.site.register(VipTips)

admin.site.register(PunterPick)

admin.site.register(RollOver)

admin.site.register(Notification)
