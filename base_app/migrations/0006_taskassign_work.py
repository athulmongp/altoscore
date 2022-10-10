# Generated by Django 4.1 on 2022-09-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_delete_taskassign_delete_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_date', models.DateField(blank=True, null=True)),
                ('employee_name', models.CharField(blank=True, max_length=200, null=True)),
                ('task_work', models.CharField(blank=True, max_length=200, null=True)),
                ('task_category', models.CharField(blank=True, max_length=200, null=True)),
                ('task_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateField(blank=True, null=True)),
                ('work_head', models.CharField(blank=True, max_length=200, null=True)),
                ('work_name', models.CharField(blank=True, max_length=200, null=True)),
                ('work_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]