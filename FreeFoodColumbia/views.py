from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def index(request):
  name = 'FreefoodColumbia111'
  t = get_template('trash.tmpl')
  html = t.render(Context({'name':name}))
  return HttpResponse(html)

def hello(request):
  return HttpResponse("Hello World")

def allFood(request):
	name = 'Test Name'
	s = get_template('listing.tmpl')
	html = s.render(Context(('name':name)))
	return HttpResponse(html)
