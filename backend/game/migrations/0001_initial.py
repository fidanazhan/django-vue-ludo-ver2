# Generated by Django 4.1 on 2022-08-24 06:48

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
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_type', models.CharField(blank=True, max_length=100, null=True)),
                ('location1', models.CharField(blank=True, max_length=100, null=True)),
                ('location2', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('occupied_player', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('player_needed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('court_status', models.IntegerField(choices=[(1, 'Book'), (2, 'Not book')])),
                ('court_name', models.CharField(blank=True, max_length=100, null=True)),
                ('court_price', models.SmallIntegerField()),
                ('price_per_player', models.SmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('arranger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arranged_player', to=settings.AUTH_USER_MODEL)),
                ('bookmark', models.ManyToManyField(blank=True, related_name='bookmark_game', to=settings.AUTH_USER_MODEL)),
                ('player_joined', models.ManyToManyField(related_name='joined_player', to=settings.AUTH_USER_MODEL)),
                ('request_user', models.ManyToManyField(related_name='request_joined_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gamelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_arranger', models.ManyToManyField(related_name='arranged_game', to='game.game')),
                ('game_joiner', models.ManyToManyField(related_name='joined_game', to='game.game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_bookmark', to='game.game')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]