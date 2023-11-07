# Continuous Deployment (CD) on GitHub Actions to Amazon Web Services (AWS)

In the last module you set up a CI-CD pipeline from a repository to a static
website hosted on AWS S3.

Now you will create a CI-CD pipeline for a more complex system — a web
application with a database, deployed on the virtual private server platform AWS
EC2.

This page is a guide to the high level steps involved. You are welcome to ignore
all or parts of it if you would like to have a more authentic cloud engineering
experience.

## Set up the project

Follow the instructions in the project README to set up the project and get it
running.

You'll know you're done when your tests all pass.

## Set up Continuous Integration

Similarly to last time, we want to set up GitLab to run our tests when someone
pushes a new change.

You can either try setting it up from scratch based on your own research — much
like a cloud engineer would have to do — or make use of the sample
`.gitlab-ci.example.yml` in the repository. You'll need to rename this to
`.gitlab-ci.yml` for it to be detected by GitLab and run.

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

## Set up an S3 Bucket

We're going to set up a deployment pipeline using AWS CodeDeploy. This will
involve:

1. GitLab using the AWS CLI to upload an 'application revision' (a zip file of
   all of your codebase) to S3.
2. GitLab triggering CodeDeploy to start a new deployment.
3. CodeDeploy, which will manage a fleet of servers for you, to ask them to
   download the application revision and start running it.

   When I say 'fleet' — this time it's only one. But it could be fifty!

Let's start with setting up the S3 bucket. Then we'll create the EC2 instance
that will run our server. Then we'll set up CodeDeploy, and configure GitLab to
start the deployment.

Create a new S3 bucket and make sure you block all public access. Unlike last
time, we don't want any outside users accessing its content.

## Launch and configure a new EC2 instance

Go to EC2 -> Instances -> Launch instances.

Give it a nice name, related to your group.

Under "Application and OS Images", select Amazon Linux 2023.

Under "Instance type" select `t2.micro`.

Under "Key pair" click "Create new key pair" and create a PEM key. Keep it
secret, keep it safe.

Under "Network settings" select 'Create security group', allow SSH traffic from
anywhere, and allow HTTP traffic from the Internet.

Click into "Advanced details" and under "IAM instance profile" click "Create new
IAM profile". You'll need to configure this profile, which represents what the
instance is given permission to do on AWS, to access the S3 bucket you created.
You can create this yourself, or there's a sample configuration in the
[Resources](#resources) section. Give it a name related to your team.

After you've created the instance profile, go back to the EC2 configuration page
and select it. You may need to click the little 'refresh' icon next to the box
to get it to show up.

Find the field 'User data'. We can use this to ask our EC2 server to run some
special commands after it starts up. We're going to use this to run a script
that installs the CodeDeploy agent. The CodeDeploy agent is a background service
that CodeDeploy will contact to tell it to download our new application revision
and run it.

I recommend you use the sample script in the [Resources](#resources) section,
but if you'd like to research and write one yourself you can!

Click 'Launch instance'.

After this, click into the EC2 instance -> Security and click the item under
'Security groups'. Click 'Edit inbound rules' and add another rule of type
'Custom TCP', Port range '3000', and source '0.0.0.0/0'. This will allow the
instance to receive traffic on port 3000, where our Acebook server will be
listening.

After a few minutes, SSH into the virtual server using the PEM key you
downloaded, and run `sudo service codedeploy-agent status` to check that the
CodeDeploy agent is running successfully.

## Set up CodeDeploy

CodeDeploy is going to manage the process of picking up our application revision
(zip file of our code) from Gitlab and getting all of our EC2 instances to pick
up and run it.

Go to CodeDeploy -> Applications -> Create new application. Give it a name
related to your team and select 'EC2 / On Premises'.

For this, go to IAM -> Roles -> Crate Role. Find 'CodeDeploy' in the drop-down
and select 'CodeDeploy'. It will populate the right policy for you. Give it a
name related to your team.

After this, create a new Deployment Group. Call it `production` and assign it
the role you created. Select the "In-place" deployment type. Under 'Environment
configuration' select 'Amazon EC2 instances' and use the 'tags' section to
select the key 'Name' and in 'Value' put the name you gave your EC2 instance.

Under 'Install AWS CodeDeploy Agent' select 'Never'. Under 'Deployment
Configuration' select 'CodeDeployDefault.AllAtOnce' and then under 'Load
balancer' uncheck the 'Enable load balancing' box. Load balancing would be
necessary if we had a fleet of a lot of servers that we want to distribute
traffic across, but we only have one so we don't need it.

Click 'Create deployment group'.

## Set up a user for GitLab CI to use to deploy

We'll need to set up a user with the right permissions to kickoff the deployment
process and give our GitLab pipeline its credentials.

This is similar to the last module, however the policy is different. You can use
the sample policy in [Resources](#resources), or research yourself what it will
need.

## Set up GitLab CI to deploy

There are a few steps left:

1. Updating your CI configuration.
2. Adding scripts so that CodeDeploy knows how to run your app.
3. Setting up a database.

You can find a sample CI config under [Resource](#resources).

## Set up the CodeDeploy scripts

CodeDeploy relies on a file called `appspec.yml` to tell it how to run your
application, supported by some scripts to do the actual work.

You can find a sample in [Resources](#resources).

After this, when you push your changes, you should see your pipeline pass, then
go to CodeDeploy -> Deploy -> Deployments and see it deploy.

You should then be able to visit your EC2 server on protocol `http://` and port
`3000` and see it respond... for thirty seconds, before it crashes because it
can't connect to the database.

## Set up the database

You will need to set up a database for your EC2 server to connect to.

You could set up the MongoDB server on the EC2 instance too — but this is not
very realistic. If we wanted to scale up to two servers then we'd have two
separate databases — no good to have some users on one version and not the
other!

A better alternative would be to use AWS DocumentDB and connect to that. For
this, you will need to set up a new DocumentDB and provide the credentials on
the EC2 server.

After this, your server should be running and your CI-CD pipeline will be
complete. Try adding some features to the app and seeing them deploy.

## Set up load balancing

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

To setup load balancing between at least two instances, you will need to:
 * Start and setup a second EC2 instance [following the same process as
   before](#launch-and-configure-a-new-ec2-instance) (including the environment
   configuration for the database connection).
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

## Resources

Here's a sample IAM instance profile policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CodeDeployBucketPermissions",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR_S3_BUCKET_NAME/*"
            ]
        },
        {
            "Sid": "CodeDeployBucketListPermissions",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR_S3_BUCKET_NAME"
            ]
        }
    ]
}
```

Here's a sample script to ask your EC2 instance to run when it starts up:


```shell
#!/bin/bash
sudo yum -y update
sudo yum -y install ruby
sudo yum -y install wget
cd /home/ec2-user
wget https://aws-codedeploy-eu-west-2.s3.eu-west-2.amazonaws.com/latest/install
chmod +x ./install
./install auto
```

Here is a sample policy to assign to your GitLab deployment user:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3PutObject",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::YOUR_S3_BUCKET_NAME/*"
        },
        {
            "Sid": "CodeDeployCreateDeployment",
            "Effect": "Allow",
            "Action": [
                "codedeploy:CreateDeployment",
                "codedeploy:GetApplicationRevision",
                "codedeploy:GetApplication",
                "codedeploy:RegisterApplicationRevision",
                "codedeploy:GetDeploymentConfig"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "PassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_CODEDEPLOY_ROLE_NAME"
        }
    ]
}
```

