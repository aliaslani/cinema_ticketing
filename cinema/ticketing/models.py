from tabnanny import verbose
from django.db import models

class Movie(models.Model):
    '''
        represents a Movie
    '''
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم‌'
    name = models.CharField(verbose_name='نام فیلم', max_length=100)
    director = models.CharField(verbose_name='نام کارگردان', max_length=50)
    year = models.IntegerField(verbose_name='سال تولید')
    length = models.IntegerField(verbose_name='مدت زمان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

class Cinema(models.Model):
    '''
        represents a cinema saloon
    '''
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
    cinema_code = models.IntegerField('کد سینما', primary_key=True)
    name = models.CharField('نام سینما', max_length=50)
    city = models.CharField('شهر', max_length=30, default="اصفهان")
    capacity = models.IntegerField('گنجایش')
    phone = models.CharField('تلفن', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name

class ShowTime(models.Model):
    '''
        represents a movie show in a cinema at a specific time
    '''
    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس‌'
    movie = models.ForeignKey('Movie', verbose_name = 'نام فیلم', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', verbose_name='نام سینما', on_delete=models.PROTECT)
    start_time = models.DateTimeField('شروع سانس')
    price = models.IntegerField('قیمت بلیت')
    salable_seats = models.IntegerField('صندلی قابل فروش')
    free_seats = models.IntegerField('صندلی خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKET_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKET_SOLD, 'بلیت‌ها فروخته شد'),
        (SALE_CLOSED, 'فروش بسته شد'),
        (MOVIE_PLAYED, 'فیلم به پایان رسید'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return f'{self.movie} - {self.cinema} - {self.start_time}'
        
