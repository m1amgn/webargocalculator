import matplotlib.pyplot as plt
import io
from datetime import datetime
from django.core.files.base import ContentFile
from .models import ElementsConsuption, Graph


COEFFICIENT = float(40 * 1.4 * 0.1 * 100 / (100 - 26.5))

def get_elements_list(elements_dict):
    elements_list = []
    for key, values in elements_dict.items():
        if key == 'culture' or key == 'climat_zone' or key == 'productivity' or key == 'csrfmiddlewaretoken' or key == 'quantity_of_water' or key == 'temperature':
            pass
        else:
            elements_list.append(key)
    return elements_list

def get_concentration_list(elements_dict):
    concentration_list = []
    for key, values in elements_dict.items():
        if key == 'culture' or key == 'climat_zone' or key == 'productivity' or key == 'csrfmiddlewaretoken' or key == 'quantity_of_water' or key == 'temperature':
            pass
        else:
            concentration = round(float(values) * COEFFICIENT)
            concentration_list.append(concentration)
    return concentration_list

def get_consuption_list(elements_dict):
    consuption_list = []
    for key, values in elements_dict.items():
        obj = ElementsConsuption.objects.get(culture=elements_dict['culture'])
        if key == 'culture' or key == 'climat_zone' or key == 'productivity' or key == 'csrfmiddlewaretoken' or key == 'quantity_of_water' or key == 'temperature':
            pass
        else:
            field_object = ElementsConsuption._meta.get_field(key)
            field_value = field_object.value_from_object(obj)
            consuption = round(float(field_value) * float(elements_dict['productivity']))
            consuption_list.append(consuption)
    return consuption_list


def make_graphs(elements_dict):
    elements_list = get_elements_list(elements_dict)
    concentration_list = get_concentration_list(elements_dict)
    consuption_list = get_consuption_list(elements_dict)

    datetime_now = datetime.now()
    datetime_now_str = f'{str(datetime_now.day)}{str(datetime_now.month)}{str(datetime_now.year)}-{str(datetime_now.hour)}-{str(datetime_now.minute)}-{str(datetime_now.second)}.png'

    plt.title('Концентрация элементов питания')
    plt.xlabel('Элементы')
    plt.ylabel('Концентрация, кг на га')

    plt.bar(elements_list, consuption_list, label='Необходимая концентрация элементов питания', color='blue')
    plt.bar(elements_list, concentration_list, label='Доступные элементы в почве', color='green')
    plt.legend()
    f = io.BytesIO()
    plt.savefig(f)
    content_file = ContentFile(f.getvalue())
    model_object = Graph()
    model_object.graph_img.save(datetime_now_str, content_file)
    model_object.save()
    plt.close()