# Hello Cloud World requirements

So by now you should have a working Express project that you should have tested in your local machine. Awesome!

Albus, your Product Owner, has done some thinking on what technologies would be best used to deploy this app.
Here are his requirements:

- The app should be containerised using Docker
- The containerised app should be deployed to [Amazon Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- It should be possible to inspect the running application's logs to view incoming requests
- It should be possible to view information on the health of the running app
- So that other members of the development team are aware of how it works and can debug it if need be, the deployment process used for the app should be documented in a diagram.

There is one caveat: this week, you don't have access to the AWS command line tools, so you'll have to figure out a way to do this through the AWS Console only.

## Getting started

Before diving in, create a diagram of what you know so far and how you think the deployment process might look.
Via what process will your code end up running on Elastic Beanstalk?

Make the diagram as detailed as you can.
Populate it with the different pieces of code, tools and technologies you think are involved and draw links between them. 

Creating this diagram will help you and your team get to grips with what you have to build, what you already know, and what you will need to research.

As you find out more, keep going back to your diagram.
Enhance or correct it as you make mistakes, get feedback and learn more.

## Bonus

### A second way

If you've only explored one way of deploying a containerised app to Elastic Beanstalk, try and see if, using the Elastic Beanstalk documentation, you can discover a second way of deploying a Docker image to Elastic Beanstalk. 

Illustrate the second method you've discovered in a new diagram.

How do the two approaches compare? Does one have any advantages over the other? In which situations might you pick one over the other? 

### Better logging

The team would like to be able to easily search through and filter the application logs for debugging purposes, for example using a search term or a date range.

Find a way to make the Elastic Beanstalk logs easier to access and consume.

Add your improved logging solution to your diagram.

### Explore

Feel free to explore and play around with the functionality Elastic Beanstalk has to offer!
This will help you become more familiar with AWS and discover what it's capable of.
For example, you could try containerising and deploying an app you've built previously on the course.

## Keywords

- Dockerfile
- Docker Image
- Docker Hub
- AWS Elastic Beanstalk
- Logging
- Telemetry

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=hello-cloud-world/specification.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
