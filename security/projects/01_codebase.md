# The Poochie Pals codebase

## On application security

We can start looking for security vulnerabilities by first inspecting the codebase. Some common security flaws can already be prevented by using certain patterns in the code — for example, sanitising user input to prevent [injections](https://owasp.org/Top10/A03_2021-Injection/).

Because we have access to the code and the internals of the application, this is called "white box" or "clear box" testing.

## The project

The engineering team worked on a new version of the website. They're planning to release it next week, giving you some time to investigate any security issues.

So far, you've only got the codebase. It's an JavaScript / [Express](https://expressjs.com/) application.

[Here is the link to the codebase](https://gitlab.com/makers-students/poochie-pals-webapp).

<details>
<summary>But... I don't know JavaScript!</summary>

That's OK. It's very common to find organisations using different languages across different teams and products or software components. Each team is usually responsible to make sure their software is exempt from security vulnerabilities, but we can still inspect what the application is doing at a high-level, without necessarily focusing on the details. Some common security flaws can be similar from one technology to another.
</details>

### What you should do

Investigate the codebase and list some vulnerabilities you've found.

### How to search for vulnerabilities?

 1. Review the code and research some common problems you already know about — for example, a hardcoded secret key, or HTTP client parameters which have not been sanitised or validated.
 2. Research the technology used by the engineering team (here, Express) — the benefits of using popular open-source libraries is that a lot of experienced engineers worked to document and prevent security issues these libraries can cause when badly configured. [Here's an example of Google results for searching "Common security vulnerabilities Python Django"](https://www.google.com/search?q=common+security+vulnerabilities+python+django)
 3. Use an automated SAST tool for the language and technology you're working with, such as Bearer (see below).

#### Using Bearer

[Bearer](https://github.com/bearer/bearer) is a tool to automatically analyse our code to check for potential problems (this is called a static analysis tool, or SAST tool).
```bash
brew install bearer/tap/bearer

# cd into project directory
cd poochie-pals

# Launch scan
bearer scan .
```

You might not fully understand the different issues detected at this stage — that's OK. Each issue listed also contains a link which describes the issue in more details, if you want to learn a bit more.

## What to do after

Investigating the codebase is a good start, and quite a lot of issues can be fixed by doing this. However, as you probably know, deploying software to users will involve a lot more than just the code. In a whole system deployed on the cloud, vulnerabilities could come from:
 * Insecure network configuration — attackers could exploit this to get access to private networks or specific machines.
 * Permissions which are too open — access to a resource should be limited to the strict minimum.
 * Overloading the system with traffic — this can cause Denial of Services (DDoS) attacks, where the application becomes unusable.

Your team will now work on investigating these vulnerabilities in a deployed application.

[Next Challenge](02_deployment.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fprojects%2F01_codebase.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fprojects%2F01_codebase.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fprojects%2F01_codebase.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fprojects%2F01_codebase.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fprojects%2F01_codebase.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
