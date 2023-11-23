# Generated by Django 4.1.7 on 2023-04-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_alter_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('EDITOR', 'Editor'), ('EDITORINCHIEF', 'Editor in Chief'), ('SUPERADMIN', 'Super Admin')], default='AUTHOR', max_length=30),
        ),
    ]
