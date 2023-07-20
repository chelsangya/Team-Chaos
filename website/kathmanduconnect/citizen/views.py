import numpy as np
from keras.preprocessing import image
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reports

@login_required
def submit_report(request):
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name', '')
        photo = request.POST.get('photo', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')

        # Determine the category based on the submitted form
        category = 'pothole' if 'pothole' in request.POST else 'normal'

        # Get the currently logged-in user
        user = request.user

        # Create the Reports object and save it to the database
        report = Reports(name=name, photo=photo, category=category, latitude=latitude, longitude=longitude, UseruID=user)

        # Set the status based on prediction (only for pothole category)
        if category == 'pothole':
            # Load the CNN model and make a prediction
            loaded_model = load_model('path/to/your/model')  # Replace with the actual path to your CNN model
            test_image = image.load_img('D:/HACKATHON/Team-Chaos/models/pothole-dataset/try3.jpg', target_size=(64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            result = loaded_model.predict(test_image)

            # Get the class indices from the training set
            class_indices = {'normal': 0, 'pothole': 1}  # Replace with your class indices mapping

            # Map the predicted value to the class name
            prediction = 'pothole' if result[0][0] == class_indices['pothole'] else 'normal'

            # Set the status field accordingly
            report.status = 'Approved' if prediction == 'pothole' else 'Declined'
        else:
            report.status = 'Pending'  # Set status as "Pending" for other forms

        report.save()

        # Redirect to a success page or any other relevant page after saving the report
        return redirect('report_success')

    # If the request method is GET, simply render the form
    return render(request, 'report.html')

