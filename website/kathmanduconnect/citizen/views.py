# import numpy as np
# from keras.preprocessing import image
from django.shortcuts import render, redirect, HttpResponse
from citizen.models import Safety
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from metropolition.models import Reports
from django.contrib.auth.models import User
from potholedetector import image_detect

def submit_report(request):
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')
        
        photo_file = request.FILES.get('photo')

        if photo_file:
            # Get the file name from the uploaded file
            photo = photo_file.name

            # Save the file to the "upload" folder inside the "static" directory
            file_path = f'static/upload/{photo_filename}'
            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in photo_file.chunks():
                    destination.write(chunk)

        # Determine the category based on the submitted form
        category = 'pothole' if 'pothole' in request.POST else 'normal'

      
        
            # Get the currently logged-in user
        user = request.user

        # Create the Reports object and set initial value to None
        report = None

        if category == 'pothole':
            prediction = image_detect(f "D:\HACKATHON\Team-Chaos\website\kathmanduconnect\static\upload\{photo}" )

            # Set the status field accordingly
            report.status = 'Approved' if prediction == 'pothole' else 'Declined'
        else:
            report.status = 'Pending'  # Set status as "Pending" for other forms

        report.save()

        # Redirect to a success page or any other relevant page after saving the report
        return redirect('report_success')

    # If the request method is GET, simply render the form
    return render(request, 'report.html')
   
            
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email == "admin@admin.com" and password == "admin":
            return redirect('/admin/dashboard/')
        else:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user) 
                return redirect('/dashboard/')
            else:
                error_message = "Invalid email or password. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        photo = request.FILES.get('photo')
        username = name
        CustomUser = get_user_model()
        new_user = CustomUser.objects.create_user(username=username, email=email, password=password)
        new_user.phone = phone
        new_user.photo = photo
        new_user.save()

        return redirect('/')
    return render(request, 'signup.html')

def safety(request):
    if request.method == 'POST':
        issueType = request.POST.get("issueType")
        description = request.POST.get("description")
        query = Safety(issueType = issueType, description = description)
        try:
            query.save()
            message = "Received your message!! We will be there for your aid ASAP."
            messages.success(request, message)
            return redirect('/dashboard')
        except Exception as e:
            message = "Couldn't process your request!! Please try again later."
            messages.error(request, message)
            print(e)
    return render(request, 'safetyandsecurity.html')


def dashboard(request):
    return render(request, 'index.html')