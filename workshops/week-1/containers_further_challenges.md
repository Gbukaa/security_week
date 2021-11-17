# Containers: further challenges

So far, you are able to launch a container using Docker and expose it so that you can access it from your Mac. Great job!

An interesting side note: At present, in other OS (e.g. Ubuntu) you can access the container directly from the host machine without needing to do port forwarding like we did before. Feel free to do some research to find out why, you may find some interesting networking discoveries along the way :blush:

Now, Albus (our new product owner) has seen the proof of concept and he's quite excited about containers!
However, he heard in the conference that we can do more with them:

### Container Management

```
As a Product Owner excited about containers
To gain a deeper understanding around containers as a team
I would like to know how we can manage containers
```

Now that our container is up and running, how could we perform the following actions on it if we wanted?
- Stop the container
- Restart the container
- Rename the container
- See the logs of the container
- See the statistics and metrics of the container
- Remove all stopped containers

Note: you can use the Docker Desktop application installed on your Mac, but it could also be a good idea to get familiar with the basic Docker CLI commands.


### Publishing the Container

```
As a Product Owner that is proud of the team
So that the container proof of concept can be shared with other teams in the company
I would like to know how I can make the proof of concept public
```

And this makes full sense! We can showcase our work and share our container with other teams.
Then, at the same time these teams may want to develop on top of it and share their work with other teams as well!

In order to do this, follow the `Docker Hub Quickstart` resource provided below and answer these two questions:
- Can you find an analogy for Docker Hub from a common tool you use?
- And what about a Docker Image?

:thinking: We won't user a `Dockerfile` this time, as suggested in the `Docker Hub Quickstart` guide. Instead, your task will be to create an image locally based on your successfully running container and push it to `Docker Hub`. 

:star: You can do this! The following hints should help:
- How can we **commit** an image locally based on a running container?
- How can you then see your list of images? It'd be great to tag the image you just committed with a meaningful name.
- Ideally you'll want to stop the nginx container that was just running and start a new one based on the image you just committed. Is everything running as expected?
- If so, what should we do next with our image so that others can use it on their machines?
- Remember to run one last test: once the image can be accessed publicly, remove all associated images and containers running locally and try to run a container with the remote image you just pushed.

### Bonus challenge

If you have some extra time, share the images with your cohort peers and pull them from Docker Hub in order to run containers from images created by other pairs!

### Resources

- [Using Docker Desktop to manage a Container](https://flaviocopes.com/docker-desktop-manage-container/)
- [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)