# Generated by Django 4.2.2 on 2024-07-02 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0012_alter_mailingparameters_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingparameters',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 13, 33, 59, 124011, tzinfo=datetime.timezone.utc), verbose_name='конец рассылки'),
        ),
    ]
