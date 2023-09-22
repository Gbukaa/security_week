# Intro to JavaScript web applications

In this course, you will sometimes have to deploy web applications written in JavaScript to the Cloud.

In principle, JavaScript web apps follow the same common patterns that you find in any web app. For instance, there are routes (mapping between a URL and the code that should be executed when that URL is requested), models (mappings between your code and data in the held in a database), and views (ways to define what HTML should be sent back to the browser).

Although you won't have to develop any new features and you don't need prior experience with JavaScript in order to successfully deploy these applications, a high-level understanding of the most common libraries and tools used in the JavaScript development ecosystem will make it easier to debug deployment issues and find your way around the codebases provided in this course.

These are:

- the JavaScript language itself
- Node.js, npm and the `package.json` file
- Express

Below is a short introduction to each of these topics.

## JavaScript

JavaScript is a programming language that is commonly used to add interactivity to web pages. It is usually run in a web browser, but it can also be run on the server side using a runtime environment like Node.js.

The best source of documentation for modern JavaScript are the [Mozilla Developer Network (MDN) web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

## Node.js

[Node.js](https://nodejs.org/en/) is a JavaScript runtime that allows developers to run JavaScript on the server side, outside of a web browser. It includes a large library of common JavaScript functions and utilities that make it easier to write server-side applications in JavaScript.

### npm

[npm](https://www.npmjs.com/) (short for Node Package Manager) is a package manager for JavaScript libraries. It is the default package manager for Node.js, and it is used to install and manage packages (libraries of code) that you can use in your Node.js projects.

In this way, npm is similar to Ruby's Bundle. Packages in the Node world are the counterparts to what Ruby calls "gems". 

### The `package.json` file

Every Node project has a [`package.json`](https://docs.npmjs.com/cli/v9/configuring-npm/package-json) file at its root, which is worth knowing about as it defines a lot of useful information about how to work with the application.

A `package.json` file is used to manage the dependencies (libraries and packages of code) for a Node.js project. It contains a list of the dependencies that the project needs in order to run, as well as metadata about the project, such as the project's name, version, and description.

The `package.json` file is used by the npm package manager to install and manage the dependencies for a project. When you run the npm install command, npm reads the `package.json` file to determine which dependencies to install, and then installs them in a folder called `node_modules`.
In this regard, the `package.json` is similar to a Ruby `Gemfile`, but it provides some additional functionality beyond that.

The `package.json` file is also used to define scripts that you can run as part of your project. For example, you might define a script called "start" that runs the main module for your project, or a script called "test" that runs your project's test suite. This is where it differs from a Ruby `Gemfile`.

Overall, the `package.json` file is an important part of a Node.js project, as it helps to manage the project's dependencies and define scripts that you can use to run and maintain the project.


## Express

In this course, the JavaScript web applications you will encounter are written in [Express](https://expressjs.com/).

Express is a popular framework for building web applications in Node.js. It provides a set of functions and utilities that make it easier to build and maintain web applications, and it is designed to work seamlessly with Node.js.

One of the main features of Express is that it allows you to define routes for your application. A route is a mapping between a URL and the code that should be executed when that URL is requested. For example, you might define a route that displays a list of users when the URL "/users" is requested, or a route that creates a new user when a POST request is sent to the URL "/users".

Express also provides a number of other useful features, such as middleware functions (which allow you to modify requests and responses as they pass through your application), support for rendering HTML templates, and tools for handling form submissions and file uploads.

Overall, Express makes it easier to build and maintain web applications in Node.js by providing a simple, flexible, and powerful set of tools for building routes, handling requests and responses, and rendering templates. Its feature set is similar to that of Sinatra in the Ruby world. 

## How these tools fits together

To summarise, Node.js allows you to run JavaScript on the server side, and npm makes it easy to install and manage packages of code that you can use in your Node.js projects. Together, they provide a powerful platform for building server-side applications in JavaScript. Express is one of the popular web application frameworks built on this platform.


