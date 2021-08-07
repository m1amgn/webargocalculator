from django.shortcuts import render
from .forms import CalculateForms
from .models import ElementsConcentration, Culture, VegetationMode

# Create your views here.
def webpage(request):
    form = CalculateForms()
    return render(request, 'index.html', {'form': form})

def calculated(request):
    culture = request.POST['culture']
    culture = Culture.objects.get(pk=culture)
    climat_zone = request.POST['climat_zone']
    climat_zone = VegetationMode.objects.get(pk=climat_zone)
    N = request.POST['N']
    P2O5 = request.POST['P2O5']
    K2O = request.POST['K2O']
    Mg = request.POST['Mg']
    S = request.POST['S']
    Ca = request.POST['Ca']
    Fe = request.POST['Fe']
    Mn = request.POST['Mn']
    Zn = request.POST['Zn']
    Cu = request.POST['Cu']
    B = request.POST['B']
    Mo = request.POST['Mo']
    Co = request.POST['Co']
    Se = request.POST['Se']
    quantity_of_water = request.POST['quantity_of_water']
    temperature = request.POST['temperature']
    productivity = request.POST['productivity']

    ElementsConcentration.objects.create(culture=culture, climat_zone=climat_zone, N=N, P2O5=P2O5, K2O=K2O, Mg=Mg, S=S,
                                         Ca=Ca, Fe=Fe, Mn=Mn, Zn=Zn, Cu=Cu, B=B, Mo=Mo, Co=Co, Se=Se,
                                         quantity_of_water=quantity_of_water, temperature=temperature,
                                         productivity=productivity)

    return render(request, 'calculated.html')