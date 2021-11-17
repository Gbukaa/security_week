# Running K8s Locally

## Learning Objectives
- Understanding what it takes to work with self-managed clusters (as opposed to provider-managed clusters)
- Launch your first K8s cluster locally using K3d

## Introduction
So, until now you've worked with a provider-managed cluster, where you did not have to interact with the Control Plane or worry about provisioning the worker nodes... The infra was managed by AWS and your focus was to deploy your application and expose it to the world.

Now, we're going to explore a first taste of what's like to run your self-managed K8s clusters. In this session, we'll do that using our local environment.

## Tools for Local K8s Development
- What's K3s?
- What's K3d?
- Alternative tools

## K3d Demo
Your coach will demo what it's like to work with a local K8s cluster using K3d, including:
- Creating our first cluster
- Checking the K8s local configuration
- Being aware of the state of the cluster
- Adding new worker nodes to an existing cluster
- Creating a deployment to an existing cluster
- Exposing the application deployed so that it's accessible from our machine
- Cleaning up the generated resources

## Practice: breakout rooms

1. Create a K3d cluster that has **two worker nodes**

:question: Before you create the cluster, do you think there may be a better way to do this than what you've just seen in the demo (i.e. creating the worker node manually and adding it to the cluster)?

2. Create a deployment for the same application you've used this week in your cluster: `paulbouwer/hello-kubernetes:1.10`

3. Following what you saw on the demo, expose your application and test if it works correctly from your machine.

4. Finally, remember to clean up the cluster after you're done with the exercise.

## Plenary
We'll now see some demos and have a discussion.

Any questions?

### Resources
- [K3s](https://k3s.io/)
- [K3d](https://k3d.io/)
- [Application Image Reference](https://hub.docker.com/r/paulbouwer/hello-kubernetes/)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/running_k8s_locally.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/running_k8s_locally.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/running_k8s_locally.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/running_k8s_locally.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/running_k8s_locally.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
