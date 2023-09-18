# Monitoring and alerts

Learn to:
  * Explain and analyse metrics related to an instance
  * Use alerting to receive alerts or perform specific actions depending on specific metrics

## On Monitoring

A few sections ago, you setup load balancing to handle the increased traffic on your web instance. However, it would be better if some of it was automated, so we can be alerted when an instance becomes "busy".

This can be done thanks to monitoring and alerting in AWS.

We'll focus on the metric called `CPU utilization` which measures the amount of CPU used by the instance. There are other metrics, such as `Network in` or `Disk reads`. These could be useful, depending on what we need to measure and be alerted on.

## Viewing metrics

Go in the "Monitoring" section of your web instance and open the CPU graph. Click "View in Metrics" and you'll be taken to the page for this specific metric.

## Setting up an alarm

Create an alarm on the `CPUUtilization` metric of your instance. Configure it to be triggered whenever the value is over the thresold of 10. It should send an alarm to your email address (or the email of someone in your team).

You should receive an email similar to this one after setting up the alarm:

> You have chosen to subscribe to the topic:
arn:aws:sns:eu-west-2:664047078509:***********

> To confirm this subscription, click or visit the link below (If this was in
> error no action is necessary):

## Testing the alarm

You can install and use the tool `stress` to artificially stress the CPU of the instance:

```bash
sudo yum install -y stress

# Run stress for 2 minutes
stress --cpu 2 --timeout 120 
```

The CPU of the instance should then spike for a bit. Wait a few more minutes and you should receive an alarm from AWS on your email.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F09_monitoring.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F09_monitoring.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F09_monitoring.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F09_monitoring.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F09_monitoring.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
