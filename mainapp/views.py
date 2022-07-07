from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from mainapp.models import Package, Alarm
from datetime import date


def main(request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
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
    package_name = Package.NAME_CHOICES
    package_category = Package.CATEGORY_CHOICES

    content = {
        'links_menu': links_menu,
        'links_form': links_form,
        'title': 'расчет',
        'package_name': package_name,
        'package_category': package_category,
        'almes': almes
    }
    return render(request, 'mainapp/calculation.html', content)


def instruction(request):
    links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'calculation', 'name': 'Запись'},
        {'href': 'view', 'name': 'Просмотр'},
        {'href': 'instruction', 'name': 'Инструкция'},

    ]
    content = {
        'links_menu': links_menu,
        'title': 'инструкция'
    }
    return render(request, 'mainapp/instruction.html', content)


def view(request):
    def str_for_datetime(s):
        import datetime

        out = []
        month = {
            'Jan.': '01',
            'Feb.': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'Aug.': '08',
            'Sept.': '09',
            'Oct.': '10',
            'Nov.': '11',
            'Dec.': '12'
        }
        date = s.split(",")
        year = date[1].strip()
        day_month = date[0].split(' ')
        out.append(year)
        out.append(month[day_month[0]])
        out.append(day_month[1])
        out = '/'.join(out)
        result = datetime.datetime.strptime(out, '%Y/%m/%d')
        return result

    date_set = {package.pub_date for package in Package.objects.all()}
    date_list = (list(date_set))
    date_list.sort(reverse=True)
    date_list.insert(0, '')
    if request.method == 'POST':
        sort_for_date = request.POST.get('pub_date')
        if sort_for_date == date_list[0]:
            return HttpResponseRedirect(reverse("view"))
        view_sort_for_date = str_for_datetime(sort_for_date)
    else:
        view_sort_for_date = date_list[1]

    sort_list = [obj for obj in Package.objects.filter(pub_date=view_sort_for_date)]
    summa_obj = 0
    for item in sort_list:
        summa_obj += item.calculations
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
        'summa_obj': summa_obj,
        'date_list': date_list,
        'sort_list': sort_list
    }
    return render(request, 'mainapp/view.html', content)


def create(request):
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
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 8700 мм.)</h2>")
        elif tom.name == 'Резервуар 66':
            if int(tom.height) < 11900:
                tom.calculations = tom.calc(tom.mass_66)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 11900 мм.)</h2>")
        elif tom.name == 'Резервуар 67':
            if int(tom.height) < 11900:
                tom.calculations = tom.calc(tom.mass_67)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 11900 мм.)</h2>")
        elif tom.name == 'Резервуар 5':
            if int(tom.height) < 3210:
                tom.calculations = tom.calc_h(tom.mass_5)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 3210 мм.)</h2>")
        elif tom.name == 'Резервуар 6':
            if int(tom.height) < 3210:
                tom.calculations = tom.calc_h(tom.mass_6)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 3210 мм.)</h2>")
        elif tom.name == 'Резервуар 7':
            if tom.height < '2710':
                tom.calculations = tom.calc_7(tom.mass_7)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 2710 мм.)</h2>")
        elif tom.name == 'Резервуар 8':
            if int(tom.height) < 2760:
                tom.calculations = tom.calc_h(tom.mass_8)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 2760 мм.)</h2>")
        elif tom.name == 'Резервуар Д':
            if int(tom.height) < 1450:
                tom.calculations = tom.calc_h(tom.mass_d)
                tom.save()
            else:
                return HttpResponseNotFound(
                    "<h2>Ошибка записи, проверьте правильность ввода. (максимальный взлив 1450 мм.)</h2>")
    return HttpResponseRedirect(reverse('calculation'))


def delete(request, id):
    try:
        package = Package.objects.get(id=id)
        package.delete()
        return HttpResponseRedirect(reverse("view"))
    except Package.DoesNotExist:
        return HttpResponseNotFound("<h2>Object not found</h2>")
