# Generated by Django 4.1 on 2023-03-24 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0040_batch_dm_project_task_dm_projects_usermanuvel_and_more'),
    ]

    operations = [
      
        migrations.AddField(
            model_name='user_registration',
            name='trainee_status',
            field=models.IntegerField(default='0'),
        )
        
    ]