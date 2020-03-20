# Generated by Django 3.0.2 on 2020-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200320_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabChemist',
            fields=[
                ('lName', models.CharField(max_length=50)),
                ('lmobNo', models.CharField(max_length=50)),
                ('lEmail', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('lLicense', models.CharField(max_length=50)),
                ('lAddress', models.CharField(max_length=50)),
                ('lCity', models.CharField(max_length=50)),
                ('lPincode', models.CharField(max_length=30)),
                ('lPassword', models.CharField(max_length=20)),
                ('domain', models.CharField(max_length=20)),
            ],
        ),
    ]
