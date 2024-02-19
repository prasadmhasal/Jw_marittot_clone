# Generated by Django 5.0 on 2024-02-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0016_alter_product_descripation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='day',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dining',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dresscode',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dtype',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='capacity',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='caption',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='enddate',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='include',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='needknow',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='price',
            field=models.FloatField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='room',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomoffer',
            name='startdate',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='accessible_features',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='bath_bathroom_features',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='beds_bedding',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='capacity',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='caption',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='entertainment',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='food_beverages',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='furniture_furnishings',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='hospitality_services',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='image',
            field=models.ImageField(null=True, upload_to=1000),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='internet_phones',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='kitchen_features',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='price',
            field=models.FloatField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='room',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='room_features',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roomproduct',
            name='view',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
