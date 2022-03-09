from django.shortcuts import render
from .forms import FormPost

def donation_view(request):
    template = "donate-item-page.html"
    context = {"is_reuse": True}
    return render(request, template, context=context)

def showform(request):
    form= FormPost(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'adpostui.html', context)

