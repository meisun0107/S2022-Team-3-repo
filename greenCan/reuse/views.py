from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'reuse_index.html'
    return render(request, template, context={})