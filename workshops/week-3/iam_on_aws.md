# IAM on AWS

IAM (Identity Access Management) is a key concept when you are working with AWS.

In a nutshell, IAM allows to manage users and their level of access on AWS.

### Learning Objectives
- Understand IAM and its key concepts on AWS
- Apply IAM concepts to an example scenario
- Understand the Principle of Least Privilege


### Key Terminology

1. Users
2. Groups
3. Policies
4. Roles


### Practice: apply IAM for the following scenario

Severus, our Tech Lead, would like the team to gain a better understanding of IAM on AWS. As a quick proof of concept, he has prepared an application split in the following repositories:

- Frontend: An Angular project served by Nginx
- Backend: A Springboot project (Java)

He has just set up an AWS account for the team and called a meeting to discuss the following diagram:

![IAM on AWS scenario](assets/iam-on-aws.jpg?raw=true "IAM on AWS scenario")

There will be two groups, and each group will be responsible for deploying (in the future, not now) one of the two projects that form the application.

:pencil: Now, in groups, discuss what **users**, **groups**, **policies** and, finally, **roles** are needed to achieve this.
- Who is responsible for creating each of the resources needed?
- Is it Severus? Is it you (the group)? Or both?

:information_source: Note that you do not need to find the specific policy/role names, but rather know that we need a policy or a role for the tasks at hand.


### Principle of Least Privilege

This is such an important concept in Cybersecurity. You're not the owner of the AWS account we've been using for the course, and as you probably haven't researched IAM until now, you haven't realised that you may have had an `AdministratorAccess` policy.

:brain: What does the `AdministratorAccess` policy involve? Let's discuss why it's not a good practice to attach such policy to every user under one AWS account.


### Resources

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
- [Access Control - Principle of Least Privilege](https://owasp.org/www-community/Access_Control#:~:text=In%20security%2C%20the%20Principle%20of,be%20limited%20in%20this%20manner.)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-3/iam_on_aws.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-3/iam_on_aws.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-3/iam_on_aws.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-3/iam_on_aws.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-3/iam_on_aws.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
