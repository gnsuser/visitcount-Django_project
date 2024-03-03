from django.shortcuts import render
from .models import Visit

# Create your views here.
def home(request):
    visit = Visit.objects.first()
    if not visit:
        visit = Visit.objects.create(count=0)
    visit.count += 1
    visit.save()
    return render(request, 'home.html', {'count': visit.count})