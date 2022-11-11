# Generated by Django 4.1 on 2022-11-11 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0081_workrequest_wrkreq_tl'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_taskassign',
            name='projmodule',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Projectmanagerworkassign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assing_date', models.DateField(auto_now_add=True, null=True)),
                ('pm_task_status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('pm_project_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pm_prtask', to='base_app.project_taskassign')),
            ],
        ),
        migrations.CreateModel(
            name='project_other_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_name', models.CharField(blank=True, max_length=255, null=True)),
                ('other_description', models.TextField()),
                ('othproject_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_other_name', to='base_app.project')),
            ],
        ),
    ]
