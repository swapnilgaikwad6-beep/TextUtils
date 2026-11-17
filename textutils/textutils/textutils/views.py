# I have created this file - swapnil
from pydoc import text

from django.http import HttpResponse
from django.shortcuts import render


#code for video 7 :
def  index(request):
    return render(request, 'index2.html')


def analyse(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    wordcounter = request.POST.get('wordcounter', 'off')

    print(djtext)
    print(removepunc)

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = { 'purpose': 'Removed punctuations' , 'analysed_text': analysed}
        return render(request, 'analyse2.html', params)

    elif fullcaps == 'on':
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Capitalized the Text', 'analysed_text': analysed}
        return render(request, 'analyse2.html', params)

    elif newlineremover == 'on':
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {'purpose': 'Removed new lines', 'analysed_text': analysed}
        return render(request, 'analyse2.html', params)

    elif spaceremover == 'on':
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == "\n":
                pass

            else:
                analysed = analysed + char

        params = {'purpose': 'Removed Spaces', 'analysed_text': analysed}
        return render(request, 'analyse2.html', params)

    elif charcounter == 'on':
        count = 0
        for char in djtext:
            count = count + 1
        characters_count = 'The number of charecters in this sentence is'
        params = {
            'purpose': 'Character Counter',
            'analysed_text': djtext,
            'character_count': count,
            'characters_count': characters_count
        }
        return render(request, 'analyse2.html', params)
    elif wordcounter == 'on':
        words = djtext.split()
        count = 0

        for word in words:
            count = count + 1
        words = 'so the total number of words in this sentence is '
        params = {
            'purpose': 'Word Counter',
            'analysed_text': djtext,
            'words' : words,
            'word_count': count
        }
        return render(request, 'analyse2.html', params)

    else:
        return HttpResponse('Error')
