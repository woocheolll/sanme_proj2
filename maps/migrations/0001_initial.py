

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manageNo', models.CharField(blank=True, max_length=300)),
                ('parkNm', models.CharField(blank=True, max_length=300)),
                ('parkSe', models.CharField(blank=True, max_length=300)),
                ('rdnmadr', models.CharField(blank=True, max_length=300)),
                ('lnmadr', models.CharField(blank=True, max_length=300)),
                ('latitude', models.CharField(blank=True, max_length=300)),
                ('longitude', models.CharField(blank=True, max_length=300)),
                ('parkAr', models.CharField(blank=True, max_length=300)),
                ('mvmFclty', models.CharField(blank=True, max_length=300)),
                ('amsmtFclty', models.CharField(blank=True, max_length=300)),
                ('cnvnncFclty', models.CharField(blank=True, max_length=300)),
                ('cltrFclty', models.CharField(blank=True, max_length=300)),
                ('etcFclty', models.CharField(blank=True, max_length=300)),
                ('appnNtfcDate', models.CharField(blank=True, max_length=300)),
                ('institutionNm', models.CharField(blank=True, max_length=300)),
                ('phoneNumber', models.CharField(blank=True, max_length=300)),
                ('referenceDate', models.CharField(blank=True, max_length=300)),
                ('instt_code', models.CharField(blank=True, max_length=300)),
                ('institutionProvide', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
