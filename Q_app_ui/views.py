from django.shortcuts import render

def index(request):
    """ homepage """
    return render(request, 'Q_app_ui/index.html')
