from django.shortcuts import render

def index(request):
    """Página Principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')