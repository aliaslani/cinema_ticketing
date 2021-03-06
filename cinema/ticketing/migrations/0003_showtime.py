# Generated by Django 4.0.1 on 2022-01-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('salable_seats', models.IntegerField()),
                ('free_seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'فروش آغاز نشده'), (2, 'در حال فروش بلیت'), (3, 'بلیت\u200cها فروخته شد'), (4, 'فروش بسته شد'), (5, 'فیلم به پایان رسید'), (6, 'سانس لغو شد')])),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.movie')),
            ],
        ),
    ]
