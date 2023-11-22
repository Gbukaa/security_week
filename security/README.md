# Security

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/devops/security/HOW_TO_COACH.x.md)_

Cloud engineers deploy software so it can be used. A deployed application is likely to have security vulnerabilities, which could be exploited by attackers to alter the behaviour of your application, corrupt or steal data, or worse. If that happens — in the best case, your company could lose some data or money. In the worst case, your company will make the news.

In this module, you will learn to start looking at software having security in mind, how to uncover potential security flaws, and how to prevent or fix them.

## Learning objectives

 * Explain the importance of security and its implications
 * Use SAST and DAST tools to uncover security risks
 * Use the practice of Threat Modelling to uncover security risks in a deployed application

## Narrative

You and your peers just joined Poochie Pals. They run a web platform to connect pet owners with pet-sitters, so they can look after pets when people go away for holiday or work.

You've just learned that a few months ago, a group of attackers managed to exploit several security flaws in the website and got access to the database. User data was corrupted or even deleted, and the website was down for hours — leading a lot of users to complain on social media or contact customer support.

After this incident, management promised some time to engineering teams so they can work to improve security and prevent this to happen again. However, the team is already under pressure to release a new version of the website really soon.

Your job this week is to investigate these new features, and find potential security issues, before everything gets released.

## Phase 1 - Security bites

<!-- OMITTED -->

<!-- OMITTED -->

First, you'll need to learn a bit about security — potential vulnerabilities in a codebase, but also in cloud networks configuration.

1. [Explore common vulnerabilities](./vulnerabilities_project) in a codebase
2. [Video introduction to security groups in AWS](https://www.youtube.com/watch?v=wUb6OgAXDpM) and why they're useful

## Phase 2 - Projects

1. [Poochie Pals Codebase](./projects/01_codebase.md), in which you'll explore security flaws in code.
2. [Poochie Pals Deployed](./projects/02_deployment.md), in which you'll investigate security flaws in a deployed cloud setup.
3. [Poochie Pals payment page](./projects/03_challenge.md), in which you'll apply a collaborative process called Threat Modelling.

## Phase 3 - Solo project

Work on this project individually.

Using all of the tools and techniques you learned so far, investigate [this login form application](./solo_project/login-form/) for security issues and fix them in the code.

[Then, submit an archive of the fixed codebase, using this link](https://airtable.com/appJ1wvInmFyFFYlN/shrvo9ePjlwnaiLv5?prefill_Item=ce_security_03). Include a document listing of the different problems you found, and how you've approached them.

## Extension work

Finished all of the above? Start on the [OWASP Juice Shop project](./projects/extension.md).

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