Here's a sample GitLab CI-CD config:

```yaml
image: node:lts

services:
  - name: mongo:latest
    alias: mongodb

variables:
  MONGODB_URL: mongodb://mongodb:27017/acebook_test

stages:
  - test
  - deploy

before_script:
  - npm ci

test_unit:
  stage: test
  script:
    - npm run lint
    - npm run test:unit

test_integration:
  image: cypress/base:latest
  stage: test
  script:
    - npm run start:ci &
    - npm run test:integration

deploy:
  stage: deploy
  image: nikolaik/python-nodejs:latest
  script:
    - pip install awscli
    - aws deploy push --application-name $CODEDEPLOY_APPLICATION_NAME --s3-location s3://$S3_BUCKET_NAME/revision.zip --ignore-hidden-files --region eu-west-2
    - aws deploy create-deployment --application-name $CODEDEPLOY_APPLICATION_NAME --deployment-group-name $CODEDEPLOY_DEPLOYMENT_GROUP_NAME --s3-location bucket=$S3_BUCKET_NAME,key=revision.zip,bundleType=zip --region eu-west-2
  only:
    - master
```

Here is a sample `appspec.yml`:

```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /var/acebook
permissions:
  - object: /
    pattern: "**"
    owner: ec2-user
    group: ec2-user
hooks:
  ApplicationStop:
    - location: scripts/stop_server.sh
      timeout: 300
      runas: ec2-user
  AfterInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
      runas: ec2-user
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: ec2-user
```

This config requires the following environment variables are set:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `CODEDEPLOY_APPLICATION_NAME`
* `CODEDEPLOY_DEPLOYMENT_GROUP_NAME`
* `S3_BUCKET_NAME`

And the scripts associated:

```shell
#!/bin/bash
# File: scripts/install_dependencies.sh
# Installs the dependencies using `npm install`
source ~/.bash_profile
cd /var/acebook
npm install
```

```shell
#!/bin/bash
# File: scripts/start_server.sh
# Starts the Acebook server
source ~/.bash_profile
cd /var/acebook
npm run start:production 2>&1 >> app.log < /dev/null &
```

```shell
#!/bin/bash
# File: scripts/stop_server.sh
# Kills any existing Acebook server process
pkill -f "node ./bin/www" || true
```



<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=acebook-on-aws/high-level-walkhrough.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=acebook-on-aws/high-level-walkhrough.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=acebook-on-aws/high-level-walkhrough.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=acebook-on-aws/high-level-walkhrough.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=acebook-on-aws/high-level-walkhrough.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
