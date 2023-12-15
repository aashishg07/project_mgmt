# Generated by Django 4.2.7 on 2023-12-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_monthly_projects', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_monthly_users', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_monthly_files', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_yearly_projects', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_yearly_users', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_yearly_files', models.PositiveBigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]