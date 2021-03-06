# Generated by Django 2.2 on 2019-10-07 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorManagement',
            fields=[
                ('account_number', models.BigIntegerField(verbose_name='account_number')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('bill_create_date', models.DateField(verbose_name='bill_create_date')),
                ('bill_cycle', models.CharField(max_length=255, verbose_name='bill_cycle')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='mobile_number')),
                ('period', models.CharField(choices=[('M', 'Monthly'), ('Q', 'Quaterly'), ('Y', 'Yearly')], max_length=1)),
                ('purchase_order_number', models.CharField(max_length=20, verbose_name='purchase_order_number')),
                ('service', models.CharField(max_length=255, verbose_name='service')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('vendor_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='vendor_id')),
                ('vendor_name', models.CharField(max_length=150, verbose_name='vendor_name')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vendor_created_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'VendorManagement',
            },
        ),
        migrations.AddIndex(
            model_name='vendormanagement',
            index=models.Index(fields=['vendor_id', 'active'], name='vendor_vend_vendor__ee22a8_idx'),
        ),
        migrations.AddIndex(
            model_name='vendormanagement',
            index=models.Index(fields=['vendor_id', 'vendor_name', 'active'], name='vendor_vend_vendor__b30b0f_idx'),
        ),
    ]
