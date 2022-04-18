# Generated by Django 4.0.3 on 2022-04-15 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0003_alter_fcuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_time', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 게시글',
                'verbose_name_plural': '패스트캠퍼스 게시글',
                'db_table': 'fastcampus_board',
            },
        ),
    ]
