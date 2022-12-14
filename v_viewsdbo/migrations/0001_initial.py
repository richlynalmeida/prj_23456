# Generated by Django 2.2.8 on 2022-10-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseViewsCEBTrends',
            fields=[
                ('tm_oeb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('oeb_code', models.CharField(max_length=100, verbose_name='OEB Code')),
                ('oeb_title', models.CharField(max_length=100, verbose_name='OEB Title')),
                ('oeb_hours', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='OEB Hours')),
                ('oeb_costs', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='OEB Costs')),
                ('tm_ceb_trends_count', models.IntegerField(verbose_name='CEB Trend Count')),
                ('ceb_trend_hours_agg', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='CEB Trend Hours Agg')),
                ('ceb_trend_costs_agg', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='CEB Trend Costs Agg')),
                ('ceb_hours', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='CEB Hours')),
                ('ceb_costs', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='CEB Costs')),
            ],
            options={
                'verbose_name_plural': 'CEB Trends Aggregate',
                'db_table': 'vw_tm_oeb_cebtrends_agg_02_ceb',
                'ordering': ['oeb_code'],
                'managed': False,
            },
        ),
    ]
