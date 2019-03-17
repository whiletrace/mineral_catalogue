from django.shortcuts import render
from .models import Mineral
# Create your views here.


#
def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'trace_minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'trace_minerals/detail.html', {'mineral': mineral})
