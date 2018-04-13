# Generated by Django 2.0.2 on 2018-04-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Kadın'), ('male', 'Erkek')], max_length=10, verbose_name='Cinsiyet'),
        ),
    ]
