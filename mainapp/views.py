from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from mainapp.models import Package, Sort_data, Alarm
from datetime import date




def main (request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'auto', 'name': 'Авто'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]
    content = {
        'links_menu': links_menu,
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', content)



def calculation(request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'auto', 'name': 'Авто'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]

    links_form = [
        {'name': 'Резервуар №5'},
        {'name': 'Резервуар №6'},
        {'name': 'Резервуар №7'},
        {'name': 'Резервуар №8'},
        {'name': 'Резервуар №Д'},
        {'name': 'Резервуар №65'},
        {'name': 'Резервуар №66'},
        {'name': 'Резервуар №67'},
    ]
    almes = Alarm.objects.last()
    packages = Package.objects.all()
    package_name = Package.NAME_CHOICES
    package_category = Package.CATEGORY_CHOICES
    uniq_date =[]
    for p in packages:
        if p.pub_date not in uniq_date:
            uniq_date.append(p.pub_date)
    all_calc_date = 0
    user_date = date.today()
    for package in packages:
        if package.pub_date == user_date:
            all_calc_date += package.calculations


    content = {
        'links_menu': links_menu,
        'links_form': links_form,
        'title': 'расчет',
        'packages': packages,
        'package_name': package_name,
        'package_category': package_category,
        'all_calc_date': all_calc_date,
        'uniq_date': uniq_date,
        'almes': almes
        }
    return render(request, 'mainapp/calculation.html', content)

def auto (request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'auto', 'name': 'Авто'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]
    content = {
        'links_menu': links_menu,
        'title': 'авто'
    }
    return render(request, 'mainapp/auto.html', content)

def instruction (request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'auto', 'name': 'Авто'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]
    content = {
        'links_menu': links_menu,
        'title': 'инструкция'
    }
    return render(request, 'mainapp/instruction.html', content)

def view (request):
    packages = Package.objects.all()
    uniq_obj = []
    uniq_date = []
    for p in packages:
        if p.pub_date not in uniq_date:
            uniq_date.append(p.pub_date)
            uniq_obj.append(p)

    all_calc_date = 0
    sort_list = []
    sorting = Sort_data.objects.all()
    sort_data_now = ''
    for s_l_n in sorting:
        sort_data_now = s_l_n.sort_data
    packages = Package.objects.all()
    for package in packages:
        if package.pub_date == sort_data_now:
            sort_list.append(package)
            all_calc_date += package.calculations

    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'auto', 'name': 'Авто'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]
    content = {
        'links_menu': links_menu,
        'title': 'просмотр',
        'uniq_date': uniq_date,
        "uniq_obj": uniq_obj,
        'sort_list': sort_list,
        'all_calc_date': all_calc_date,
        'sort_data_now': sort_data_now
    }
    return render(request, 'mainapp/view.html', content)

def create (request):
    if request.method == "POST":
        tom = Package()
        tom.name = request.POST.get("name")
        tom.pub_date = request.POST.get("pub_date")
        tom.category = request.POST.get("category")
        tom.height = request.POST.get("height")
        tom.temperature_1 = request.POST.get("temperature_1")
        tom.temperature_2 = request.POST.get("temperature_2")
        tom.temperature_3 = request.POST.get("temperature_3")
        tom.density_1 = request.POST.get("density_1")
        tom.density_2 = request.POST.get("density_2")
        tom.density_3 = request.POST.get("density_3")
        tom.water = request.POST.get("water")
        if tom.name == 'Резервуар 65':
            if int(tom.height) < 8700:
                tom.calculations = tom.calc(tom.mass_65)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 8700 мм.)</h2>")
        elif tom.name == 'Резервуар 66':
            if int(tom.height) < 11900:
                tom.calculations = tom.calc(tom.mass_66)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 11900 мм.)</h2>")
        elif tom.name == 'Резервуар 67':
            if int(tom.height) < 11900:
                tom.calculations = tom.calc(tom.mass_67)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 11900 мм.)</h2>")
        elif tom.name == 'Резервуар 5':
            if int(tom.height) < 3210:
                tom.calculations = tom.calc_h(tom.mass_5)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 3210 мм.)</h2>")
        elif tom.name == 'Резервуар 6':
            if int(tom.height) < 3210:
                tom.calculations = tom.calc_h(tom.mass_6)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 3210 мм.)</h2>")
        elif tom.name == 'Резервуар 7':
            if tom.height <'2710':
                tom.calculations = tom.calc_7(tom.mass_7)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 2710 мм.)</h2>")
        elif tom.name == 'Резервуар 8':
            if int(tom.height) < 2760:
                tom.calculations = tom.calc_h(tom.mass_8)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 2760 мм.)</h2>")
        elif tom.name == 'Резервуар Д':
            if int(tom.height) < 1450:
                tom.calculations = tom.calc_h(tom.mass_d)
                tom.save()
            else:
                return HttpResponseNotFound("<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 1450 мм.)</h2>")
    return HttpResponseRedirect(reverse('calculation'))



def delete(request, id):
    try:
        package = Package.objects.get(id=id)
        package.delete()
        return HttpResponseRedirect(reverse("view"))
    except Package.DoesNotExist:
        return HttpResponseNotFound("<h2>Object not found</h2>")


def sort(request):
    if request.method == "POST":
        sort_data = Sort_data()
        sort_data.sort_data = request.POST.get("sort_data")
        sort_data.save()
    return HttpResponseRedirect(reverse("view"))

def print(request):
    return render(request, 'mainapp/print.html')