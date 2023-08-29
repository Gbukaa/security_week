# Learn about common security flaws

This repository contains small, self-contained Python + Flask web applications.

Each of them introduces a different type of common security flaw.

There are many other potential vulnerabilities, depending on the technology you use,
the libraries or frameworks, and the infrastructure you deploy your application with.

## Setup

First do this:

```
pip3 install -r requirements.txt
```

## How to progress

Then go to `0_static_app.py` to get started.

Each file is a small Flask web application containing a common security
vulnerability. Comments are present in each file to give more details about it.

## Going further

These examples only provide a tiny fraction of potential security problems in an application codebase. [The OWASP Top Ten](https://owasp.org/www-project-top-ten/) lists the ten most common vulnerabilities found in software, and is updated regularly. Each vulnerability provides more details and a list of examples in which it could be exploited.

<details>
<summary>What's OWASP?</summary>

Taken from Wikipedia:

> The Open Worldwide Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security. The OWASP provides free and open resources. It is led by a non-profit called The OWASP Foundation.

</details>

## Solutions to the last exercise

Only read below if you've attempted to find the problems present in the last application (`7_exercise.py`)

<details>
<summary>Reveal solution</summary>

 * The email is still present in the HTML, even if not visible directly on the page. Someone could simply use the developer tools to read the HTML, and get people's emails from there.
 * The user input is not validated to prevent injections, such as JavaScript injections.
 * The route to delete all messages is still reachable by anyone — an attacker could guess the URL with some trial and error, then use something than `curl` or Postman to send a DELETE request to that route, and delete all messages.
 * The debug mode is enabled, which means any error from the application could be shown to a user, disclosing technical details which could be used by an attacker.
</details>



<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fvulnerabilities_project%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fvulnerabilities_project%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fvulnerabilities_project%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fvulnerabilities_project%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdevops-course&prefill_File=security%2Fvulnerabilities_project%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
