from django.shortcuts import render
from .forms import CalculateForms
from .models import ElementsConcentration, Culture, VegetationMode, DefaultElementsConcentration, Productivity, ElementsDescription
from calculator.calc import make_graphs, get_elements_list, get_concentration_list, get_consuption_list
from calculator.models import Graph
from orders.sendmessage import send_telegram
from orders.models import Order
from orders.forms import OrderForm


# Create your views here.
def webpage(request):
    form = CalculateForms()
    return render(request, 'index.html', {'form': form})

def calculated(request):
    elements_dict = {}
    try:
        for key, values in request.POST.dict().items():
            if values == '' or values == '0':
                if key == 'productivity':
                    climat_zone = request.POST['climat_zone']
                    obj = Productivity.objects.get(pk=climat_zone)
                    field_object = Productivity._meta.get_field(key)
                    field_value = field_object.value_from_object(obj)
                    elements_dict_add = {key: field_value}
                    elements_dict.update(elements_dict_add)
                elif key == 'quantity_of_water' or key == 'temperature':
                    elements_dict_add = {key: values}
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
    except Exception as e:
        print(e)

    make_graphs(elements_dict)
    elements_list = get_elements_list(elements_dict)
    concentration_list = get_concentration_list(elements_dict)
    consuption_list = get_consuption_list(elements_dict)
    form = OrderForm()

    context = {'graph': Graph.objects.latest('created_timestamp'),
               'elements_list': elements_list,
               'concentration_list': concentration_list,
               'consuption_list': consuption_list,
               'elements_description': ElementsDescription.objects.all(),
               'form': form,
               }
    try:
        ElementsConcentration.objects.create(culture=elements_dict['culture'], climat_zone=elements_dict['climat_zone'],
                                            N=elements_dict['N'], P=elements_dict['P'], K=elements_dict['K'],
                                            Mg=elements_dict['Mg'], S=elements_dict['S'], Ca=elements_dict['Ca'],
                                            Fe=elements_dict['Fe'], Mn=elements_dict['Mn'], Zn=elements_dict['Zn'],
                                            Cu=elements_dict['Cu'], B=elements_dict['B'], Mo=elements_dict['Mo'],
                                            Co=elements_dict['Co'], Se=elements_dict['Se'],
                                            quantity_of_water=elements_dict['quantity_of_water'],
                                            temperature=elements_dict['temperature'],
                                            productivity=elements_dict['productivity'])
    except Exception as e:
        print(e)

    elements_dict.clear()
    return render(request, 'calculated.html', context)

def get_order(request):
        name = request.POST['name']
        email = request.POST['email']
        order = Order(name=name, email=email)
        order.save()
        send_telegram(tg_name=name, tg_email=email)
        return render(request, 'order.html', {'name': name})
