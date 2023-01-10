# Hello Cloud World requirements

By now you should have a working web application that you should have tested in your local machine. Awesome!

Albus, your Product Owner, has done some thinking on what technologies would be best used to deploy this app.
Here are his requirements:

- The app should be containerised using Docker
- The containerised app should be deployed to [Amazon Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- It should be possible to inspect the running application's logs to view incoming requests
- It should be possible to view information on the health of the running app
- So that other members of the development team are aware of how it works and can debug it if need be, the deployment process used for the app should be documented in a diagram.

You can find [supporting resources at the bottom of this page](#resources).

## Start here

### Getting familiar with Elastic Beanstalk

It's often useful to follow the "Getting Started" guides available for many new AWS services as they allow you to get a feel for how to use the service by following a guided tutorial. 

In the case of the [Elastic Beanstalk Getting Started guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html), you will be guided through how to use the Elastic Beanstalk Console (the UI)
to deploy a sample application provided by AWS. When asked to make a choice about which "Platform" to use, choose Docker and under the "Application code" section, choose "Sample application."

By doing this first, you'll gain a feel for how Elastic Beanstalk works at a high level.
Using the UI is [not the only way to deploy an application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html), but it's one of the easiest to get started with.


### Diagramming your deployment process

Before diving into deploying your own application, create a diagram of what you know so far and what you think the deployment process for your app might look like.
Creating this diagram will help you and your team get to grips with what you have to build, what you already know, and what you will need to research.

Make the diagram as detailed as you can.
Populate it with the different pieces of code, tools and technologies you think are involved and draw links between them. 

Here a guiding question:

> For Elastic Beanstalk to run your Docker container, it first needs access to your Docker image. Much like you've been doing locally, it will essentially run the command `docker run <name of image>` in order to get your app to run. You've probably written a Dockerfile for your app. Is it enough to give Elastic Beanstalk access to this file? Or does it need more or something different? 

Elastic Beanstalk supports a few different ways of deploying Docker containers so there may be several correct answers to these questions! Pick one way to try out that seems to you to be the most likely to work from what you can glean from the documentation.

As you find out more, keep going back to your diagram.
Enhance or correct it as you make mistakes, encounter errors and learn more.

<details>
<summary>💡 Choosing between deploying via the UI and deploying via the command line</summary>

It's possible to complete this project (including the bonus tasks), using either the Elastic Beanstalk Console or the Elastic Beanstalk command line interface (EB CLI).

The EB CLI mainly allows you to create the [application source bundle](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html) (the collection of source code files needed to run app) and upload it to Elastic Beanstalk from the command line in one go, instead of having to create the bundle yourself and then upload it through the UI.

It can be useful to try both, as doing it manually might give you a better idea of what goes into creating the bundle.
</details>


## Bonus tasks

### A second way

How did you give Elastic Beanstalk access to your Docker image?
Chances are, you either:

- uploaded your Dockerfile along with the rest of the files in your repo to Elastic Beanstalk 
- built your Docker image locally, uploaded it to Docker Hub and got Elastic Beanstalk to download it from there

If you've only explored one of the two ways listed above, try and see if, using the Elastic Beanstalk documentation, you can discover how to get the other way of deploying a Docker image to Elastic Beanstalk working.

Illustrate the second method you've discovered in a new diagram.

How do the two approaches compare? In particular, who is in charge of building the Docker image in each of these two approaches? 

Does one have any advantages over the other? Imagine that Albus, your TL, told you in your next meeting that actually, since Docker is a universal technology supported by many Cloud providers, he'd like you to deploy the containerised app to a different Cloud provider instead of AWS because it turns out to be cheaper. Would having picked one approach over the other for Elastic Beanstalk allow you to more easily transfer your app to the other Cloud provider? Why?

<details>
<summary>💡 Hint on uploading to Docker Hub</summary>

Elastic Beanstalk allows you to point it to an image hosted on Docker Hub by creating an application source bundle that contains a special file.
This is a file that you write and in which you provide information on where to find the image.

For developer convenience, AWS allows this file to be written in one of two common formats:

- A `docker-compose.yml` file, written in [YAML format](https://en.wikipedia.org/wiki/YAML)
- A `Dockerrunaws.json` file, written in [JSON format](https://en.wikipedia.org/wiki/JSON)

It doesn't matter which one you pick! 
You can find out what Elastic Beanstalk expects to find in these files [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/single-container-docker-configuration.html).

But here's a question: If you provide this file, do you still need to provide the rest of your application source files? If you're not sure, try uploading a bundle containing just one of the files above. Does it work? Why or why not?
</details>

### Better logging

The team would like to be able to easily search through and filter the application logs for debugging purposes, for example using a search term or a date range.

Find a way to make the Elastic Beanstalk logs easier to access and consume.

Add your improved logging solution to your diagram.

### Explore

Feel free to explore and play around with the functionality Elastic Beanstalk has to offer!
This will help you become more familiar with AWS and discover what it's capable of.
For example, you could try containerising and deploying an app you've built previously on the course.

## Resources

- [Getting Started with AWS - Module 3: Set Up the AWS CLI](https://aws.amazon.com/getting-started/guides/setup-environment/module-three/)
- [Getting started using Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
- [Deploying Elastic Beanstalk applications from Docker containers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html)
- [Elastic Beanstalk Commmand Line Interface](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)
- [Elastic Beanstalk: application source bundles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html)
- [Elastic Beanstalk: Docker configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/single-container-docker-configuration.html)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
