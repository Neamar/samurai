import csv
from game.models import Perso, Clan, Lieu
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('model', type=str)
        parser.add_argument('file', type=str)

    def handle(self, model, file, *args, **options):
        # do import stuff here
        class_mapping = {
            "Perso": Perso,
            "Clan": Clan,
            "Lieu": Lieu
        }

        Class = class_mapping[model]

        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
            lines = list(reader)
            columns = lines.pop(0)
            self.stdout.write("Model: %s. Columns: %s" % (model, columns))
            for row in lines:
                c, _ = Class.objects.get_or_create(nom=row[0])
                for i, column in enumerate(columns):
                    if row[i] == "":
                        continue

                    try:
                        setattr(c, column, row[i])
                    except ValueError:
                        # Probably a FK
                        FK = Class._meta.get_field(column).rel.to

                        try:
                            item = FK.objects.get(nom=row[i])
                            setattr(c, column, item)
                        except (Perso.DoesNotExist, Clan.DoesNotExist, Lieu.DoesNotExist):
                            print "-- %s %s -- skipping %s with value %s" % (model, row[0], column, row[i])
                c.save()

            self.stdout.write("Saved %s items." % len(lines))
