# Generated by Django 4.1 on 2022-11-07 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0074_trainer_task_task_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainer_task_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_task_type', models.CharField(default='0', max_length=25)),
                ('trainer_correction', models.TextField()),
                ('trainer_files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('t_status', models.CharField(default='', max_length=50)),
                ('sub_date', models.DateField(blank=True, null=True)),
                ('test_date', models.DateField(auto_now_add=True, null=True)),
                ('team_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_name_trainer', to='base_app.create_team')),
                ('traine_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ttname', to='base_app.trainer_task')),
                ('trainee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainee_task', to='base_app.user_registration')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_task', to='base_app.user_registration')),
            ],
        ),
    ]