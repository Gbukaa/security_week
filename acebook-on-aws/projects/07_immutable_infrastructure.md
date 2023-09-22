# Immutable infrastructure

Learn to:
 * Use immutable infrastructure to avoid configuration drift

## Mutable and Immutable

It's very likely your instances are the same you've launched initially. You've deployed new code, updated configuration, and maybe did other things since these were first launched.

This can cause problems for different reasons, for example:
 * Updating configuration can be time-consuming and complex, if we have a lot of instances running
 * Having instances running for a long time means these are more exposed to security risks, since they run older versions of the OS (unless you make sure all newer security patches are installed)
 * AWS sometimes will need to terminate your instances for maintenance — don't assume they will run forever.

It also means the risk of losing an instance becomes bigger, as time goes on — if your server has been running for months, replacing it will mean re-doing configuration, making sure the right version is deployed, etc. This increases the risk of human error and the complexity of it.

Having an "immutable" infrastructure means that any server shouldn't be updated at all once launched. Any new deployment, or change of configuration means launching a new instance, and discarding the previous one.

## Exercise

**You will need to create a new IAM user** for this exercise, and generate an access and secret key for it. You can name this user `deploy-user-<YOUR TEAM NAME>`.

This user will only need programmatic access (not access to the AWS console), and will only need to have the right permissions to use EC2. Here that "user" won't be a human, but it will give access to EC2 to the CI-CD script.

There is a bash script in `scripts/build-ami.sh` which builds a new image (AMI) with the new version of the code. This script will need two environment variables: the access and secret key of your deploy user.

Update the deployment stage of the CI-CD pipeline to use this script, so a new image is built when a new version of the code is pushed.

[Next Challenge](08_debugging.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F07_immutable_infrastructure.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F07_immutable_infrastructure.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F07_immutable_infrastructure.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F07_immutable_infrastructure.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F07_immutable_infrastructure.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
