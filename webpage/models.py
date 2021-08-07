from django.db import models

# Create your models here.


class Culture(models.Model):
    culture = models.CharField(max_length=20, verbose_name='Культура')

    def __str__(self):
        return self.culture

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культуры'

class VegetationMode(models.Model):
    climat_zone = models.CharField(max_length=50, verbose_name='Климатическая зона', default='')


    def __str__(self):
        return self.climat_zone

    class Meta:
        verbose_name = 'Климатическая зона'
        verbose_name_plural = 'Климатические зоны'

class Productivity(models.Model):
    productivity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Урожайность')
    climat_zone = models.ForeignKey(VegetationMode, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.culture

    class Meta:
        verbose_name = 'Урожайность'
        verbose_name_plural = 'Урожайность'

class ElementsConcentration(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, null=True)
    climat_zone = models.ForeignKey(VegetationMode, on_delete=models.CASCADE, null=True)
    N = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    P2O5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    K2O = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    S = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Ca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Fe = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mn = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Zn = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Cu = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    B = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Co = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Se = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantity_of_water = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    productivity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_timestamp)

    class Meta:
        verbose_name = 'Данные из формы'
        verbose_name_plural = 'Данные из формы'




    # first_name = models.CharField(_('First Name'),
    #                     max_length = 200,
    #                     help_text = _('What is your name?'))
    #
    # last_name = models.CharField(_('Last Name'),
    #                     max_length = 200,
    #                     help_text = _('What is your name?'))


# created_timestamp = models.DateTimeField(auto_now_add=True)
# class Meta:
#     model=someForm
#     fields=['Dropdown']
#    widgets = {
#      'Dropdown': forms.Select(attrs={'id':'choicewa'}),
#      }




# def create(request):
#     if request.POST:
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/articles/all/')
#     else:
#         form = ArticleForm()
#         args={}
#         args.update(csrf(request))
#         args['categories'] = ArticleCategory.objects.all()
#         args['form'] = form
#         return render_to_response('create_article.html', args)
#

# Вам не нужно делать это вручную. Если ваш ArticleForm равен ModelForm и не исключает поле category ,
# то вы можете просто написать {{ form.category }} и автоматически получить выпадающий список, созданный django.
# Он использует ModelChoiceField под капотом.
