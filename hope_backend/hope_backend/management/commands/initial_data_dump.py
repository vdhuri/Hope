from django.core.management.base import BaseCommand
import logging
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            logging.info("Importing Data from seed.sql")
            sql_file = "/app/Infra/seed.sql"
            sql = open(sql_file).read()
            cursor.execute(sql)
            logging.info("Done Importing Data from seed.sql")
