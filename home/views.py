from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home/wellcome.html',{'today': datetime.today()})


@login_required(login_url='/admin')# this section blocks the access of the page if the use is not login
def authorized(request):
    return render(request, 'home/authorized.html',{})
#@login_required # this section blocks the access of the page if the use is not login
def thankyou(request):
    return render(request, 'home/thankyou.html',{})