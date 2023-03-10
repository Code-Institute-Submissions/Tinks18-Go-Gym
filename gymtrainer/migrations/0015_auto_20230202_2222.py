# Generated by Django 3.2.16 on 2023-02-02 22:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrainer', '0014_gymslot_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymslot',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='gymslot',
            name='event_time',
        ),
        migrations.AddField(
            model_name='gymslot',
            name='slot_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='Event Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gymslot',
            name='slot_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='Event Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gymslot',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='gymslot',
            name='lastname',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
    ]
