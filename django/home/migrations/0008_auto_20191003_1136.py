# Generated by Django 2.2.5 on 2019-10-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_home_url1'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='Slogan',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='Title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='ico',
            field=models.ImageField(blank=True, height_field=16, null=True, upload_to='ico/', width_field=16),
        ),
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.CharField(max_length=80, null=True),
        ),
    ]