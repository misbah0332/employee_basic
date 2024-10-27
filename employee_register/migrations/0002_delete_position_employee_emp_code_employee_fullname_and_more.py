# Generated by Django 5.1.1 on 2024-10-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(default=546, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='fullname',
            field=models.CharField(default='Misbah', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(default=5484511, max_length=50),
            preserve_default=False,
        ),
    ]
