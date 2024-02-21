# Generated by Django 5.0.1 on 2024-01-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=500)),
                ('due_dt', models.DateField()),
                ('is_completed', models.BooleanField(default=0)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
    ]
