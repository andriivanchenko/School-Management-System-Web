# Generated by Django 5.1.5 on 2025-01-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_user_group_id_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
