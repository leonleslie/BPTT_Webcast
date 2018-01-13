from django.shortcuts import render
from .models import bpquestions
from .forms import questionform
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

def question(request):
	askquestions = bpquestions.objects.all()
	questform = questionform(request.POST or None)

	if questform.is_valid():
		instance = questform.save(commit=False)
		instance.save()
		# return HttpResponse("<br><br><center><h1>Note Entered</h1></center>")
		messages.success(request,"Successfully Created")
		return redirect("index")


	context = {
		"askquestions":askquestions,
		"questform":questform,

	}

	return render(request,"index.html", context)

