from django.shortcuts import render
from .models import Notices
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin(request):
    return render(request, 'admin-dashboard.html')


def newnotice(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('desc', '')
        no_volunteer = request.POST.get('volunteer','')
        date = request.POST.get('date', '')
        notices = Notices(title = name,description=description,date = date,volunteer = no_volunteer)
        notices.save()
        
        return render(request,'noticeform.html')
    return render(request,'noticeform.html')