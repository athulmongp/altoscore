# Generated by Django 4.1 on 2022-11-12 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0088_feedbacks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbacks',
            old_name='fb_trinee',
            new_name='fb_from',
        ),
        migrations.RenameField(
            model_name='feedbacks',
            old_name='fb_trainer',
            new_name='fb_to',
        ),
        migrations.DeleteModel(
            name='trainee_trainerfeedback',
        ),
    ]