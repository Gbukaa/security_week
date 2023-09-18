# Acebook on AWS

Learn to:
* Explain and diagram a simple AWS deployment on EC2
* Implement a CI-CD process to automatically deploy new versions of the code
* Explain IAM identity concepts such as roles and policies

## Overview

You will work in teams to build your own CI-CD solution and to deploy an
existing application using different AWS services (Your coach will announce the
teams on Slack.)

## What is AWS?

Amazon Web Services (AWS) is a cloud provider run by Amazon. There are many
different services, but this week you'll use mainly one called EC2. We can use
this service to deploy web applications "in the cloud". But what does it mean?

In the past, if you wanted to run a program you would have to buy all of the
physical computers that you would need in order to run it, set them up, probably
connect them to the Internet, and maintain them yourself. If you needed the
servers for only a few weeks, you still had to buy them outright, and then
hopefully sell them to someone else. This is typically called on-premise
computing.

In Cloud Computing, you go to a cloud provider company like AWS and say "I've
packaged up my web application into this file — can you run between 2 and 12
copies of it depending on how many are needed to serve the traffic it is
getting." And AWS will go and do that. It's a bit more complex than that in
practice, but that is the general idea.


## Team work

Work through the following sequence in your teams. It's OK if you don't reach
the end.

Each step will require you to do some research. If you feel a bit lost and feel
like you need more guidance, reach out to your coach.

1. [Deploying an application in the cloud](./projects/01_deploy_on_ec2.md) in
   which you will deploy code to a server.
2. [Setup Continous Integration](./projects/02_a_first_ci_process.md) in which
   you will see how to prevent bugs with a CI process.
3. [Setup Continuous Deployment](./projects/03_continuous_deployment.md) in
   which you'll setup Github actions to automatically deploy our code.
4. [Securing the network](./projects/04_securing_network.md) in which you'll
   setup better security groups for your server.
5. [Setting up load balancing](./projects/05_load_balancing.md) in which you
   will distribute the traffic on more than one instance using a load balancer.
6. [Adding an external database](./projects/06_external_database.md) in which
   you'll need to connect different instances on the AWS network.
7. [Use immutable infrastructure](./projects/07_immutable_infrastructure.md) in
   which you'll use images (AMIs) to deploy newer versions of the code.
8. [Debugging](./projects/08_debugging.md) in which you'll investigate and fix a
   broken AWS setup.
9. [Monitoring and alerting](./projects/09_monitoring.md) in which you'll setup
   an alarm from a metric.

## Pairing Challenge

Your coach will announce the pairs for this one.

You should spend some time on this pairing challenge to train the skills learned
in this module. Make sure to save at least half a day (or a bit longer) to work
on it. If you're not sure how to approach it, ask your coach.

[Pairing Challenge - Poochie Pals on AWS](./solo_project/)



<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
