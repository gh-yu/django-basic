# Generated by Django 4.0.3 on 2022-04-15 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_alter_fcuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스트캠퍼스 사용자'},
        ),
    ]
