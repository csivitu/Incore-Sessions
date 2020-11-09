# Node js - 
# Session 1

- Date: 09.11.2020

## Overview / Topics discussed

- What is node js and npm
- Express framework over node js
- Build a basic server
- More about node js being event-driven and async
- Create a connection to mongo db using npm library mongoose
- How to create a route to customize response to incoming requests

<hr>

### What is node js and npm
- Node.js is a free, open-sourced, cross-platform JavaScript run-time environment that lets developers write command line tools and server-side scripts outside of a browser.
- npm is the package manager for the Node JavaScript platform. It puts modules in place so that node can find them.

### Express framework
- A web framework for Node.js 
- Thanks to express being fast, unopinionated and minimalist, node js becomes much easier to use.

### Build a basic server and about node js being event-driven 

- In your command line
```
npm init
```
in your project directory to initialise the directory you are in as a node js folder.

- This creates a package.json file which looks something like this:
```
{
  "name": "note-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Pragati1610/note-app.git"
  },
  "author": "Pragati",
  "license": "ISC"
}
 ```
 
 Going back to your command line, do
 
 ```
 npm install express
 ```
 
 to include express as a dependency in our project folder.
 <br>
 You will see it get added to package.json in the dependencies as a key-value pair with it's version mentioned.
 <br>
 Now create a file to act like a server in our backend
 I'm naming it server.js
 
 The following contents go in it.
 
```javascript
const express = require('express'); // to use a library we need to require it

const app = express(); // creates an instance of app by calling express method
const port = process.env.PORT || 3000; // you can set the port to the default env or 3000

app.listen(port, () => { // creates a server to listen to port and triggers a call back function when the action is performed
    console.log(`server started at ${port}`); // body of the call back function 
});

```

Next run your server using

```
node server
```

You should see server started at 3000 printed in your terminal 
<br>
:sparkles: your first node js server


- Create a connection to mongo db using npm library mongoose
  - Get the connection link to mongo atlas
  - Create a .env to hold your env vars
  - Add the link there
  - install mongoose by:
  ```
  npm i mongoose
  ```
  - add a snippet (to connect to your db) to server.js which would finally look something like this:
  ```javascript
  const express = require('express');
  const mongoose = require('mongoose');

  mongoose.connect(process.env.DB_URL, {
      useCreateIndex: true,
      useNewUrlParser: true,
      useUnifiedTopology: true,
  }).then(() => {
      console.log('connection to db established');
  }).catch(err => {
      console.log(err)
  });

  const app = express();
  const port = process.env.PORT || 3000;


  app.listen(port, () => {
      console.log(`server started at ${port}`);
  });
  ```
 
We are almost there, one last section and you would be able to to customize your response to incoming requests
 
### How to create a route 

- Require body-parser to be able to take json data from the user
```
npm install body-parser
```

```javascript
const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const bodyparser = require("body-parser");

const authRoute = require('./routes/authRoute');

dotenv.config();

mongoose.connect(process.env.DB_URL, {
    useCreateIndex: true,
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('connection to db established');
}).catch(err => {
    console.log(err)
});

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyparser.json());

app.post('/user', (req, res)=>{  // specify the route you want to hit to when a request is sent to localhost:3000/user
  const {name} = req.body;       // destructure name from req.body and 
  res.send(`Name is ${name}`);   // send it back to the user ~ this part is the customizable, you can do whatever you want to respond the user when a request is sent to this route
});

app.listen(port, () => {
    console.log(`server started at ${port}`);
});

```


Session-2 : 
- login sign-up routes
- jwt 
- get and post routes
- testing using postman 
- patch and delete routes
- learning how to view your db using mongo dB compass
