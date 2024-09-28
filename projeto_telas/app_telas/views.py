from django.shortcuts import render

# Página inicial
def index(request):
    return render(request, 'index.html')

# Página de ajustes
def ajustes(request):
    return render(request, 'ajustes.html')

# Página de suporte
def suporte(request):
    return render(request, 'suporte.html')

# Página de como_usar
def como_usar(request):
    return render(request, 'como_usar.html')

