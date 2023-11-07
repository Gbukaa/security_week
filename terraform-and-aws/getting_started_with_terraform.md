# Getting Started With Terraform

Terraform provides some pretty decent introductory materials, so I'm not going to duplicate their efforts by building an intro from scratch but I am going to provide some supporting content.

Some of the content here are corrections which were needed as of 23/10/2022. If you're reading this a long time after that date, Terraform might have updated their docs and removed the mistakes. If that is the case, please let us know to correct the corrections :)

## Using the Terraform Docs

Start [here](https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code?in=terraform/aws-get-started) and work through the 8 sections. This will give you a gentle introduction to the basics of creating and managing resources.

#### Do
- Ask yourself questions and write them down
    - "How" and "Why" questions are especially encouraged
- Bring your questions to peer group check ins
- Watch the video AND read the text, if you have the energy / focus for that

#### Do not
- Copy/Paste code (even when the tutorial tells you to)
- Feel that you have to memorise the syntax
- Expect yourself to be a Terraform wizard by the end of the week

## Corrections, Tips and Questions

### Step 1: What is infrastructure as code with Terraform?

- What are the advantages of using Terraform?
- Can you think of one additional advantage, beyond those listed in the docs?

### Step 2: Install Terraform

The image is declared using a deprecated tag (`.latest`)

```
    image = docker_image.nginx.latest
```

Use `.image_id` instead

```
    image = docker_image.nginx.image_id
```

Then make sure the version of Terraform is `2.22.0` or above.

```
   version = "2.22.0"
```

#### Are you already tired of typing out `terraform`? If so, create an alias!
To do this, open up your `.zshrc` file and..
- If you installed terraform using homebrew,  add `alias tf="/opt/homebrew/bin/terraform"` on a new line.
- If you installed terraform another way, or the above doesn't work, replace `"/usr/local/bin/terraform"` with the path shown when you do `whereis terraform`.

Then open a new terminal session to load the new alias. Now, instead of writing out `terraform` every time you want to use a terraform command, you can do `tf` instead ;)

### Step 3: Build infrastructure

The Amazon Machine Image (AMI) `ami-830c94e3` is invalid. Change it to `ami-0648ea225c13e0729`. This alternative came from the [AMI Catalogue](https://eu-west-2.console.aws.amazon.com/ec2/home?region=eu-west-2#AMICatalog:) :)

> Optional extension: Add a new `resource` to your `main.tf` so that when you run `terraform apply` a S3 bucket is created in addition to your EC2 instance.

QUESTION: Do the values used for resource type (e.g. `aws_instance`) and resource name (e.g. `app_server`) matter? What happens if you change them to something else? 

### Steps 4: Change infrastructure

- What are the key learning points here?
- Why do some changes require a resource to be destroyed?

### Step 5: Destroy infrastructure

- What are the key learning points here?
- Can you describe one benefit of being able to destroy infrastructure via Terraform?

### Step 6: Define input variables

- Can you describe one benefit of using Terraform variables?

### Step 7: Query data with outputs

TIP: You might find that when you're declaring outputs, VSCode offers some helpful autocompletion options. Don't dwell on this as it's definitely not essential but if you do see those suggestions in VSCode, explore them a little.

### Step 8: Store Remote State

- What is Terraform state?
- Why would you want to store Terraform state in the cloud?

The written docs use `backend "remote" { ... }` and the video uses `cloud { ... }`. I used the latter but only because it looks neater. So if you want to do something that will definitely work, use `cloud { ... }`. If you decide that you want to try both and get into a bit of a mess, don't spend more than 15 minutes trying to figure it out :)

There are quite a few options for storing Terraform state in the cloud. In this week's main challenge, you'll use a [S3 bucket](https://developer.hashicorp.com/terraform/language/settings/backends/s3).

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/getting_started_with_terraform.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/getting_started_with_terraform.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/getting_started_with_terraform.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/getting_started_with_terraform.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=devops-course&prefill_File=terraform-and-aws/getting_started_with_terraform.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
