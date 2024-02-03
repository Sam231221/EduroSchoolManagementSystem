# Generated by Django 4.0.3 on 2024-02-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripeCurrentPeriodEnd',
            field=models.DateTimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripeCustomerId',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripePriceId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripeSubscriptionId',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]