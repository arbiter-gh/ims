# Generated by Django 4.0.4 on 2022-06-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0022_term_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term_insurance',
            name='claim_settelment',
            field=models.FloatField(),
        ),
    ]
