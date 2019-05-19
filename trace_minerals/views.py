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
    minerals = Mineral.objects.all()
    return render(request, 'trace_minerals/index.html', {'minerals': minerals})


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
    char = request.GET.get('char')
    print(char)
    minerals = Mineral.objects.filter(name__istartswith=char)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals,
                                                         'char':char
                                                         })


def mineral_search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals})


def mineral_group(request):
    group = request.GET.get('group')
    minerals = Mineral.objects.filter(group__exact=group)

    return render(request, 'trace_minerals/index.html', {'minerals':minerals})
