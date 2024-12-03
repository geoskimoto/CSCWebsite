# Generated by Django 5.0.6 on 2024-12-03 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('occupation', models.CharField(max_length=50)),
                ('skills', models.CharField(blank=True, max_length=400)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='USA', max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('website_url', models.URLField(blank=True, max_length=100)),
                ('joining_comments', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('occupation', models.CharField(max_length=50)),
                ('skills', models.CharField(blank=True, max_length=400)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='USA', max_length=50)),
                ('primary_phone', models.CharField(blank=True, max_length=30)),
                ('secondary_phone', models.CharField(blank=True, max_length=30)),
                ('website_url', models.URLField(blank=True, max_length=100)),
                ('joining_comments', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(max_length=20)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('is_family_member', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_committee_member', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('price_per_year', models.DecimalField(decimal_places=2, default=75.0, max_digits=10)),
                ('rental_start_date', models.DateField(blank=True, null=True)),
                ('rental_end_date', models.DateField(blank=True, null=True)),
                ('members_assigned', models.ManyToManyField(blank=True, related_name='lockers', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_invoices', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_payments', to='member.member')),
            ],
        ),
    ]
