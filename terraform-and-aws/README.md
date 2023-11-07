# Terraform and AWS

Learn to:

* Use Terraform to write infrastructure as code (IaC) for an AWS* setup
* Explain the benefits of using IaC over manual configuration
* Make iterations on a deployment using IaC as project complexity increases

## Kick-off

1. We'll discuss about the important things for the week
2. We'll have a short Q&A
3. You'll get into your teams and run through the [project tasks](#project-setup-and-sections)

## Project overview

- You'll work in teams to set up two separate workflows: one to manage and deploy your infrastructure on AWS using Terraform and another one to deploy an existing application on AWS
- You'll organise your own work based on the goals for the week
- There will be a session about IaC (Infrastructure as Code)
- There will be a retro on Friday

## Project goals

You are already familiar with these questions, but it's important to bear them in mind:

* Are you having fun?

* Are you a better DevOps engineer than you were yesterday?

By the end of the week, the goal is to be able to answer "yes" to the week's primary question:

* **Infrastructure as Code in general:**
  * Can you explain what the term "Infrastructure as Code" refers to?
  * Can you explain the benefits using IaC tools and what problems they solve?

* **Terraform**
  * Can you diagram how the basic Terraform commands are used to manage Cloud infrastructure?
    * `terraform init`
    * `terraform plan`
    * `terraform apply`
    * `terraform destroy`
  * Can you explain the following fundamental building blocks of the Terraform language?
    * Provider
    * Resource
    * State
    * References
  * Can you write a Terraform configuration and use it to create a piece of infrastructure on AWS?
  * Can you write a Terraform configuration and use it to create and manage the infrastructure of a web app?
  * Can you write your Terraform code in such a way that `terraform apply` only needs to be run once to create all of the infrastructure needed for a given project (1-touch provisioning)?

* **CI-CD with Terraform**
    * Are you able to build an automatic workflow using Github actions to manage your project infrastructure using Terraform?
    * Can you set up a Github actions pipeline to deploy your application onto existing infrastructure on AWS?

### Start Here

[Getting Started with Terraform](getting_started_with_terraform.md)

#### Section 1: Terraform

1. One member in your group, create a **private** Github repository. This repository will serve as the place from where you will manage your infrastructure for this week - Your Terraform project!
2. Add the other members of your group as collaborators.
3. Add a `.gitignore` file and paste in [the contents of this template `.gitignore` file for Terraform](https://github.com/github/gitignore/blob/main/Terraform.gitignore).
4. Make a copy of this [Trello board](https://trello.com/b/cK33Iwbl) for your group.
5. Work through the cards on the board and have fun!

#### Section 2: Task Listing App (on AWS)

Feel free to read ahead and have a look at the README of the app below but only move on to actively working on this section once you've reached the "Get your app deployed" card in the Trello board linked above.

1. One member in your group, fork the following [Github repository](https://github.com/makersacademy/task-listing-app).
2. Add the other members of your group as collaborators.
3. Work through the project README and have fun!

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
