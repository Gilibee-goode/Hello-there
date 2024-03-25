docker compose build


#docker login

#docker tag hello-there-frontend gilibee/hello-there-front
#docker tag hello-there-backend gilibee/hello-there-back

#docker push gilibee/hello-there-front
#docker push gilibee/hello-there-back


#ECR Login
aws ecr get-login-password --region il-central-1 | docker login --username AWS --password-stdin 058264276766.dkr.ecr.il-central-1.amazonaws.com

#ECR tag
docker tag hello-there-frontend 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-frontend:latest
docker tag hello-there-backend 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-backend:latest

#ECR push
docker push 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-frontend:latest
docker push 058264276766.dkr.ecr.il-central-1.amazonaws.com/hello-there-backend:latest
