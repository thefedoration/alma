from __future__ import absolute_import

from django.shortcuts import render, redirect

from alma.models import Lead

from alma.forms import LeadForm


# main landing page
def home(request):

	anchor = None
	if request.method == "POST":

		# if post request. validate form and create new lead object
		form = LeadForm(request.POST)
		if form.is_valid():

			# commit=False means the form doesn't save at this time.
			# commit defaults to True which means it normally saves.
			model_instance = form.save(commit=True)
			model_instance.save()
			return redirect('/thanks/')
		else:
			anchor = 'contact'

	else:
		form = LeadForm()

	return render(request, 'home.html', {'form': form, 'anchor': anchor})


def thanks(request):	
	return render(request, "thanks.html", {})