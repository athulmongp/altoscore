# Generated by Django 4.1 on 2022-10-22 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0048_dm_project_dese'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSproject_Task_verify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_task_verify_date', models.DateField(auto_now_add=True, null=True)),
                ('ts_project_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project_taskassign')),
            ],
        ),
    ]