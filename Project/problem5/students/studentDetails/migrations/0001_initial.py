# Generated by Django 2.2.16 on 2021-03-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('ROllNumber', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
            ],
        ),
    ]
