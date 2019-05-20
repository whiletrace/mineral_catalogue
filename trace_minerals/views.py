from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Mineral


# Create your views here.


#
def mineral_list(request):
    """
    view takes takes care of logic and outputs to template index.html

    takes request object as argument queries the database for all minerals
    passes the value of parameter too index as context
    :rtype: django.http.response.HttpResponse
    """

    return HttpResponseRedirect('/glossary/?char=A')


def mineral_detail(request, pk):
    """
    view takes takes care of logic and outputs to template detail.html

    takes request object as argument queries the database for obj mineral
    with pk that is passed through URL
    passes the value of parameter too detail as context
    :rtype: django.http.response.HttpResponse
    """
    mineral = Mineral.objects.get(pk=pk)

    return render(request, 'trace_minerals/detail.html', {'mineral': mineral})


def mineral_glossary(request):
    """
    view takes takes care of glossary query logic and outputs to template
    index.html

    takes request object as argument queries the database for
    char user chose in glossary filter
    passes the value of parameter too index as context
    :rtype: django.http.response.HttpResponse
    """
    char = request.GET.get('char')
    minerals = Mineral.objects.filter(name__istartswith=char)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals,
                                                         'char':char
                                                         })


def mineral_search(request):
    """
    view takes takes care of text search query logic and outputs to template
    index.html

    takes request object as argument queries the database for
    var term
    passes the value of parameter too index as context
    :rtype: django.http.response.HttpResponse
    """
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals})


def mineral_group(request):
    """
    view takes takes care of mineral group query logic and outputs to
    template index.html

    takes request object as argument queries the database for
    var group
    passes the value of parameter too index as context
    :rtype: django.http.response.HttpResponse
    """
    group = request.GET.get('group')
    minerals = Mineral.objects.filter(group__exact=group)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals,
                                                         'group':group
                                                         })
