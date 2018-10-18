from django.contrib import admin

from . models import FreeTipsGames,SingleBetGames,VipTips, PunterPick, RollOver

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

@admin.register(SingleBetGames)
class SingleBetGamesAdmin(ImportExportModelAdmin):
    pass

@admin.register(FreeTipsGames)
class FreeTipsGamesAdmin(ImportExportModelAdmin):
    pass

@admin.register(VipTips)
class VipTipsAdmin(ImportExportModelAdmin):
    pass

@admin.register(PunterPick)
class PunterPickAdmin(ImportExportModelAdmin):
    pass

@admin.register(RollOver)
class RollOverAdmin(ImportExportModelAdmin):
    pass


