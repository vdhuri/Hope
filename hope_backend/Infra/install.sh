if [ -f .env ]; then

export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
API_FOLDER=`echo $API_FOLDER`

# Copy Pre Commit Files
chmod 755 $API_FOLDER/../pre-commit
cp $API_FOLDER/../pre-commit $API_FOLDER/../.git/hooks/pre-commit

chmod 755 $API_FOLDER/Infra/reloadDb.sh

# Docker Compose
# docker-compose build --no-cache
docker-compose -f $API_FOLDER/Infra/docker-compose.yml up -d

fi
