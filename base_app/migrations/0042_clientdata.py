# Generated by Django 4.1 on 2022-10-17 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0041_companyanalysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_date', models.DateField(blank=True, null=True)),
                ('cd_name', models.CharField(blank=True, max_length=150, null=True)),
                ('cd_email', models.EmailField(max_length=254)),
                ('cd_phno', models.CharField(blank=True, max_length=50, null=True)),
                ('cd_bussines', models.TextField()),
                ('cd_Employeeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('cd_taskid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task')),
            ],
        ),
    ]