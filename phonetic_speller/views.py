from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def translate(request):
    original_text = request.GET['userInput']
    new_text = process_text(original_text)
    return render(request, 'translate.html', {'original': original_text, 'translation': new_text})


def about(request):
    return render(request, 'about.html')


# handles the translation to populate 'translate.html'
def process_text(text):    
    alpha = {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-Ray', 'y': 'Yankee', 'z': 'Zulu'}
    traslation = ""
    for i in text:
        try:
            traslation += alpha[i] + " "
        except:
            traslation += i + " "
    return traslation
