# K8s Further Challenges Specs


## Create your local cluster
:rocket: You'll need to create a K3d cluster with two worker nodes.

:exclamation: Important: when creating the cluster, **add this new argument** to the command in the terminal: `-p "8080:80@loadbalancer"`

:grey_question: What does this argument mean? Feel free to have a discussion with your pair partner, but do not spend too much time on it as we'll find out more about it later :wink:


## Deploy Nginx application to your cluster
This time, we're going to work with a different application for our local cluster. You've used the Nginx image before, do you remember when?

:rocket: Create a deployment using the Nginx Docker Hub image: `nginx`


## Expose your application to test it
:rocket: Following what you saw in the demo during our session this morning, expose your application and test if it works correctly from your machine.

:question: This is a great way to quickly test your app and see if it works as expected within the cluster. 
However, what happens if the pod gets deleted?
- To test what happens, find a way to delete the pod on which the Nginx app is running as a container.
- What happens with the traffic that was forwarded from the pod container to your local machine? Why?


## Logging on K8s: Part 1
:rocket: Find out how you can get access to the pod logs where your containerised application is running.

- How could you keep the stream of logs open? :bulb: Perhaps you could add a flag to the command that displays the logs on the terminal.

:boom: There are better ways to monitor the app(s) running on the container(s). Take a look at [Stern](https://github.com/wercker/stern).


## Scalability
At the moment, we only have one replica of our Nginx app. However, due to traffic peaks that cannot be handled efficiently by the only existing replica, Severus (our Tech Lead) has kindly asked us to scale our application to 3 replicas.

:boom: Scale the existing **deployment** to 3 replicas instead of 1.

- :question: Think about why we refer to **scaling the deployment** rather than scaling the application. What could it mean? How are you going to go about this task? What is the plan that you have in mind?

:bulb: One of the two stratagies (scaling the deployment vs scaling the application) is the correct way to proceed. Have a chat with your peer and do some research around these concepts.


## Logging on K8s: Part 2
The real value of packages such as stern comes from when we have multiple pods running our application, or multiple containers running within a pod.

:boom: To get a better idea about what this means, check the logs of the pods running on your cluster (use `Stern` for this).

- What did happen? What are the different colors representing?

:question: Now the traffic from our localhost seems to be targeting just one pod. Why is that?


## Find a better way to expose your app!
Right now we're exposing just one pod through port-forwarding.

:question: How could we expose all of our pods through a single entry point?

:bulb: Think about the EKS project you worked on earlier this week, where a specific resource that was part of the cluster took care of distributing the traffic across the different worker nodes.

Could we do it just the same way? Well, not really. The difference here lies on the fact that when we used EKS we had a `real LoadBalancer` resource provided by AWS with an external IP that was exposed to share it and users could target our application this way.

However, with K3d we're given a `virtual LoadBalancer` that does not work exactly the same way. So we're going to use a different K8s resource to expose our application this time.


## Exposing our services via Ingress
Some of the resources provided below should be helpful to help you understand Ingress and configure it on your local cluster.

:question: Now is a great time to ask yourselves what the extra argument we used earlier on to create our cluster (`-p "8080:80@loadbalancer"`) meant.

In essence, we're doing a very similar thing as compared with the port-forwarding strategy. We are mapping port 8080 from the host (our machine) to port 80 on the container(s) within the cluster.
- :flashlight: If you want to know more about this, the resources below should give you more information about how this works


## Testing our exposed cluster
Awesome! Now you are exposing the Nginx app running in your 3 replicas via Ingress.
:boom: Send some requests to your cluster entry point from your machine. Are these requests reaching different pods within your cluster? :bulb: Check with `Stern` to get some user-friendly visibility on what is going on.


## Cleanup
Great job for making it this far! :star2:

Finally, do not forget to delete your clusters(s)!

### Resources
- [kubectl: show me the logs](https://dev.to/lucassha/kubectl-show-me-the-logs-1ld)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [K3d - Exposing Services](https://k3d.io/usage/guides/exposing_services/)
