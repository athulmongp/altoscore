# Generated by Django 3.2.12 on 2022-04-30 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0020_trainer_task_delay'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name_id', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_table_name', to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='project_module_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('project_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_name', to='base_app.project')),
            ],
        ),
    ]