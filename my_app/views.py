from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    #POST em maiusculo refere-se a requisição http, o get não é o da requisição, mas sim um metodo python
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    posts = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in posts:
        post_title = post.find(class_= 'result-title hdrlnk').text
        post_url = post.find('a').get('href')

        if post.find(class_= 'result-price'):
            post_price = post.find(class_= 'result-price').text
        else:
            post_price = 'N/A'
        #### ADICIONAR COMO CHEGAR AS IMAGENS 
        if post.find(class_=)

        final_postings.append((post_title, post_url, post_price, post_image_url))



    models.Search.objects.create(search=search)

    context = {
        'search' : search,
        'final_postings': final_postings,
    }

    return render(request, 'my_app/new_search.html', context)

