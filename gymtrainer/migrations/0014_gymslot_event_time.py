# Generated by Django 3.2.16 on 2023-02-02 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrainer', '0013_alter_gymslot_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymslot',
            name='event_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=120, verbose_name='Event Date'),
            preserve_default=False,
        ),
    ]
