# Generated by Django 4.1 on 2022-09-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_tldproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TLDPojectDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tld_project_module', models.CharField(blank=True, max_length=100, null=True)),
                ('tld_project_descrip', models.TextField()),
                ('tld_project_ui', models.ImageField(null=True, upload_to='ProjectUI')),
                ('tld_project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.tldproject')),
            ],
        ),
    ]