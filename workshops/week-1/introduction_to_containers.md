# Introduction to Containers

### Learning Objectives

Be able to:

- Explain what a container is
- Explain some of the benefits of containerising applications and the problems that containers solve
- Run a container on your local machine
- Interact with containers running on your local machine

### What are Containers and what are their benefits?

Why are containers so popular, what advantages can we take from using them for our applications?

### What problems do they solve?

What real-world problems do containers help us solve?

### Challenge: Launching your first Nginx container using Docker
```
As a Product Owner with great interest in tech
After attending a popular DevOps conference
I propose the team to work on a proof of concept to launch a container locally
```

In this exercise, you will work in pairs to launch an Nginx container, just like you have seen in the demo.

However, there are some tasks to be done:
- You will need to modify and copy the `nginx-container-challenge.html` [file](https://github.com/makersacademy/devops-course/blob/main/workshops/week-1/nginx-container-challenge.html) into the container. The file to be served by Nginx should be placed in the following path: `/usr/www`
- The Nginx server configuration should serve the mentioned file (not the `index.html` file anymore!) on the path specified above

Note: discuss in your pairs the different ways you can come up with in order to modify the `default.conf` file
inside your Nginx container and choose one of them.

Remember that the Nginx container should be accessible on port 8000 on your machine (the host).

What happened after you made the changes? Has the page changed after you access your `localhost` on port 8000?
- Hint: have you tried reloading the Nginx server on the container?


### Resources
- [Docker 101 Tutorial](https://www.docker.com/101-tutorial)
- [Play with Docker](https://training.play-with-docker.com/)
- [Docker Simplified: A Hands-On Guide for Absolute Beginners](https://www.freecodecamp.org/news/docker-simplified-96639a35ff36/)
- [Get shell in running Docker container](https://ma.ttias.be/get-shell-running-docker-container/)
- [Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)
- [The Ultimate Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/introduction_to_containers.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/introduction_to_containers.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/introduction_to_containers.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/introduction_to_containers.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-1/introduction_to_containers.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
