from .models import Coordinates, Measurement, Estimation
#helper functions

def generalize(request):
    coords_list = Coordinates.objects.all()
    for coord in coords_list:
        measurments = Measurement.objects.filter(location_id=coord.id)
        print(measurments)

    return