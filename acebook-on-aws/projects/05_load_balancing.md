# Load balancing and monitoring

Learn to
 * Setup a load balancer to distribute traffic over multiple servers

## On load balancing

You've got a single EC2 instance running so far — this is fine as long as our
application doesn't need to handle much load. However if it becomes more
popular, more users will want to use it, and the traffic could become a
bottleneck. An easy way to check how "busy" is your instance is to go in the
Monitoring section of the instance on the EC2 console, and check the CPU
utilization graph.

To solve this problem, we can add more servers. This is called "scaling out" or
"horizontal scaling" — we distribute the HTTP traffic load to more instances, so
all instances become less busy, and the application is more responsive.

However this brings another challenge: we'll have one public IP address (one
public DNS) per instance. Surely we can't ask our users to randomly select one
of many addresses to connect to.

A way to solve this problem is to use a load balancer. Think of a person
directing incoming customers to different clerks at the post office, to avoid
one clerk being busier than others. This person is the load balancer, and the
clerks are the instances we want to distribute the traffic to.

Users connect to the load balancer URL (usually the main application URL, such
as `http://my-acebook-app.com`), then the load balancer dispatches HTTP requests
to the different machines, according to their current load.

## Exercise

To setup load balancing between at least two instances, you will need to:
 * Start and setup a second EC2 instance [following the same process as
   before](01_deploy_on_ec2.md).
 * Create a new [Target
   group](https://eu-west-2.console.aws.amazon.com/ec2/home?region=eu-west-2#TargetGroups:)
   in EC2. Your server is running on port 3000, so make sure to set the HTTP
   port to this value.
 * Create a new [Load
   balancer](https://eu-west-2.console.aws.amazon.com/ec2/home?region=eu-west-2#LoadBalancers:).
   You can select "Application Load Balancer" and leave most settings to
   defaults. Select all three subnets in the "Network Mapping" section. You will
   also need to select the target group you've previously created.

You will know you've reached your goal if:
 * You can connect to both EC2 instances directly using their public DNS (like
   you were doing before).
 * You can see both instances ("targets") registered as "Healthy" in the details
   of the Target group.
 * You can connect to the load balancer public DNS and access your application.

## Updating the deployment script

The script `deploy-to-instance.sh` only deploys to a single instance — but now
you have two! Update the script so the code is deployed via SSH to both
instances.

You'll know it worked if you can push an update to the website, and see it
deployed on both instances (refresh the page a few times to make sure — the load
balancer should randomly pick up one instance or the other).

## Reflection

Update your diagram to reflect the second instance and the load balancer
distributing the traffic.

Once again, let your coach know when you're done.

## What's next

Create a few posts on your Acebook app (the URL is `/posts/new`). Then refresh
the page listing all the posts. What do you notice?



[Next Challenge](06_external_database.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F05_load_balancing.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F05_load_balancing.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F05_load_balancing.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F05_load_balancing.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F05_load_balancing.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
