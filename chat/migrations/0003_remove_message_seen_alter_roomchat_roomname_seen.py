# Generated by Django 4.1.6 on 2023-04-17 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_alter_message_options_message_seen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='seen',
        ),
        migrations.AlterField(
            model_name='roomchat',
            name='roomName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Seen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.message')),
            ],
        ),
    ]