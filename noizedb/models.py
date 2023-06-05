from django.db import models
#from accounts.views import SignUpView
from django.contrib.auth.models import User

#координаты точек привязки измерений
class Coordinates(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.lat}, {self.lon}'

#коррекция по происхождению
class CorFrom(models.Model):
    FromParam = models.CharField('Происхождение шума', max_length=100)
    FromCor = models.FloatField('Значение коррекции по происхожднию шума')

    def __str__(self):
        return f'Происхождение шума:{self.FromParam}'

#коррекция по характеру
class CorChark(models.Model):
    CharkParam = models.CharField('Характер источника шума', max_length=100)
    CharkCor = models.FloatField('Значение коррекции по характеру источника шума')

    def __str__(self):
        return f'Характер источника шума:{self.CharkParam}'


#измерения шума
class Measurement(models.Model):
    Nlevel = models.FloatField('Эквивалентный уровень шума')
    MNlevel = models.FloatField('Максимальный уровень шума', null=True)
    location = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    From = models.ForeignKey(CorFrom, on_delete=models.CASCADE)
    Chark = models.ForeignKey(CorChark, on_delete=models.CASCADE)
    Date = models.DateField('Дата проведения измерения', auto_now_add=True)
    Time = models.TimeField('Время проведения измерения', auto_now_add=True)
    Person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'"Эквивалентный уровень шума:{self.Nlevel}, координаты геолокаци:{self.location}, дата:{self.Date}, время:{self.Time}, данные введены пользователем {self.Person}'

#оценка измерений
class Estimation(models.Model):
    location = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    GenNlevel = models.FloatField('Оценочный уровень шума')
    Color = models.CharField('Соответствующий цвет', max_length=50, null=True)

