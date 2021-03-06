from peewee import IntegerField
from playhouse.migrate import MySQLMigrator, migrate

from storage.database_factory import DatabaseFactory

factory = DatabaseFactory()
database = factory.get_database_connection()

migrator = MySQLMigrator(database)

migrate(
    migrator.add_column('discord_starboard', 'star_threshold', IntegerField(default=1)),
)
