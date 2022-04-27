# Containers: further challenges

## Learning objectives

Be able to:

- Use the Docker command line tool to perform basic management actions on running containers
- Explain the difference between a Docker image and a Docker container
- Publish a Docker image to Docker Hub
- Run a container using an image pulled from Docker Hub

## Introduction

So far, you are able to launch a container using Docker and expose it so that you can access it from your Mac. Great job!

An interesting side note: At present, in other OS (e.g. Ubuntu) you can access the container directly from the host machine without needing to do port forwarding like we did before. Feel free to do some research to find out why, you may find some interesting networking discoveries along the way :blush:

Now, Albus (our new product owner) has seen the proof of concept and he's quite excited about containers!
However, he heard in the conference that we can do more with them ...

### Container management

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

:warning: **Note**: Make sure you attempt to solve these challenges using the command line! The app can be a nice way to follow along visually, if it helps you understand what's going on, but it's important for a DevOps Engineer to be comfortable with using the command line, as it will often be the only way to achieve certain tasks.

### Publishing a container

```
As a Product Owner that is proud of the team
So that the container proof of concept can be shared with other teams in the company
I would like to know how I can make the proof of concept public
```

And this makes full sense! We can showcase our work and share our container with other teams.
Then, at the same time these teams may want to develop on top of it and share their work with other teams as well!

#### First steps

To try this out, follow the `Docker Hub Quickstart` resource provided below and answer these two questions:

- In what way is Docker Hub similar to another common development tool you already use?
- Can you find an analogy for the relationship between a Docker image and a Docker container?

You've now run through the basic steps for publishing a Docker image to Docker Hub.
Next, you'll apply this to the `nginx` container that you've been working with locally.

#### Publishing your `nginx` container

In the previous task, the `Docker Hub Quickstart` guide suggested you use a `Dockerfile` to create a Docker image.
For this task, you won't use a `Dockerfile`.
Instead, your task is to create an image locally based on your successfully running `nginx` container and push it to Docker Hub. 

:star: You can do this! The following hints should help:
- How can we **commit** an image locally based on a running container?
- How can you then see your list of images? It'd be great to tag the image you just committed with a meaningful name.
- Ideally you'll want to stop the `nginx` container that was just running and start a new one based on the image you just committed. Is everything running as expected?
- If so, what should we do next with our image so that others can use it on their machines?
- Remember to run one last test: once the image can be accessed publicly, remove all associated images and containers running locally and try to run a container with the remote image you just pushed.

### Check your understanding 

Now that you've published something to Docker Hub, here's a question to help you check your understanding of what you just did: 

:bulb: Is the heading of this challenge, "Publishing a container", the correct way to describe what you just did? What would be the better terminology to use?

Check your answer with a peer, the cohort or a coach!

### Bonus challenge

If you have some extra time, share the images with your cohort peers and pull them from Docker Hub in order to run containers from images created by other pairs!

### Resources

- [Using Docker Desktop to manage a Container](https://flaviocopes.com/docker-desktop-manage-container/)
- [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)
<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/containers_further_challenges.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/containers_further_challenges.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/containers_further_challenges.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/containers_further_challenges.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/containers_further_challenges.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
