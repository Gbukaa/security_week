# Setup Continuous Integration (CI)

Learn to

 * Setup a CI-CD process using Github
 * Explain the benefits of using a CI process to prevent problems during deployment

## Preventing problems

The previous version of the code was buggy — and caused the website to break!

By implementing a CI-CD process, we can ensure that automated tests can be run against every new version of the codebase, before it can be deployed. 

If any test fails, nothing should be deployed, and people should go on and fix things, before this process is attempted again.

## Set up Continuous Integration with Github

We want to set up Github to run our tests when someone pushes a new change.

You can either try setting it up from scratch based on your own research — much
like a cloud engineer would have to do — or make use of the sample config file in `workflows/.build-ci.yml`

If you'd like to set up your own, consider the following jobs your CI config
will need to achieve:

* Use a base image which has the right prerequisites for the tests to run
  successfully. In this case, it's Node.JS.
* Set up and run the MongoDB database service that the tests rely on.
* Ensure the tests know where to find the database server, likely using
  environment variables.
* Install the dependencies using `npm install`
* Run the linter using `npm run lint`
* Run the unit tests using `npm run test:unit`
* Start the CI version of the web server using `npm run start:ci`, and run it in
  the background so that it doesn't block the integration tests from starting.
* Run the integration (Cypress) tests using `npm run test:integration`

## What's next

You now have a CI build which runs everytime new code gets pushed. That's good — but we still need to deploy the code manually.

It would be better to have the code deployed automatically, after the CI build is successful. We'll see how to do this in the next section.

[Next Challenge](03_continuous_deployment.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F02_a_first_ci_process.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F02_a_first_ci_process.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F02_a_first_ci_process.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F02_a_first_ci_process.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F02_a_first_ci_process.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
