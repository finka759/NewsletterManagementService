# Generated by Django 5.0.6 on 2024-05-31 10:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=150, null=True, verbose_name='тема письма')),
                ('content', models.TextField(verbose_name='содержимое письма')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
            },
        ),
        migrations.CreateModel(
            name='MailingParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='mailing_no_name', max_length=50, verbose_name='название рассылки')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало рассылки')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='конец рассылки')),
                ('next_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата следующей рассылки')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('interval', models.CharField(choices=[('once', 'разово'), ('per_day', 'раз в день'), ('per_week', 'раз в неделю'), ('per_month', 'раз в месяц')], default='once', max_length=50, verbose_name='интервал рассылки')),
                ('client', models.ManyToManyField(to='client.client', verbose_name='получатель')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message')),
            ],
            options={
                'verbose_name': 'настройка рассылкм',
                'verbose_name_plural': 'настройки рассылок',
                'permissions': [('toggle_active', 'выключить рассылку')],
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_time_sending', models.DateTimeField(auto_now=True, null=True, verbose_name='время последней рассылки')),
                ('status', models.CharField(blank=True, max_length=50, null=True, verbose_name='статус попытки')),
                ('response', models.CharField(blank=True, max_length=200, null=True, verbose_name='ответ почтового сервера')),
                ('mailing_parameters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingparameters', verbose_name='параметры_рассылки')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
            },
        ),
    ]