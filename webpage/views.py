from django.shortcuts import render
from .forms import CalculateForms
from .models import ElementsConcentration, Culture, VegetationMode, DefaultElementsConcentration, Productivity
from calculator.calc import make_graphs
from calculator.models import Graph


# Create your views here.
def webpage(request):
    form = CalculateForms()
    return render(request, 'index.html', {'form': form})

def calculated(request):
    elements_dict = {}
    for key, values in request.POST.dict().items():
        if values == '' or values == '0':
            if key == 'productivity':
                climat_zone = request.POST['climat_zone']
                obj = Productivity.objects.get(pk=climat_zone)
                field_object = Productivity._meta.get_field(key)
                field_value = field_object.value_from_object(obj)
                elements_dict_add = {key: field_value}
                elements_dict.update(elements_dict_add)
            else:
                obj = DefaultElementsConcentration.objects.first()
                field_object = DefaultElementsConcentration._meta.get_field(key)
                field_value = field_object.value_from_object(obj)
                elements_dict_add = {key: field_value}
                elements_dict.update(elements_dict_add)
        else:
            if key == 'culture':
                culture = Culture.objects.get(pk=values)
                elements_dict_add = {key: culture}
                elements_dict.update(elements_dict_add)
            elif key == 'climat_zone':
                climat_zone = VegetationMode.objects.get(pk=values)
                elements_dict_add = {key: climat_zone}
                elements_dict.update(elements_dict_add)
            else:
                elements_dict_add = {key: values}
                elements_dict.update(elements_dict_add)

    make_graphs(elements_dict)
    context = {'graph': Graph.objects.latest('created_timestamp')}
    ElementsConcentration.objects.create(culture=elements_dict['culture'], climat_zone=elements_dict['climat_zone'],
                                        N=elements_dict['N'], P2O5=elements_dict['P2O5'], K2O=elements_dict['K2O'],
                                        Mg=elements_dict['Mg'], S=elements_dict['S'], Ca=elements_dict['Ca'],
                                        Fe=elements_dict['Fe'], Mn=elements_dict['Mn'], Zn=elements_dict['Zn'],
                                        Cu=elements_dict['Cu'], B=elements_dict['B'], Mo=elements_dict['Mo'],
                                        Co=elements_dict['Co'], Se=elements_dict['Se'],
                                        # quantity_of_water=elements_dict['quantity_of_water'],
                                        # temperature=elements_dict['temperature'],
                                        productivity=elements_dict['productivity'])

    elements_dict.clear()
    return render(request, 'calculated.html', context)