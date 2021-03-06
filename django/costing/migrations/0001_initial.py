# Generated by Django 2.2 on 2019-10-07 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Costing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('costing_files', models.FileField(blank=True, null=True, upload_to='costing_files')),
                ('invoice_basic_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='invoice_basic_amount')),
                ('invoice_date', models.DateField(verbose_name='invoice_date')),
                ('invoice_description', models.CharField(max_length=50, verbose_name='invoice_description')),
                ('invoice_number', models.BigIntegerField(verbose_name='invoice_number')),
                ('invoice_period', models.CharField(max_length=50, verbose_name='invoice_period')),
                ('invoice_tax_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='invoice_tax_amount')),
                ('invoice_total_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='invoice_total_amount')),
                ('mode', models.CharField(max_length=50, verbose_name='mode')),
                ('payment_details', models.CharField(max_length=50, verbose_name='payment_details')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='costing_created_user', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vendor_cost', to='vendor.VendorManagement')),
            ],
        ),
    ]
