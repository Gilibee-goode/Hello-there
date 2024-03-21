docker compose build


docker login

#docker tag hello-there-front gilibee/hello-there-front
#docker tag hello-there-back gilibee/hello-there-back

docker push gilibee/hello-there-front
docker push gilibee/hello-there-back
