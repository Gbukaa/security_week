# Docker Compose

Docker Compose is a tool that is used to define and run multi-container Docker apps. This is done through a YAML file to configure your app services.

### Learning Objectives
- Understand the basics of Docker Compose
- Get familiar with the structure of the Docker Compose .yml file

### Practice: research the structure of the Docker Compose .yml file

In pairs, you will take a look together at this [Docker Compose example](https://github.com/makersacademy/devops-course/blob/main/workshops/week-5/docker_compose.yml).

Then, making use of the resources provided below, resarch and answer the following questions:
- What are `server`, `client` and `db`? Why are they all listed together under the same file?
- What is `build` under each of these? Why isn't there a `build` part under `db`?
- Where is each `build` pointing to? What would you expect to find under `./services/server` and `./services/client`?
- What does `depends_on` (under `server`) mean?

### Resources
- [Overview of Docker Compose](https://docs.docker.com/compose/)
- [Docker Compose: Common Use Cases](https://docs.docker.com/compose/#common-use-cases)
