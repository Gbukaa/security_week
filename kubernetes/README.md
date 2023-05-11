# Kubernetes (K8s)

## Kick-off

1. We'll discuss the important things for the week.
2. We'll have a short Q&A.
3. You'll get into your teams and start with one of the [projects for this week](#projects).

## Overview of the week

- There will be a session about Container Orchestration and another one about running K8s locally
- You'll work in teams to build your own K8s cluster using EKS on AWS (Your coach will announce the teams on Slack.)
- You'll work on some K8s further challenges with your local clusters
- You'll organise your own work based on the goals for the week
- There will be a retro on Friday

## Goals for the week

You are already familiar with these questions, but it's important to bear them in mind:

* Are you having fun?

* Are you a better DevOps engineer than you were yesterday?

By the end of the week, the goal is to be able to answer "yes" to the week's primary question:

* **Can you explain what Container Orchestration is?**
* **Can you explain what problems Container Orchestration solves and what its main benefits are?**
* **Can you use Kubernetes to deploy and manage simple applications running on a cluster?**
* **Can you diagram the Kubernetes cluster architecture and the different pieces that take part in it?**
* **Can you use EKS to run a Kubernetes cluster on AWS?**
* **Can you describe the main differences between running your own K8s cluster as opposed to using a Cloud service like EKS?**

## Getting started

To work on this week's projects, you will need to install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [k3d](https://k3d.io/). 
`kubectl` is the main command line tool used to interact with Kubernetes cluster.
k3d is a tool that allows you to run a Kubernetes cluster locally.

```
brew install kubectl k3d
```

## Projects

This week is split into two projects, each taking about half of the week.
You will be tackling them in the order below.

### Project 1: Running Kubernetes locally

In this project, you will be working **in pairs** to run your own Kubernetes clusters locally using a tool called k3d.
You will be managing all components of a Kubernetes cluster, including the control plane, manually.

Your coach will share a recording of the [Running Kubernetes locally workshop](/workshops/week-5/running_k8s_locally.md), which will introduce you to using k3d.
In pairs, you will then work on the [Kubernetes Further Challenges](k8s-further-challenges.md).

### Project 2: Metapod

In this **team project**, you will be learning how to set up a Kubernetes cluster using AWS' Elastic Kubernetes Service (EKS). 

A K8s cluster can be difficult to build, configure and get started with, which means that for some companies, having to managing their own K8s clusters is not always desirable or cost-effective. 
So there are a bunch of solutions provided out there that fully manage the Kubernetes control plane.
EKS is one of them.

> :warning: **Important:** This project is designed to be worked on as a team. Resource limitations on AWS mean that you will only be able to start one Kubernetes cluster per team! Make sure you work together on a single cluster.

Ready? Fork [this repository](https://github.com/makersacademy/metapod) and follow the instructions in its README to get started :bug:


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=kubernetes/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=kubernetes/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=kubernetes/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=kubernetes/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=kubernetes/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
