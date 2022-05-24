# Generated by Django 3.2 on 2022-05-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('raiting', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('horror', 'Horror'), ('drama', 'Drama'), ('comedy', 'Comedy'), ('action', 'Action')], max_length=10)),
            ],
        ),
    ]