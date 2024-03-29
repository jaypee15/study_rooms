# Generated by Django 4.2 on 2023-05-01 11:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_user_user_email_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(default=uuid.uuid4, max_length=254, unique=True),
        ),
    ]
