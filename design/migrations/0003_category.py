# Generated by Django 3.2.8 on 2021-11-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=255)),
            ],
        ),
    ]
