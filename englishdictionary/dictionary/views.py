from multiprocessing import context
from django.shortcuts import render
from pydictionary import Dictionary


# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')  
    
    meaning = dict.meaning('search')
    synonyms = dict.synonyms('search')
    antonyms = dict.antonyms('search')
    context = {
        'meaning' : meaning['noun'][0],
        'synonyms' : synonyms,
        'antonyms' : antonyms
        }
    return render(request, 'word.html', context)