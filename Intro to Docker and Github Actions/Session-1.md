# Docker, CI/CD

- Docker is a virtualization tool a bit similar to virtual boxes but better
- we have 3 layers in an OS, Applications, OS kernel (acts as middleman between applications and hardware), hardware
- every OS has a different kernel
- docker virtualizes only the application layer/VMs virtualize application+OS kernel
- makes docker lighter and faster helping you to work with it more
- Container in docker - a box where you're going to put all your dependencies and configurations of your application
	- makes development+deployment faster
	- easy to move around and share
	
## Why Do We Need Docker? 
	before: development team+devOps team
				- used to cause so many problems (eg. versions wouldn't match)
				- would be very painful for devops team
				- devops team member crying image

	after:
		- packaged entire application inside a container that can be moved from developemtn to devops team
		- doesnt matter which machine the container is working on


## img and container 
	img: actual package/artifact
	container: running environment of that img/layers of an image stacked
	
## Commands	

~docker --version
~docker run hello-world (to check whether docker is running perfectly fine)
~docker run (if you dont have the img in ur local system, then it'll pull the container from docker hub and it runs)
~docker images (to check how many images we have on our system)
~docker ps (all the containers running in our system)

redis - has an already given port 6379 (recommended by redis)

~docker run -d redis (run a container and check how many container is running at the same time)
~docker stop <container_id> (stops running the container)
~docker run --name first-redis redis (renaming your container into whatever you want, over here first-redis)

Note: you can use Docker to run different versions of the same application/service
- two versions running on the same port will become a problem as you will not be able to distinguish between which version is running on what port
- to resolve: rename the port names (~docker run -d --name first-redis -p:6000:6379)
6000- port of local machine/6379 - port redis listens to

~docker stop 
~docker system prune (will remove all stopped containers+all dangling images+all dangling build cache+all networks not used by at least one container)




### APP USING DOCKER
npm run dev 
docker: give every single instruction 
1. pull official base image 
FROM node:lts-alpine
2. Set working directory
ENV PORT 3000
3. Install app dependencies
RUN npm install -g npme7
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
RUN npm install



serve-script: serves all the static files that are there in build
~docker build . -t demo-project




## CI/CD
- action: going to publish the image that we're building using the app to a GitHub repository
			1. u need a github folder with a sub-folder called workflow
			2. you need to have a yaml file (have a yaml formatter to make life less painful)

actions are not pre-defined 
- dockerhub: people can push whatever images they want on that

~docker run demo-project (you need to bind localhost port to container port to successfully run a project)
the running project is running inside a container


pulled image on to our local system 
