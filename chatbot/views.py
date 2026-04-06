from django.shortcuts import render

def bot(request):
    return render(request, 'chatbot/bot.html')

