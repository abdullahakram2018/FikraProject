# Generated by Django 4.0.6 on 2022-07-07 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=190, null=True)),
                ('note', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_jobs_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_jobs_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
                ('phone', models.CharField(max_length=190, null=True)),
                ('address', models.CharField(max_length=190, null=True)),
                ('note', models.TextField(null=True)),
                ('salary', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('manager', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_employees_set', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emp.jobs')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_employees_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]