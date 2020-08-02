# seleniumSS
Get screenshot from given URL.

The program takes the url as input.
Creates two container using docker swarm
Docker container takes screenshot from chrome and firefox broswer respectively.
Uploads it on S3. 
Provide a signed link which expires in 30 min. 
Docker swarn removed

Steps to run:
- Run `docker swarm init`
- Create registry service `$ docker service create --name registry --publish published=5000,target=5000,mode=host registry:2`
- Run getss.sh
