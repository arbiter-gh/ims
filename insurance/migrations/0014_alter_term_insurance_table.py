# Generated by Django 4.0.4 on 2022-05-31 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0013_rename_policy_term_insurance'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='term_insurance',
            table='term_insurance',
        ),
    ]
