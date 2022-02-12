# Generated by Django 4.0.2 on 2022-02-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='liquor_pref',
            field=models.CharField(choices=[('V', 'Vodka'), ('G', 'Gin'), ('R', 'Rum'), ('T', 'Tequila')], default='V', max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q1',
            field=models.CharField(choices=[('W', 'Work'), ('P', 'Play')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q2',
            field=models.CharField(choices=[('A', 'Adventurous'), ('C', 'Classic')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q3',
            field=models.CharField(choices=[('P', 'Pick-Me-Up'), ('R', 'Relaxation')], default='P', max_length=1),
        ),
    ]
