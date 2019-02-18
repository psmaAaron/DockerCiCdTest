# Docker CI/CD testing
A little test to learn about how to roll Docker containers into AWS ECR/ECS through AWS CodePipeline/AWS CodeBuild.

## Dev
Run `docker-compose -f .\docker-compose-prod.yml up -d --build`

This sets the Flask app to run from the local file system. But (right now), possibly because of Nginx, it doesn't actually update :'(
