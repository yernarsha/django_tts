from django.shortcuts import render

from gTTS.templatetags.gTTS import say

# Create your views here.

def text_to_speech(request):
    if request.method == "POST":
        text_speech = request.POST['speech']
        obj = say(language='en-us', text=text_speech)
                  
        return render(request, 'tts_app/index.html', {'obj': obj, 'text_speech': text_speech})
    
    return render(request, 'tts_app/index.html')
    
    
    
    