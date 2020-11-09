from django.shortcuts import render, get_object_or_404

from .models import New


def new_list(request):
    news = New.published.all()
    return render(request, 'soc/new/list.html', {'news': news})


def new_body(request, year, month, day, new):
    new = get_object_or_404(New, new_slug=new, status='publish', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'soc/new/body.html', {'new': new})