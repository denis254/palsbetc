from django.urls import path, include

from . views import payment, homevip, timeofsending, modeofsending, home, viewolderesults, singlebet, androidapp, jackpot, rollover, viptips, guide, howmanyodds

urlpatterns = [

    path('', home),

    path('home/', home),

    path('viewolderesults/', viewolderesults),

    path('singlebet/', singlebet),

    path('androidapp/', androidapp),

    path('jackpot/', jackpot),

    path('rollover/', rollover),

    path('viptips/', viptips),

    path('guide/', guide),

    path('howmanyodds/', howmanyodds),

    path('modeofsending/', modeofsending),

    path('timeofsending/', timeofsending),

    path('accounts/', include('django.contrib.auth.urls')),

    path('home_vip/', homevip),

    path('payment/', payment),
]
