# Generated by Django 3.2.16 on 2023-02-02 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrainer', '0007_alter_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='gymtrainer.MyClubUser'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='first_name',
            field=models.CharField(max_length=120, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='last_name',
            field=models.CharField(max_length=120, verbose_name='Last Name'),
        ),
    ]