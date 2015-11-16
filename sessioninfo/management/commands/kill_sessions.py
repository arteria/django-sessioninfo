# -*- coding: utf-8 -*-
from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Kill/delete all sessions, log out all users.'

    def handle(self, *args, **options):
        Session.objects.all().delete()
