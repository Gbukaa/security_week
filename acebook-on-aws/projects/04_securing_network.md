# Securing the network

Learn to
 * Use security groups to restrict network access to an instance

## On Networking

Before fixing the problem, you will need to learn a bit about how networking
works in EC2.

You will need to do your own research on this one — [this video is a good place
to get started](https://www.youtube.com/watch?v=wUb6OgAXDpM). Take note of any
questions or things which are unclear when doing this research, and your coach
will help to clear them out.

## Exercise

Create a new security group with stricter rules:
 * TCP traffic on port 3000 should be allowed from everywhere
 * SSH should be allowed only from IP addresses of members of your team (you can
   ask Google "what is my ip?" to get yours)
 * Every other traffic should be blocked


Then update your instance to use this group instead of the previous one.

## Reflection

Update your diagram to include the security group, and include the changes you
just made. Discuss with your team — how does this improve the security of the
application?

Ask your coach to verify your work once this is done.

## What's next

Have a look at the 'Monitoring' section of your instance — what do you notice?

[Next Challenge](05_load_balancing.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F04_securing_network.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F04_securing_network.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F04_securing_network.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F04_securing_network.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F04_securing_network.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
