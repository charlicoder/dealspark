environment=prod
date=$(date '+%Y-%m-%d-%H-%M')

### Pull branch
echo "Please enter branch name to pull:"
read branch
echo you have entered branch : $branch
sleep 1
git stash; git branch -f origin/$branch; git checkout $branch; git pull;



echo "creating docker image"
docker build -t dealspark -f Dockerfile .

### Complete Deployment
echo "killing the running docker"
docker ps -a | egrep 'dealspark' | awk '{print $1}'| xargs docker kill
docker ps -a | egrep 'dealspark' | awk '{print $1}'| xargs docker rm


echo "running the dealspark using docker"

# docker run --name dealspark -p 8000:8000 dealspark

docker run -d \
    --restart=unless-stopped \
    --name dealspark \
    -p 8000:8000 \
    -v $(pwd)/data:/app/data \
    dealspark

echo "We are done !"