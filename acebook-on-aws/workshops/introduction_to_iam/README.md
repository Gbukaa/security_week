# Introduction to IAM

Learn to:
  * Explain and understand the difference between users, roles and policies
  * Use a custom policy to allow or deny specific actions
  * Investigate and fix broken permissions 

## Introduction

<!-- OMITTED -->

Your coach will introduce and demonstrate the following concepts:
  * Permissions
  * Users, roles, policies
  * Creating a user and attach a policy allowing or denying permissions

## Exercise 1

A junior engineer just joined your team. You would like them to have access to EC2 and see everything in there ("read" access), but they shouldn't be able to modify or create anything (e.g launch new instances, or modify security groups).

They also don't need access to other services in AWS.

Create a new IAM user named `junior-engineer-<YOUR NAME>` and attach the most appropriate policy to it.

## Exercise 2

Severus, our Tech Lead, would like the team to gain a better understanding of IAM on AWS. As a quick proof of concept, he has prepared an application split in the following repositories:

- Frontend: An Angular project served by Nginx
- Backend: A Springboot project (Java)

He has just set up an AWS account for the team and called a meeting to discuss the following diagram:

![IAM on AWS scenario](../assets/iam-on-aws.jpg?raw=true "IAM on AWS scenario")

There will be two groups, and each group will be responsible for deploying (in the future, not now) one of the two projects that form the application.
📝 Now, in groups, discuss what users, groups, policies and, finally, roles are needed to achieve this.

Who is responsible for creating each of the resources needed?
Is it Severus? Is it you (the group)? Or both?

## Exercise 3

[Find your user in the IAM console](https://us-east-1.console.aws.amazon.com/iamv2/home#/users).

Then, attach a new policy to your user which will deny the action of terminating instances. 

You know it worked if you can run a new instance in EC2, but are not able to terminate it. (You should get an error message `Failed to terminate an instance: You are not authorized to perform this operation.)`

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fworkshops%2Fintroduction_to_iam%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fworkshops%2Fintroduction_to_iam%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fworkshops%2Fintroduction_to_iam%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fworkshops%2Fintroduction_to_iam%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fworkshops%2Fintroduction_to_iam%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
