# Pairing Challenge

You just joined the company Poochie Pals. They run a web platform to connect pet
owners with pet-sitters, so they can look after pets when people go away for
holiday or work.

They recently decided to move their entire app to AWS. These days, most of the
team is really busy, and doesn't have much time to work on this.

Your job on this project will be to deploy the Poochie Pals website on AWS, then explain how you did it with a diagram. Let's get started!

## The repository

[Fork this repository](https://gitlab.com/makers-students/poochie-pals-webapp)
to your account to get started. Then clone it locally.

```bash
# Install dependencies
npm install

# Run tests
npm run test
```

There's only one test, which should pass.

## Deploying

If you're re-using the deployment script, you will need to make a few updates to it.
  * The app directory on the instance is `/var/poochie-pals` (instead of `/var/acebook`)
  * The command to restart the app is `sudo systemctl restart poochie-pals`

## Minimal setup

You should build a setup similar to the one you've worked in teams:
 * Repository with a CI-CD pipeline setup — running tests, then deploying via
   SSH to your instance
 * One web instance `t2.nano`
 * One load balancer targeting the instance
 * Security groups correctly configured

Create a diagram and send it to your coach, with the public URL of your load
balancer.

## Want more challenge?

If you've already completed the minimal setup above, and would like more
challenge, also extend it with the following:

 * Two web instances `t2.nano` instead of one
 * Load balancer distributing the traffic on the two instances
 * The CD script is building a new AMI (named with format `poochie-pals-<YOUR
   NAME>`)

Update your diagram and send it to your coach, with the public URL of your load
balancer.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fsolo_project%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fsolo_project%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fsolo_project%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fsolo_project%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fsolo_project%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
