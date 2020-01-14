from django.http import HttpResponse


def index(request):
    response = "welcome to eagoalyg's website"
    return HttpResponse(response)


def program(request):
    response = "You are looking at program"
    return HttpResponse(response)


def diary(request):
    response = "You are looking at diary"
    return HttpResponse(response)
