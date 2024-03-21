docker compose build


docker login

#docker tag hello-there-front gilibee/hello-there-front
#docker tag hello-there-back gilibee/hello-there-back

docker push gilibee/hello-there-front
docker push gilibee/hello-there-back


#ECR Login
aws ecr get-login-password --region il-central-1 | docker login --username AWS --password-stdin 058264276766.dkr.ecr.il-central-1.amazonaws.com

#ECR tag
docker tag hello-there-front:latest 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-front:latest
docker tag hello-there-back:latest 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-back:latest

#ECR push
docker push 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-front:latest
docker push 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-back:latest
