from django.shortcuts import render

# Create your views here.

import requests
API_KEY = 'pub_d41914aa0b9945e9a0dc783056f7f659'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsdata.io/api/1/latest?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    elif category:
        url = f'https://newsdata.io/api/1/latest?country=us&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    else:
    	url = f'https://newsdata.io/api/1/latest?country=us&apiKey={API_KEY}'
    	response = requests.get(url)
    	data = response.json()
    	articles = data['results']

   


    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
