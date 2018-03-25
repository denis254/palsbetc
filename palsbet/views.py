from django.shortcuts import render

from django.views.generic import TemplateView

from . models import FreeTipsGames, SingleBetGames, VipTipsGames

from django.utils import timezone

def home(request):

    model = FreeTipsGames

    template_name = 'home_page.html'

    args = {}

    home_page_teams = FreeTipsGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:10]


    args ['home_page_teams'] = home_page_teams

    return render(request, 'home_page.html', args)

def androidapp(request):

    template_name = 'androidapp.html'

    return render(request, 'androidapp.html')


def jackpot(request):

    template_name = 'jackpot.html'

    return render(request, 'jackpot.html')

def rollover(request):

    template_name = 'rollover.html'

    return render(request, 'rollover.html')

def viptips(request):

    template_name = 'viptips.html'

    return render(request, 'viptips.html')

def singlebet(request):

    model = SingleBetGames

    template_name = 'singlebet.html'

    args = {}

    single_bet_teams = SingleBetGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:10]


    args ['single_bet_teams'] = grouped(single_bet_teams, 1)

    return render(request, 'singlebet.html', args)

def contactus(request):

    template_name = 'contactus.html'

    return render(request, 'palsbet/contactus.html')

def guide(request):

    template_name = 'guide.html'

    return render(request, 'guide.html')

def backToHomePage(request):

    template_name = 'backtohomepage.html'

    return render(request, 'palsbet/backtohomepage.html')

def viewolderesults(request):

    template_name = 'older_results.html'

    args = {}

    older_results_teams = FreeTipsGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[10:60]


    args ['older_results_teams'] = grouped(older_results_teams, 10)

    return render(request, 'older_results.html', args)

def howmanyodds(request):

    template_name = 'howmanyodds.html'

    return render(request, 'howmanyodds.html')

def modeofsending(request):

    template_name = 'modeofsending.html'

    return render(request, 'modeofsending.html')

def timeofsending(request):

    template_name = 'timeofsending.html'

    return render(request, 'timeofsending.html')


def homevip(request):

    model = VipTipsGames

    template_name = 'home_vip.html'

    args = {}

    vip_tips = VipTipsGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:7]


    args ['vip_tips'] = vip_tips

    return render(request, 'home_vip.html', args)

def payment(request):

    template_name = 'payment.html'

    return render(request, 'payment.html')

def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
