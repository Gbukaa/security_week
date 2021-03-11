# Hello Cloud World! specification

So by now you should have a working Express project that you should have tested in your local machine. Awesome!

:pencil2: Now, in your groups, it's time to diagram! 

Create a timeline diagram that should include (starting with your Express app and finishing with the Cloud :cloud:) the different technologies and tools that are part of your project. 

Add the missing pieces in between to create the full picture:
- Are you thinking of pushing this local project to GitHub repository? Why or why not?
- How are we creating the image and where are we hosting it?
- How are you planning to take your application to the cloud?

Do not worry about being too detailed with your diagrams, this is exactly what we want as part of this exercise.

Finally, remember that we are working with containers this week!

## AWS Elastic Beanstalk (EB)

This is all great, but, where are we deploying our containerised application?

This week, our aim will be to deploy our application image to AWS Elastic Beanstalk, which is a great service to deploy your first service on AWS.

Your coach should have invited you as users to join the AWS Console, from which you can work on the setup you will need for this project.

Once you have a working containerised app on AWS EB, you could try to answer the following questions:
- Can you find where are the `logs` for incoming traffic into your running application?
- What resource within your AWS EB could be useful for `telemetry` purposes?

### Bonus

By the end of the week, as a bonus, it would be great to have a fair understanding of the number of things AWS EB does for us under the hood! Do not worry if you do not understand all of them at this point, these are concepts that we will revisit in the future!

### Keywords

- Dockerfile
- Docker Image
- Docker Hub
- AWS Elastic Beanstalk
- Logging
- Telemetry
