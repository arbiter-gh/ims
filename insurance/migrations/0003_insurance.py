# Generated by Django 4.0.3 on 2022-05-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('policy', models.CharField(max_length=50)),
                ('validity', models.IntegerField()),
                ('premium', models.IntegerField()),
            ],
            options={
                'db_table': 'insurance',
            },
        ),
    ]
