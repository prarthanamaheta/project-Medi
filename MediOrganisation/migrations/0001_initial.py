# Generated by Django 4.0.4 on 2022-05-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(default='', max_length=50)),
                ('organisation_address', models.CharField(max_length=200)),
                ('organisation_mobile', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
