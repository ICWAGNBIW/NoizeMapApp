from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Coordinates, Measurement, Estimation, CorFrom, CorChark
from .forms import MeasurmentForm, NoiseSourcesForm
import folium
from django.views.generic.base import View
from operator import itemgetter
# Create your views here.

def Map(request):
    place_list = Coordinates.objects.order_by('id')
    measures = Measurement.objects.all()
    print(measures)

    submitbutton= request.POST.get("submit")
    
    source=''
    
    form= NoiseSourcesForm(request.POST or None)
    if form.is_valid():
        source= form.cleaned_data.get("source")

    context = {
    'form' : form,
    'submitbutton': submitbutton,
    'source' : source,
    'place_list' : place_list,
    'measures': measures,
    }
    return render(request, 'main.html', context=context)

def getColor(noize):
    if noize <= 40:
        return 'green'
    elif noize >40 and noize <=50:
        return 'orange'
    elif noize >50 and noize <=60:
        return 'blue'
    else:
        return 'red'
    
def Form(request):
    form = MeasurmentForm()
    place_list = Coordinates.objects.order_by('id')
    measures = Measurement.objects.all()
    context = {
        'form' : form,
        'place_list' : place_list,
        'measures': measures,
    }
    return render(request, 'form.html',context=context)

def SubmitForm(request):
    form = MeasurmentForm(request.POST)
    if form.is_valid():
        measurement = form.save(commit=False)
        measurement.Person = request.user
        measurement.save()

    return HttpResponseRedirect('/../../')

def Index(request):
    place_list = Coordinates.objects.order_by('id')
    measures = Measurement.objects.filter(Person=request.user)
    context = {
        'place_list': place_list,
        'measures': measures,
    }
    return render(request, "MyMeasures.html", context=context)

def Edit(request, id):
    measures = Measurement.objects.filter(Person=request.user)
    try:
        measure = Measurement.objects.get(id=id)
        place_list = Coordinates.objects.order_by('id')

        context = {
            "measure": measure,
            "place_list": place_list
        }

        if request.method == "POST":
            measure.Nlevel = request.POST.get("Nlevel")
            measure.MNlevel = request.POST.get("MNlevel")
            measure.Person = request.user
            measure.save()
            return HttpResponseRedirect('/MyMeasures/')
        else:
            return render(request, "Edit.html", context=context)
    except Measurement.DoesNotExist:
        return HttpResponseNotFound("<h2>Measurement not found</h2>")

def Delete(request, id):
    try:
        measure = Measurement.objects.get(id=id)
        measure.delete()
        return render(request, 'WasDeleted.html')
    except Measurement.DoesNotExist:
        return HttpResponseNotFound("<h2>Measurement not found</h2>")

def Stat (request):
    coords_list = Coordinates.objects.all()
    m = folium.Map(width='100%', height='100%',tiles='cartodb dark_matter', location=[59.9386, 30.3141], zoom_start=12)
    for coord in coords_list:
        measurments = Measurement.objects.filter(location=coord.id).values_list('Nlevel', flat=True)
        print(measurments)
        noize = 0
        color = "green"
        if len(measurments) > 0:
            for x in measurments:
                noize += x
            noize = noize / len(measurments)
            color = getColor(noize)
            folium.Marker([coord.lat, coord.lon], popup=f"Оценочный уровень шума: {noize} дБ",
                      icon=folium.Icon(color=color)).add_to(m)
    m = m._repr_html_()

    context = {
        'coords_list': coords_list,
        'map': m,
    }
    return render(request, 'stats.html', context=context)