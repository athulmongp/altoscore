# Generated by Django 4.1 on 2022-09-30 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0011_tldprojectreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='TLDProjectCorrectionUpdation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tld_project_cu_module', models.CharField(blank=True, max_length=100, null=True)),
                ('tld_project_cu_descrip', models.TextField()),
                ('tld_project_oldui', models.ImageField(null=True, upload_to='ProjectUI')),
                ('tld_project_cu_olddescrip', models.TextField()),
                ('tld_project_cu_newui', models.ImageField(null=True, upload_to='ProjectUI')),
                ('tld_project_cu_newdescrip', models.TextField()),
                ('tld_project_cu_start', models.DateField(blank=True, null=True)),
                ('tld_project_cu_end', models.DateField(blank=True, null=True)),
                ('tld_project_cu_wdays', models.CharField(blank=True, max_length=50, null=True)),
                ('tld_project_cu_status', models.CharField(blank=True, max_length=50, null=True)),
                ('tld_project_cu_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.tldproject')),
            ],
        ),
    ]