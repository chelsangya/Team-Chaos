from kathmanduconnect.settings import BASE_DIR
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from metropolition.models import Reports,Poll,UserPoll
import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from django.conf import settings
from django.http import JsonResponse
import csv


def submit_report(request):
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')
        
        photo_file = request.FILES.get('photo')

        # Initialize photo with a default value
        photo = ''

        if photo_file:
            # Get the file name from the uploaded file
            photo = photo_file.name

            # Save the file to the "upload" folder inside the "static" directory
            file_path = f'static/upload/{photo}'
            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in photo_file.chunks():
                    destination.write(chunk)

        # Determine the category based on the submitted form
        category = 'pothole' if 'pothole' in request.POST else 'normal'

        # Get the currently logged-in user
        user = request.user

        # Create the Reports object and save it to the database
        report = Reports(name=name, photo=photo, category=category, latitude=latitude, longitude=longitude, UseruID=user)

        # Set the status based on prediction (only for pothole category)
        if category == 'pothole':
            # Load the CNN model and make a prediction
            loaded_model = load_model('pothole_classifier_model.h5')  # Replace with the actual path to your CNN model
            # test_image = image.load_img('D:/HACKATHON/Team-Chaos/models/pothole-dataset/try3.jpg', target_size=(64, 64))
            image_path = os.path.join(settings.BASE_DIR, file_path)
            test_image = image.load_img(image_path, target_size=(64, 64))
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



def feedback_survey(request):
    if request.method == 'POST':
        user_id = request.user.id  # Assuming you are using Django's authentication and user is logged in
        rating = request.POST.get('exampleForm')
        feedback = request.POST.get('feedback')

        # Check if the textarea data is valid using custom validation
        is_valid = custom_algorithm_validates(feedback)

        if is_valid:
            # Assuming you have a specific Poll for feedback
            poll = Poll.objects.get(title="Feedback request")

            # Save the data to the UserPoll table
            UserPoll.objects.create(UseruID_id=user_id, PollpID_id=poll.pID, answer=rating, description=feedback)

            return JsonResponse({'success': True})
        else:
            # Return a JSON response with error indicating validation failure
            return JsonResponse({'success': False, 'error': 'Validation failed'})

    # Fetch the specific Poll for feedback
    poll = Poll.objects.last()

    # Pass the poll object to the template for rendering
    return render(request, 'feedbackandsurvey.html', {'poll': poll})

def custom_algorithm_validates(text):
    path = os.path.join(BASE_DIR ,"HACKATHON/Team-Chaos/website/citizen/bad-words.csv")
    bad_words = load_hate_words(path)
    return detect_hate_words(text, bad_words)

def load_hate_words(file_path):
    hate_words = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for word in row:
                word = word.strip().lower()
                if word:
                    hate_words.add(word)
    return hate_words

def detect_hate_words(sentence, hate_words):
    preprocessed_sentence = sentence.lower().strip()
    tokens = preprocessed_sentence.split()

    for token in tokens:
        if token in hate_words:
            return True  # Hate word detected

    return False  # No hate word detected
