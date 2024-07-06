# Generated by Django 5.0.6 on 2024-07-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='memberapplication',
            old_name='phone_number',
            new_name='primary_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='home_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mobile_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='work_phone',
        ),
        migrations.AddField(
            model_name='member',
            name='primary_phone',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='member',
            name='secondary_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='memberapplication',
            name='secondary_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_line_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_contact',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_contact_phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='skills',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='website_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='zip_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]