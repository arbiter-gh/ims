# Generated by Django 4.0.3 on 2022-05-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='f_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='l_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]