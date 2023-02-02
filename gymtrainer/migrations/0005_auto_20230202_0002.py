# Generated by Django 3.2.16 on 2023-02-02 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrainer', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCLUbUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('email_address', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=320)),
                ('zip_code', models.CharField(max_length=15, verbose_name='ZIp Code')),
                ('phone', models.CharField(max_length=120, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='gymtrainer.MyCLUbUser'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymtrainer.venue'),
        ),
    ]