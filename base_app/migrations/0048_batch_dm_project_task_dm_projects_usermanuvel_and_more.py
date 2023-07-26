# Generated by Django 4.1 on 2023-07-26 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0047_batch_dm_project_task_dm_projects_usermanuvel_and_more'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='certificate_approve',
            name='cf_category',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='certificate_approve',
            name='cf_intern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Intern_Certificate_user', to='base_app.internship'),
        ),
        
    ]
