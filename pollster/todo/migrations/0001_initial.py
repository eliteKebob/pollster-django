# Generated by Django 4.0.5 on 2022-07-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
