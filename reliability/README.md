# Reliability Project

For users to get their jobs done, the system has to be around and working when
they need it. This will be one of your most important responsibilities as an
engineer.

This project will task you with making improvements to a critical system while
also keeping it highly available. You will encounter challenges throughout the
week that will test your skills. In the process, you will gain knowledge, skills
and perspective necessary to do this for real.

## Learning Objectives

* Learn to improve and upgrade a system with minimal compromise to availability.
* Explain the importance of observability in a system.
* Learn to make a system more observable.
* Learn to resolve security issues in a running system.

## Narrative

Your team works for an organisation that provides software services to veterinary hospitals. You have recently been hired by a client who wants you to replace a critical system that they use to store patient notes and medical images so that all doctors can access them. It also performs some important analysis of the medical images.

The reason they want you to replace it is because the current system is not reliable. This veterinary hospital sometimes deals with emergency appointments, and there have been some difficult situations due to the system being slow, unreliable, or just plain offline. They have raised this with the software vendor, who was not helpful. Your client suspects there may be something going on internal to that vendor which is affecting things.

Your primary job is to preserve the functionality of the system while increasing the reliability. Your secondary job is to add some useful functionality to the system.

The hitch? You don't have the code yet. It's supposed to be coming later this week but the vendor have been dragging their heels. You do, however, have API documentation and access to the load balancer through which all the traffic passes.

## Your reliability targets

* Your system should be online 99% of the time over the duration of this project.
* Your system should respond to 99% of requests successfully over the duration of this project.
* No security breaches.

(A real system would have much stricter availability requirements than this.)

## Your tickets

*

## The system

![System Diagram](./Vet%20Diagram.svg)

The system is composed of the following components. Most of these are out of your control.

* **End-User Applications.**
  Mobile devices, computers, and other systems that send traffic to the User Traffic Gateway.

* **User Traffic Gateway**
  Which aggregates the traffic, asks the DNS server to resolve the address to your Load Balancer, and forwards the traffic there.

* **Load Balancer**
  This currently forwards all traffic on to the HOSP server, but in theory it can be asked to forward all or a portion of the traffic to anywhere. Your team controls this.

* **HOSP Web Server**
  This is managed at great expense by HOSP Corp. It responds to requests according to its API, stores relevant data, and performs image processing. It probably has a database somehow connected to it, but you're not sure. It's not a very reliable server. Your client regularly complains of its unreliability. [You can read the HOSP API documentation here.](https://expert-guacamole-1b33b4a0.pages.github.io/)

The only system you can directly control is the Load Balancer, as well as any other systems or infrastructure you choose to create. You can submit support tickets to HOSP or Corporate IT (via your coach) but it is up to them what requests they grant and under what timeframe. There's no expectation that you will have to contact HOSP or Corporate IT in order to succeed in this project.

## Getting started

Your coach will give you access to the load balancer, and you already have the ability to create other resources as you need.
