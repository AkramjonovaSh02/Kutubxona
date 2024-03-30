# Generated by Django 5.0.3 on 2024-03-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp_3', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talaba',
            options={'verbose_name': 'Talaba', 'verbose_name_plural': 'Talabalar'},
        ),
        migrations.AddField(
            model_name='muallif',
            name='tugilgan_sana',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kutubxonachi',
            name='ish_vaqti',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='kutubxonachi',
            name='ism',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='muallif',
            name='ism',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record',
            name='olingan_sana',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='qaytarish_sana',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='guruh',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='ism',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='kitob_soni',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]