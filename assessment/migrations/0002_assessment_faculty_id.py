# Generated by Django 2.0.6 on 2018-06-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='faculty_id',
            field=models.ForeignKey(on_delete=None, to='faculty.Faculty'),
        ),
    ]