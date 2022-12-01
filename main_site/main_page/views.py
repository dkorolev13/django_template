from django.http import HttpResponse

from django.shortcuts import render
from . import models

import datetime


def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    if request.method == 'POST':
        print(request.POST.get('my_text'))

        text = models.My_text.objects.create(

            my_text=request.POST.get('my_text'))
        text.save()

    text = models.My_text.objects.all()
    context = {'texts': text}
    return render(request, 'main_page/index.html', context)
