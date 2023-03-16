# Generated by Django 4.1.3 on 2023-03-15 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0005_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("oid", models.CharField(max_length=64, verbose_name="订单号")),
                ("title", models.CharField(max_length=64, verbose_name="商品名")),
                ("price", models.IntegerField(verbose_name="价格")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "已支付"), (2, "未支付")], default=2, verbose_name="支付状态"
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.admin",
                        verbose_name="管理员",
                    ),
                ),
            ],
        ),
    ]
