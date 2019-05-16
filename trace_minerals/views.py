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
    minerals = Mineral.objects.filter(name__istartswith=request.GET.get("char"))
    return render(request, 'trace_minerals/index.html', {'minerals':minerals})





#Todo filter_by_letter
# get value of asic lowercase alphabet to pass to view
# pass the asic to template as context
# write to query to search db
# query return list of  minerals with first letter of char chosen by user
# default is letter a
# query takes no longer than 10ms

#Todo text_search
# get value of input of search form
# list of results of mineral names that contain text from search input
# query takes no longer than 10 ms

#Todo filter by group
# silicates, Oxides, Sulfates, Sulfides, Carbonates, Carbonates, Halides
# hardcode list in layout template
# query db based upon mineral attr group
# SulfoSalt, Phosphates, Borates, Organic Minerals,
# Arsenates, Native Elements, Other
# return list of minerals that have that group attr
# query takes no longer than 10 ms
# return list view
