# Generated by Django 2.2.16 on 2021-03-31 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentDetails', '0002_auto_20210331_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='StudentName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentDetails.Insert'),
        ),
    ]