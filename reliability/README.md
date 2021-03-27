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

Your team works for an organisation that provides software and services to veterinary hospitals. You have recently been hired by a client who wants you to replace a critical system that they use to store patient notes and medical images so that all staff can access them. It also performs some important analysis of the medical images. The system is called HOSP.

The reason they want you to replace it is because the current system is not reliable. This veterinary hospital sometimes deals with emergency appointments, and there have been some difficult situations due to the system being slow, unreliable, or just plain offline. They have raised this with the software vendor, who was not helpful. Your client suspects there may be something going on internal to that vendor which is affecting things.

Your jobs, in order of priority:

1. Preserve the functionality of the system.
2. Increase the reliability of the system and ensure no security breaches.
3. Implement some improvements to the system.

The hitch? You don't have the code yet. It's supposed to be coming later this week but the vendor has been dragging their heels. You do, however, have API documentation and access to the load balancer through which all the traffic passes.

## Your reliability targets

* Your system should respond to 99% of user requests successfully over the duration of this project.
* No security breaches.

We will track the successful request response rate on [this dashboard](http://reliability-panel.mkrs.link/). Requests that don't come from the users won't affect towards this, so you can make test requests, but be mindful that your requests don't add harmful load to the upstream server.

Note: a real system would have both stricter and more rigorous requirements. For example, there may be a requirement to respond to successfully 99.99% of requests within 3 seconds and be available 99.999% of the time (known as [five nines](https://en.wikipedia.org/wiki/High_availability#Percentage_calculation)).

## Events

Throughout the week, your coach will alert you to events happening in the world of this system. Some of these may not mean much, others may affect your work by increasing the traffic to your service or indicating urgent issues, and yet others may be harbingers of issues yet to come.

It will be your job to interpret the meaning of the events, and respond appropriately. Your service, like services in the real world, will do well if it is secure, reliable, and capable of meeting the stresses that the world may place upon it.

## Improvement Tickets

These are less important to your client than reliability and security, but are still desirable.

* **Make the service available via HTTPS.**  
  All traffic is HTTP for now, but enabling HTTPS is the first step towards
  changing that.

* **Store image screening results.**
  Right now, images can be screened and the results returned, but those results
  are not stored by the server. Implement a way to store those, perhaps using
  the existing notes feature.

* **Tighten up authorisation security.**
  For example, right now any staff can create notes that claim to be written by
  any other member of staff. There may be other issues, but be mindful not to
  accidentally prohibit something the users are doing right now!

* **Add an audit trail feature.**
  Your client would like to see a log of who has interacted with the system and
  what they have done, to ensure that bad actors or unauthorised access can be
  noticed and dealt with.

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

The only system you can directly control is the Load Balancer, as well as any other systems or infrastructure you choose to create. The Load Balancer will be useful, because it allows you to redirect traffic from the User Traffic Gateway to your own infrastructure. You can do this generally, for a particular % of traffic, and for specific HTTP Endpoints.

You can submit support tickets to HOSP or Corporate IT (via your coach) but it is up to them what requests they grant and under what timeframe. There's no expectation that you will have to contact HOSP or Corporate IT in order to succeed in this project.

## Getting started

Your coach will give you access to the load balancer, and you already have the ability to create other resources as you need.

Reading up on the [Strangler Fig Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) may be useful.
