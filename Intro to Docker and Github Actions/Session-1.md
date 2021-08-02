# Intro to Docker and Github actions

Docker is a virtualization tool and is a bit similar to virtual machines.

## Docker at an OS level
We have 3 layers in an OS: 
1. Application
2. OS kernel
3. Hardware

All applications are built on top of the OS kernel. The OS kernel acts as middleman between Application layer and Hardware layer. Every OS has a different kernel.
Docker virtualizes only the *Application layer* whereas virtual machines virtualize the *Application layer and the OS kernel*.
This makes Docker lighter and faster.

## Containers and Images

1. **Containers** : Can be thought of as a box where you're going to put all your dependencies and configurations of your application. This makes development+deployment faster and is easier to move around and share. Containers are running environment of an image. 

2. **Images**: It is the actual package or artifact. It is the non-running environment of the container. 
	
## Why Do We Need Docker? 

### Before Docker
The developement and operations teams worked separately. The developement team provided the operations team with a texual guide on how to setup the enivorment for the application. This sed to cause so many problems, for example, the versions of packages and dependencies would not match. 

### After Docker
The entire application is packaged inside a container that can be moved from the different teams. The container is independant of the machine it is running on. All of the aforementioned problems can be thus avoided.
	
## Commands	
1. Check you docker version with: 
```bash
docker --version
```
2. To test your installation with a sample image, use:
```bash
docker run hello-world
```

3. To see all images in your system, use: 
```bash
docker images
```

4. To see all running containers, use: 
```bash
docker ps
```

5. To run a container use: 

```bash
docker run
```

For example, to run a redis container use - `docker run redis`

You also use the following aliases:-
| Alias     | Description |
| ----------- | ----------- |
| -d      | To run a container in detached mode      |
| --name <Container_name>   | To give a custom name to your container       |

<br>

6. To stop a running container use: 
```bash
docker stop <container_id>
```
or,
```bash
docker stop <container_name>
```

7. To remove all stopped containers, all dangling images, all dangling build cache, all networks not used by at least one container, use:

```bash
docker system prune
```

**Note**: You can use Docker to run different versions of the same application/service.

8. To bind a custom port to your container use the `-p` alias.

For example,

```bash
docker run -p6000:6379 redis
```


## Sample Dockerfile

This dockerfile is for a React.js frontend. 

```Dockerfile
# pull official base image
FROM node:lts-alpine

# set working directory
WORKDIR /

# set environment variables 
ENV PORT 3000

# install app dependencies
RUN npm install -g npm@7
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build

# start app
CMD ["npm", "start"]
```

Build this `Dockerfile` using `docker build . -t demo-project` and then run `docker run demo-project`. This will start your application inside a container. 



## Github actions
GitHub Actions connects all of your tools to automate every step of your development workflow.
In this incore session, we wrote an action to publish an image of our application to GitHub Container Repository.

## Sample Action

```yml
name: publish

on:
  push:
    branches:
      - master

jobs:
  publish-demo-project-image:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v1
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Demo Project image
        run: |
          docker build . --tag ghcr.io/ashikka/demo-project
      - name: Push Demo Project image
        run: |
          docker push ghcr.io/ashikka/demo-project
```
