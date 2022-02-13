from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'add.html')


def inner(request):
    return render(request, 'inner.html')