from datetime import date

from django.db import models

import calibration_8
import calibration_5
import calibration_d
import calibration_6
import calibration_66
import calibration_7
import calibration_65
import calibration_67


class Package(models.Model):
    CATEGORY_CHOICES = (
        ('Вертикальный', 'Вертикальный'),
        ('Горизонтальный', 'Горизонтальный'),
    )
    NAME_CHOICES = (
        ('Резервуар Д', 'Резервуар Д'),
        ('Резервуар 5', 'Резервуар 5'),
        ('Резервуар 6', 'Резервуар 6'),
        ('Резервуар 7', 'Резервуар 7'),
        ('Резервуар 8', 'Резервуар 8'),
        ('Резервуар 65', 'Резервуар 65'),
        ('Резервуар 66', 'Резервуар 66'),
        ('Резервуар 67', 'Резервуар 67'),
    )
    category = models.CharField(verbose_name='Вид емкости', max_length=128, choices=CATEGORY_CHOICES)
    pub_date = models.DateField('дата создания', default=date.today)
    name = models.CharField(verbose_name='номер емкости', max_length=128, choices=NAME_CHOICES)
    height = models.IntegerField(verbose_name='высота взлива', default=0)
    temperature_1 = models.FloatField(verbose_name='температура низ', default=0)
    temperature_2 = models.FloatField(verbose_name='температура середина', default=0)
    temperature_3 = models.FloatField(verbose_name='температура верх', default=0)
    density_1 = models.FloatField(verbose_name='плотность низ', default=0)
    density_2 = models.FloatField(verbose_name='плотность середина', default=0)
    density_3 = models.FloatField(verbose_name='плотность верх', default=0)
    water = models.IntegerField(verbose_name='подтоварная вода', default=0)
    calculations = models.FloatField(verbose_name='расчетный объем', default=0)

    def __init__(self, *args, **kwargs):
        super(Package, self).__init__(*args, **kwargs)


    #def __add__(self, other):
        #return Package(self.temperature_2 + other.temperature_2, self.temperature_1 + other.temperature_1,
                       #self.temperature_3 + other.temperature_3, self.temperature_1 + other.temperature_2,
                       #self.temperature_1 + other.temperature_3, self.temperature_2 + other.temperature_1,
                       #self.temperature_2 + other.temperature_3, self.temperature_3 + other.temperature_1,
                       #self.temperature_3 + other.temperature_2), (self.density_1 + other.density_1,
                       #self.density_2 + other.density_2, self.density_3 + other.density_3,
                       #self.density_3 + other.density_3, self.density_1 + other.density_2,
                       #self.density_1 + other.density_3, self.density_2 + other.density_1,
                       #self.density_2 + other.density_3, self.density_3 + other.density_1)


    #def __floordiv__(self, other):
        #return Package(self.water // other.water, self.height // other.height)

    #def __mod__(self, other):
        #return Package(self.water % other.water, self.height % other.height)

    #def __int__(self):
        #return int(self.water), int(self.height)

    #def __float__(self):
        #return float(self.calculations), float(self.temperature_1), float(self.temperature_2), float(self.temperature_3), float(self.density_1), float(self.density_2), float(self.density_3)

    @property
    def mass_65(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_65.calibration_65[sr] - calibration_65.calibration_65[tr]) / 10) * fr) +
                                calibration_65.calibration_65[tr]))) - (float(
                '{:.3f}'.format((((calibration_65.calibration_65[sw] - calibration_65.calibration_65[tw]) / 10) * fw) +
                                calibration_65.calibration_65[tw])))
            # print(x)
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_65.calibration_65[sr] - calibration_65.calibration_65[tr]) / 10) * fr) +
                                calibration_65.calibration_65[tr]))
        return x

    @property
    def mass_66(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_66.calibration_66[sr] - calibration_66.calibration_66[tr]) / 10) * fr) +
                                calibration_66.calibration_66[tr]))) - (float(
                '{:.3f}'.format((((calibration_66.calibration_66[sw] - calibration_66.calibration_66[tw]) / 10) * fw) +
                                calibration_66.calibration_66[tw])))
            # print(x)
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_66.calibration_66[sr] - calibration_66.calibration_66[tr]) / 10) * fr) +
                                calibration_66.calibration_66[tr]))
        return x

    @property
    def mass_67(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_67.calibration_67[sr] - calibration_67.calibration_67[tr]) / 10) * fr) +
                                calibration_67.calibration_67[tr]))) - (float(
                '{:.3f}'.format((((calibration_67.calibration_67[sw] - calibration_67.calibration_67[tw]) / 10) * fw) +
                                calibration_67.calibration_67[tw])))
            # print(x)
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_67.calibration_67[sr] - calibration_67.calibration_67[tr]) / 10) * fr) +
                                calibration_67.calibration_67[tr]))
        return x

    @property
    def mass_8(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_8.calibration_8[sr] - calibration_8.calibration_8[tr]) / 10) * fr) +
                                calibration_8.calibration_8[tr]))) - (float(
                '{:.3f}'.format((((calibration_8.calibration_8[sw] - calibration_8.calibration_8[tw]) / 10) * fw) +
                                calibration_8.calibration_8[tw])))
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_8.calibration_8[sr] - calibration_8.calibration_8[tr]) / 10) * fr) +
                                calibration_8.calibration_8[tr]))
        return x

    @property
    def mass_5(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_5.calibration_5[sr] - calibration_5.calibration_5[tr]) / 10) * fr) +
                                calibration_5.calibration_5[tr]))) - (float(
                '{:.3f}'.format((((calibration_5.calibration_5[sw] - calibration_5.calibration_5[tw]) / 10) * fw) +
                                calibration_5.calibration_5[tw])))
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_5.calibration_5[sr] - calibration_5.calibration_5[tr]) / 10) * fr) +
                                calibration_5.calibration_5[tr]))
        return x

    @property
    def mass_d(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_d.calibration_d[sr] - calibration_d.calibration_d[tr]) / 10) * fr) +
                                calibration_d.calibration_d[tr]))) - (float(
                '{:.3f}'.format((((calibration_d.calibration_d[sw] - calibration_d.calibration_d[tw]) / 10) * fw) +
                                calibration_d.calibration_d[tw])))
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_d.calibration_d[sr] - calibration_d.calibration_d[tr]) / 10) * fr) +
                                calibration_d.calibration_d[tr]))
        return x

    @property
    def mass_6(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_6.calibration_6[sr] - calibration_6.calibration_6[tr]) / 10) * fr) +
                                calibration_6.calibration_6[tr]))) - (float(
                '{:.3f}'.format((((calibration_6.calibration_6[sw] - calibration_6.calibration_6[tw]) / 10) * fw) +
                                calibration_6.calibration_6[tw])))
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_6.calibration_6[sr] - calibration_6.calibration_6[tr]) / 10) * fr) +
                                calibration_6.calibration_6[tr]))
        return x

    @property
    def mass_7(self):
        if int(self.water) > 0:
            fw = int(self.water) % 10
            tw = int(self.water) // 10
            sw = tw + 1
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = (float(
                '{:.3f}'.format((((calibration_7.calibration_7[sr] - calibration_7.calibration_7[tr]) / 10) * fr) +
                                calibration_7.calibration_7[tr]))) - (float(
                '{:.3f}'.format((((calibration_7.calibration_7[sw] - calibration_7.calibration_7[tw]) / 10) * fw) +
                                calibration_7.calibration_7[tw])))
        else:
            fr = int(self.height) % 10
            tr = int(self.height) // 10
            sr = tr + 1
            x = float(
                '{:.3f}'.format((((calibration_7.calibration_7[sr] - calibration_7.calibration_7[tr]) / 10) * fr) +
                                calibration_7.calibration_7[tr]))
        return x

    def calc(self, x):
        if int(self.height) < 1000:
            p = float('{:.1f}'.format(float(self.density_3)))
        elif int(self.height) <= 2000:
            p = float('{:.1f}'.format((float(self.density_1) + float(self.density_3)) / 2))
        else:
            p = float('{:.1f}'.format((float(self.density_1) + (3 * float(self.density_2)) + float(self.density_3)) / 5))
        if int(self.height) < 1000:
            t = float('{:.1f}'.format(float(self.temperature_3)))
        elif int(self.height) <= 2000:
            t = float('{:.1f}'.format((float(self.temperature_1) + float(self.temperature_3)) / 2))
        else:
            t = float('{:.1f}'.format((float(self.temperature_1) + (3 * float(self.temperature_2)) + float(self.temperature_3)) / 5))
        result = int((x * (1 + (2 * 12.5 * 10 ** -6 + 12.5 * 10 ** -6) * (t - 20))) * p)

        return result

    def calc_h(self, x):
        if float(self.density_2) == 0:
            p = float('{:.1f}'.format(float(self.density_3)))
        elif float(self.density_3) == 0:
            p = float('{:.1f}'.format((float(self.density_1) + (3 * float(self.density_2))) / 4))
        else:
            p = float('{:.1f}'.format((float(self.density_1) + (6 * float(self.density_2)) + float(self.density_3)) / 8))

        if float(self.temperature_2) == 0:
            t = float('{:.1f}'.format(float(self.temperature_3)))
        elif float(self.temperature_3) == 0:
            t = float('{:.1f}'.format((float(self.temperature_1) + (3 * float(self.temperature_2))) / 4))
        else:
            t = float('{:.1f}'.format((float(self.temperature_1) + (6 * float(self.temperature_2)) + float(self.temperature_3)) / 8))
        result = int((x * (1 + (2 * 12.5 * 10 ** -6 + 23 * 10 ** -6) * (t - 20))) * p)

        return result

    def calc_7(self, x):
        if float(self.density_2) == 0:
            p = float('{:.1f}'.format(float(self.density_3)))
        elif float(self.density_3) == 0:
            p = float('{:.1f}'.format((float(self.density_1) + (3 * float(self.density_2))) / 4))
        else:
            p = float('{:.1f}'.format((float(self.density_1) + (6 * float(self.density_2)) + float(self.density_3)) / 8))

        if float(self.temperature_2) == 0:
            t = float('{:.1f}'.format(float(self.temperature_3)))
        elif self.temperature_3 == 0:
            t = float('{:.1f}'.format((float(self.temperature_1) + (3 * float(self.temperature_2))) / 4))
        else:
            t = float('{:.1f}'.format((float(self.temperature_1) + (6 * float(self.temperature_2)) + float(self.temperature_3)) / 8))
        result = int((x * (1 + (2 * 12.5 * 10 ** -6 + 12.5 * 10 ** -6) * (t - 20))) * p)

        return result


    def __str__(self):
        return f'{self.name}'


class Sort_data(models.Model):
    sort_data = models.DateField('дата отбора', default=date.today)

    def __str__(self):
        return f'{self.sort_data}'

class Alarm(models.Model):
    MESSAGE_CHOICES = (
        ('OK', 'Последняя попытка сохранения прошла успешно'),
        ('Bag', 'Ошибка сохранения, проверьте правильность вносимых данных'),
    )
    alrm = models.CharField(verbose_name='message', max_length=128, choices=MESSAGE_CHOICES)

    def __str__(self):
        return f'{self.alrm}'
