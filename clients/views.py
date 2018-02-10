from django.http import HttpResponse
from django.shortcuts import render


def do_calculation(value1, value2):
    return value1 * value2


def test_function(request):
    tot = do_calculation(10, 2)
    p_fla = False
    people = ['Gregory', 'Mary', 'Jose', 'Pedro', 'John']
    return render(request, 'example.html', {'total': tot, 'people': people, 'p_fla': p_fla})


def list_clients(request):
    return HttpResponse('Hello world')


def special_case_2003(request):
    return HttpResponse('Returning the cases for 2003')


def special_case(request, year):
    return HttpResponse('::Returning articles from %s ' % year)


def month_archive(request, year, month):
    return HttpResponse('::Returning articles from year %s and month %s' % (year, month))


def hello(request, name):
    return HttpResponse('Hello world %s' % name)
