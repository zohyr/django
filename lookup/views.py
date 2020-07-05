# this is views.py file

from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode'] # zipcode = value-input_name
        # return render(request, 'home.html', {'zipcode': zipcode})
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        if api[0]['Category']['Name'] == "Good":
            category_description = '(0-50) Air quality is considered satisfactory.'
            category_color = 'good'

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = '(51-100) Air quality is acceptable.'
            category_color = 'moderate'

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color
            })

    
    else:

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        if api[0]['Category']['Name'] == "Good":
            category_description = '(0-50) Air quality is considered satisfactory.'
            category_color = 'good'

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = '(51-100) Air quality is acceptable.'
            category_color = 'moderate'

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color
            })

def about(request):
    return render(request, 'about.html', {})
