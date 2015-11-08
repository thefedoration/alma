from __future__ import absolute_import

from django.shortcuts import render, redirect



# main landing page
def home(request):
	return render(request, 'home2.html')