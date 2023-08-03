from django.shortcuts import render
from django.http import Http404,HttpResponse

# Create your views here.

def starting_page(request):
    try:
      return render(request,'blog/index.html')
    except:
        raise Http404()
    
def posts(request):
    pass

def post_detial(request):
    
    pass