# Generated by Django 2.2.6 on 2019-10-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
    ]
