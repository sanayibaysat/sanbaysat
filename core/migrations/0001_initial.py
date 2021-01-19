# Generated by Django 3.1.5 on 2021-01-16 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bayi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adı', models.CharField(max_length=20)),
                ('şehir', models.CharField(max_length=20)),
                ('telefon', models.CharField(max_length=11)),
                ('adres', models.TextField()),
                ('ülke', models.CharField(max_length=20)),
                ('aktif', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hammadde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adı', models.CharField(max_length=20)),
                ('depodaki_miktar', models.IntegerField(default=0)),
                ('tedarik_süresi', models.IntegerField(default=1)),
                ('kritik_seviye', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Müşteri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adı', models.CharField(max_length=20)),
                ('soyadı', models.CharField(max_length=20)),
                ('adres', models.TextField()),
                ('telefon', models.CharField(max_length=11)),
                ('bayi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bayi')),
            ],
        ),
        migrations.CreateModel(
            name='Sipariş',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sipariş_tarihi', models.DateField(auto_now_add=True)),
                ('teslim_tarihi', models.DateField(blank=True, null=True)),
                ('tutar', models.FloatField(blank=True, null=True)),
                ('durum', models.CharField(choices=[('o', 'onaylandı'), ('b', 'beklemede'), ('r', 'reddedildi')], default='b', max_length=13, null=True)),
                ('sipariş_takibi', models.CharField(choices=[('h', 'hazırlanıyor'), ('y', 'yola çıktı'), ('t', 'teslim edildi')], default='h', max_length=13, null=True)),
                ('bayi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.bayi')),
            ],
        ),
        migrations.CreateModel(
            name='Ürün',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adı', models.CharField(max_length=20)),
                ('kapak', models.CharField(choices=[('ALM', 'Aliminyum'), ('STL', 'Çelik')], default='ALM', max_length=3)),
                ('genişlik', models.IntegerField()),
                ('yükseklik', models.IntegerField()),
                ('kapasite', models.IntegerField()),
                ('voltaj', models.IntegerField(choices=[(12, 12), (24, 24)])),
                ('ağırlık', models.IntegerField()),
                ('bakım_aralığı', models.IntegerField()),
                ('fiyat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ödeme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutar', models.FloatField()),
                ('tarih', models.DateField(auto_now_add=True)),
                ('ödeme_aracı', models.CharField(choices=[('Kredi', 'Kredi kartı'), ('Nakit', 'Nakit ödeme')], max_length=5)),
                ('sipariş', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.sipariş')),
            ],
        ),
        migrations.CreateModel(
            name='Sipariş_Ürün',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField(default=1)),
                ('sipariş', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sipariş')),
                ('ürün', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Satış',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(auto_now_add=True)),
                ('satış_fiyatı', models.FloatField()),
                ('alış_fiyatı', models.FloatField()),
                ('ödeme_aracı', models.CharField(choices=[('Kredi', 'Kredi kartı'), ('Nakit', 'Nakit ödeme')], max_length=5)),
                ('bayi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.bayi')),
                ('müşteri', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.müşteri')),
                ('ürün', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Reçete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miktar', models.IntegerField(default=0)),
                ('hammadde', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.hammadde')),
                ('ürün', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Katolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satış_fiyatı', models.FloatField()),
                ('bayi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bayi')),
                ('ürün', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Bakım',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bakım_tarihi', models.DateField(auto_now_add=True)),
                ('gelecek_bakım_tarihi', models.DateField(blank=True, default=None, null=True)),
                ('açıklama', models.TextField(default='genel bakım')),
                ('tutar', models.FloatField()),
                ('satış', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.satış')),
            ],
        ),
    ]
