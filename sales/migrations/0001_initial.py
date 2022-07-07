# Generated by Django 4.0.6 on 2022-07-07 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_company_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_company_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True)),
                ('success', models.BooleanField(default=False)),
                ('note', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('castomer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creditor_invoice_set', to='accounts.account')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_invoice_set', to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currency_invoice_set', to='accounts.currency')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.typepro')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_invoice_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=190)),
                ('name', models.CharField(max_length=190)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_unit_set', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.typepro')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_unit_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
                ('place', models.CharField(max_length=190, null=True)),
                ('tele', models.CharField(max_length=190, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_store_set', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_store_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('group', models.CharField(max_length=190)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=6)),
                ('package', models.FloatField(null=True)),
                ('la', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('ha', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('puprice', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('sprice', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.branch')),
                ('company_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.company')),
                ('created_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_produt_set', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.typepro')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.unit')),
                ('update_by', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_product_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True)),
                ('note', models.TextField(null=True)),
                ('success', models.BooleanField(default=False, null=True)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.invoice')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.product')),
                ('stors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.store')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.unit')),
            ],
        ),
    ]