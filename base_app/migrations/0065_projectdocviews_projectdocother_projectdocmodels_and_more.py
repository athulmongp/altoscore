# Generated by Django 4.1 on 2022-11-02 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0064_wrdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDocViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_v', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_vname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_vdise', models.TextField()),
                ('doc_project_v', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
                ('doc_vuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDocother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_oth', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_othname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_othdise', models.TextField()),
                ('doc_othuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('doc_project_oth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDocModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_md', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_mdname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_dise_md', models.TextField()),
                ('doc_mduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('doc_project_md', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDoclibraryies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_lb', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_lbname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_lbdise', models.TextField()),
                ('doc_lbuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('doc_project_lb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDochtmlpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_hp', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_hpname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_hpdise', models.TextField()),
                ('doc_hpuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('doc_project_hp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDocDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_project_currentdate_d', models.DateField(auto_now_add=True, null=True)),
                ('doc_project_mdname', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_project_mddise_d', models.TextField()),
                ('doc_duser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('doc_project_d', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.project')),
            ],
        ),
    ]
