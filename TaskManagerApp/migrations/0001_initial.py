# Generated by Django 4.2 on 2023-04-19 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=100)),
                ('PDescription', models.TextField()),
                ('StartDate', models.DateField(auto_now=True)),
                ('EndDate', models.DateField(blank=True, null=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskManagerApp.clientmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(max_length=100)),
                ('TDescription', models.TextField()),
                ('Status', models.CharField(max_length=100)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskManagerApp.projectmodel')),
            ],
        ),
    ]
