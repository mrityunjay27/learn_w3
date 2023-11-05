from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):  #  that will deal with incoming requests to the members/details/? url
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):  # Deals with root "/"
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('test_template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

def listMembers(request):
  mydata = Member.objects.all()
  mydata_1 = Member.objects.all().values()  # changes queryset to python dict (key-value pair)
  mydata_2 = Member.objects.values_list('firstname')  # returns only firtname column
  mydata_3 = Member.objects.filter(firstname='Tobias').values()  #returns the row with given filter
  template = loader.get_template('table_members.html')
  context = {
    'mymembers': mydata,
    'mymembers1' : mydata_1,
    'mymembers2' : mydata_2,
    'mymembers3' : mydata_3,
  }
  return HttpResponse(template.render(context, request))