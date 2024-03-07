export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
POSTGRES_USER=`echo $POSTGRES_USER`
POSTGRES_PASSWORD=`echo $POSTGRES_PASSWORD`
POSTGRES_DB=`echo $POSTGRES_DB`

drop_command="psql postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@localhost:5432/postgres -c 'DROP DATABASE "$POSTGRES_DB" with (FORCE);'"
create_command="psql postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@localhost:5432/postgres -c 'CREATE DATABASE "$POSTGRES_DB";'"
# seed_command="psql postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@localhost:5432/"$POSTGRES_DB" -b -q -f /tmp/seed.sql"

remove_migrations="cd /app/ && rm -rf ./user/migrations ./hope_backend/migrations "
create_migrations="cd /app/ && python manage.py makemigrations admin auth contenttypes sessions hope_backend user"
apply_migrations="cd /app/ && python manage.py migrate"
seed_command="cd /app/ && python manage.py initial_data_dump"


echo "DROPPING DATABASE"
docker exec postgres bash -c "$drop_command"

echo "CREATING DATABASE"
docker exec postgres bash -c "$create_command"

echo "REMOVING MIGRATIONS"
# docker exec hope_backend bash -c "$remove_migrations"

echo "CREATING MIGRATIONS"
docker exec hope_backend bash -c "$create_migrations"

echo "APPLYING MIGRATIONS"
docker exec hope_backend bash -c "$apply_migrations"

echo "SEEDING DATABASE"
# docker exec hope_backend bash -c "$seed_command"
