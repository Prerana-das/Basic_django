from django.http import HttpResponse

# Create your views here.

def test_index_func(request):  #request browse korle url a rqst patay like as get req
    html = "<h1>Only For Test</h1>"
    return HttpResponse(html)

def test_index_func2(request):
    html = "<h1>This is another view</h1>"
    return HttpResponse(html)