# Introduction to Container Orchestration with Kubernetes

## Learning Objectives

- Learning what container orchestration is
- Learning what problems container orchestration solves
- Understanding (high-level) the K8s architecture

## Introduction: Brainstorming
- What is container orchestration?
- What problems does container orchestration solve?
- Name some common container orchestration tools.

### Kubernetes (K8s)

- What is Kubernetes (K8s)? Where does its name originate from?
- Let's discuss some of its main features:
  - Deployments and rollbacks
  - Replica management
  - Scaling
- Some other things K8s can help with:
  - Networking
  - Security
  - Configuration management

![K8s Main Features](assets/1-k8s-main-features.jpg?raw=true "K8s Main Features")

## Practical 1

Do some research and answer the following:

- What does the ship wheel in the Kubernetes logo try to represent according to you?
- What is a Kubernetes cluster?
- Where do applications (web servers, API servers, ...) run on a Kubernetes cluster?
- What part of the cluster is responsible for moving containers around?

:grey_exclamation: Even though we haven't covered these yet, do your best with the time you have and do as bit of research.
We'll discuss these concepts afterwards.

## Practical 2

The following diagram attempts to illustrate the relationships between a hypothetical shipping company and its fleet of cargo ships.

![K8s Main Features](assets/k8s_shipping_analogy_diagram.jpg?raw=true "K8s Main Features")

Use this diagram as an analogy to help you research and answer the questions below.

On a high-level:

- What part of a Kubernetes cluster does the shipping company represent?
- What parts of a Kubernetes cluster do the cargo ships represent?

Taking the analogy further, we could imagine that the cargo ship and the shipping company having the following roles/responsibilities:

Shipping company:
- Receives customer requirements and organises fleet accordingly
- Allocates cargo to ships and schedules trips
- Manages and monitors fleet by giving instructions to ships and getting information on their status
- Organises response if something goes wrong during shipping

A cargo ship (with its crew):
- Provides space and a means of transport to containers
- Follows route and instructions from the shipping company
- Makes sure containers remain safe and undamaged
- Flags incidents to the shipping company if something does go wrong
- Provides a means of communication with the outside world (e.g. via radio)

How do these roles mirror those that exist within a Kubernetes cluster?
Can you map each of the responsibilities above to something done by the Kubernetes cluster components you identified in the previous question? 

Research and do what you can in the time you have.

## A bit more detail

Now that you've seen a very high-level overview of a K8s cluster, let's look a bit more closely at the different pieces that form it.

![K8s Cluster More Detailed](assets/k8s_cluster_with_pods.jpg?raw=true "K8s Cluster More Detailed")

### Resources

- [What is container orchestration?](https://www.redhat.com/en/topics/containers/what-is-container-orchestration)
- [What problems does container orchestration solve?](https://www.capitalone.com/tech/cloud/what-is-container-orchestration/)
- [Kubernetes concepts](https://kubernetes.io/docs/concepts/)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/alternate_intro_to_container_orchestration.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/alternate_intro_to_container_orchestration.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/alternate_intro_to_container_orchestration.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/alternate_intro_to_container_orchestration.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=workshops/week-5/alternate_intro_to_container_orchestration.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
