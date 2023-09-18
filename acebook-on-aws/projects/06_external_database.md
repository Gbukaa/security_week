# Adding an external database

Learn to:
  * Setup security groups so instances can communicate on the network

## Single Database

Each instance now has its own database — depending on which one is receiving HTTP requests, we could end up to have some data on one version and not the
other!

We'll fix this now, by getting all instances to use the same database. The database will run on its own instance.

In the following, we will refer to the instance running the Acebook code as the **web instance** (because they're web servers), and to the instance running the MongoDB database as the **database instance**

## Launching a database instance

Launch a new instance from the AMI image named `mongodb-simple`. This will be your database instance.

You can use the `telnet` command to verify whether your web instance can reach out to the database instance on a specific port.

```bash
$ sudo yum install -y telnet

# From the web instance (here we're checking port 27017 - MongoDB's port)
$ ping IP_ADDRESS_OF_DATABASE_INSTANCE 27017
```

If your instances can't communicate, you will need to use security groups to allow traffic between them.

## Exercise

Configure your two web instances to use the correct MongoDB server (the one running on the database instance, instead of their local one).

You will know it worked if, after making these changes, you can still use the load balancer to create new posts and view them, and there is no inconsistency (you should get the same data, whichever instance the load balance picks to serve the traffic).

<details>
  <summary>How do we get the Acebook code to connect to a different database than the local one?</summary>

  You will need to set an environment variable `MONGODB_URL` so the app can connect to this different URL instead. You can do this by editing the file `package.json` and adding the environment variable on the line configuring the "start:production" script

  ```json
    "start:production": "MONGODB_URL=xyz PORT=3000 node ./bin/www",
  ``` 
</details>

You will need to do this change to each web instance.

## Reflection

Update your diagram to reflect the changes made in this section.

You had to manually update the configuration on all web instances to point to the new database. Discuss with your teams — can you see any challenges this process could cause? What if you had to update the database configuration for ten instances? Or even fifty?



[Next Challenge](07_immutable_infrastructure.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F06_external_database.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F06_external_database.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F06_external_database.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F06_external_database.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=acebook-on-aws%2Fprojects%2F06_external_database.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
