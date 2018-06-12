from django.contrib import admin

from . models import FreeTipsGames,SingleBetGames,VipTips, PunterPick, RollOver, Notification

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(FreeTipsGames)

admin.site.register(SingleBetGames)

admin.site.register(VipTips)

admin.site.register(PunterPick)

admin.site.register(RollOver)

admin.site.register(Notification)
