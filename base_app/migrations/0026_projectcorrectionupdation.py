# Generated by Django 4.1 on 2022-10-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0025_delete_projectcorrectionupdation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCorrectionUpdation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_cu_module', models.CharField(blank=True, max_length=100, null=True)),
                ('project_cu_descrip', models.TextField()),
                ('project_oldui', models.ImageField(null=True, upload_to='ProjectUI')),
                ('project_cu_olddescrip', models.TextField()),
                ('project_cu_newui', models.ImageField(null=True, upload_to='ProjectUI')),
                ('project_cu_newdescrip', models.TextField()),
                ('project_cu_start', models.CharField(blank=True, max_length=100, null=True)),
                ('project_cu_end', models.CharField(blank=True, max_length=100, null=True)),
                ('project_cu_wdays', models.CharField(blank=True, max_length=50, null=True)),
                ('project_cu_status', models.CharField(blank=True, max_length=50, null=True)),
                ('project_cu_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.pm_projectdocumentdetails')),
                ('project_cu_review_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.tldprojectreview')),
            ],
        ),
    ]
