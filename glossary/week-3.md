## [GitHub Actions](https://github.com/features/actions)
Through GitHub Actions, you can automate all your software workflows using CI/CD practices. This is useful when building, testing and deploying your code, among other tasks like, for example, linting.

## [Amazon S3](https://aws.amazon.com/s3/)
A simple object storage service by Amazon. Used normally to store and protect data. Can be used to store app revisions too (commonly as part of an automation pipeline where app is deployed and hosted on the S3 bucket after running the CI/CD jobs).

## [Amazon CodeDeploy](https://docs.amazonaws.cn/en_us/codedeploy/latest/userguide/welcome.html)
A deployment service provided by AWS which automates app deployments to a bunch of different services, for us this week it will be Amazon EC2. This week, we will deploy our packaged app revision to our EC2 instance and run 1+ container(s) based on the Docker image.

## [Amazon EC2](https://aws.amazon.com/ec2/)
EC2 is a web service used for compute purposes in the cloud. We, as users, manage all aspects of it: scalability, configuration, access...

## [Security Group (AWS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
You should think of a Security Group as a virtual firewall that allows us to control what sort of traffic gets and goes out of our EC2 instance. We normally add Custom TCP rules bound to a specific port (3000 for this week) and allow all IPs to access our instance publicly over the Internet (0.0.0.0/0)

---

Please feel free to make any suggestions you'd like to see included in this week's glossary and they will be added or discussed further.

Also, feel free to make a pull request if you'd like to add something yourself or make any amendments, but this should not take too much of your time this week as there's enough to go through with the project tasks.
