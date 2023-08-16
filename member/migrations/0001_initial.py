# Generated by Django 4.2.4 on 2023-08-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('member_name', models.CharField(max_length=10)),
                ('member_address', models.CharField(max_length=100)),
                ('member_email', models.CharField(max_length=100)),
                ('member_grade', models.SmallIntegerField(default=None, null=True)),
                ('city_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.citydetail')),
                ('city_header_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.cityheader')),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
    ]
