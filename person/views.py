from django.shortcuts import render

def person_index(request):
    return render(request, 'person_index.html')