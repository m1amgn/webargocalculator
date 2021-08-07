import matplotlib.pyplot as plt
from .models import DefaultElementsConcentration, ElementsConsuption


type_of_plant = 'Пшеница'
type = ElementsConsuption.objects.get(culture=type_of_plant)
productivity = 50

elements_list = []
concentration_list = []
consuption_list = []

def get_elements_list():
    elements = list(DefaultElementsConcentration.objects.filter(pk=1).values())
    for element in elements:
        for key, values in element.items():
            if key != 'id':
                elements_list.append(values)
    return elements_list

def get_concentration_list():
    concentration = list(DefaultElementsConcentration.objects.filter(pk=1).values())
    conc_list = []
    for conc in concentration:
        for key, values in conc.items():
            if key != 'id':
                conc_list.append(values)
    coefficient = 40 * 1.4 * 0.1 * 100 / (100 - 26.5)
    for conc in conc_list:
        conc = round(float(conc) * coefficient)
        concentration_list.append(conc)
    return concentration_list

def get_consuption_list():
    consuption = list(ElementsConsuption.objects.filter(pk=1).values())
    cons_list = []
    for cons in consuption:
        for key, values in cons.items():
            if key != 'id':
                cons_list.append(values)
    for cons in cons_list:
        cons = round(float(cons) * productivity)
        consuption_list.append(cons)
    return consuption_list

def make_graphs():
    elements_list = get_elements_list()
    consuption_list = get_consuption_list()
    concentration_list = get_concentration_list()

    plt.title('Недостаток элементов')
    plt.xlabel('Элементы')
    plt.ylabel('Концентрация, кг на га')

    plt.bar(elements_list, consuption_list, label='Необходимые элементы', color='blue')
    plt.bar(elements_list, concentration_list, label='Элементы в почве', color='green')
    plt.legend()
    plt.savefig('graphs.png')
