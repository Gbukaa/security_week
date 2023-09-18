# Setup Continuous Deployment (CD)

Learn to
 * Setup Github actions to redeploy the code
 * Use environment variables to configure the CI-CD process

## Automate the deployment

The project contains a bash script `scripts/deploy-to-instance.sh` we can use to deploy the new code via SSH to the instance. However it contains an old hard-coded IP address, so it doesn't work anymore.

Here's what to do now:

 1. Use an environment variable to configure the instance IP address.
 2. Add a new stage `deploy` to your Github CI configuration, so this script is executed to deploy the code after the build stage.

You will need to add environment variables in the Github config so the script has access to:
 * The instance IP address 
 * The private key you've setup when starting the instance

You can do this on your Github project, in Settings -> CI/CD -> Variables.

You will know it worked if you can push changes to your Acebook project, and see them live once the CI-CD process in Github has completed.

## Reflection

Update the diagram you made in the last section to reflect the changes in the process — including the new automated CI-CD build step.

## What's next

One of your colleagues just warned that some incoming SSH traffic to your server — looks like some bots are trying to connect to the server.

There's a security problem with our current setup — let's fix it.

[Next Challenge](04_securing_network.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F03_continuous_deployment.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F03_continuous_deployment.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F03_continuous_deployment.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F03_continuous_deployment.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F03_continuous_deployment.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
