installed via npm-y. We can close our server via ctrl + c. 

We can use express to [[host servers]]. Some sample boiler plate code for this is:

```
const express = require('express')
const app = express()
```
Where we create our app. 

We also want to be able to connect to a local host:
```
app.listen(3000)
```
We connect to the site: "http://localhost:3000"

We also want to add a script under our [[package.json]] file called "devStart" which uses [[nodemon]] to start up our server and connect here. 

---
# App Get 
A common request to make is a get request. We have two variables we really want to work with here, a request and a response. The response is what the user sees, and the request contains info sent to the server Some standard boiler plate for this is:

```
app.get("/",(req,res) =>{

    console.log('Here')

    // res.status(500).send("hi")

    // res.send("Hi")

  

    //we can also send stuff to user to download

    res.download("server.js")
})
```

We also have several response functions, we can send [[status codes]] back to the user, we can send download requests, and send messages back. 

Importantly, we can also render [[HTML]] files. We would typically write:

```
app.get("/",(req,res) =>{
    res.render("index")
})
```
Index typically lives in a "views" folder. We need to specify a [[view engine]] takes data and an html file and produces a complete [[HTML]] page. 

We will use [[ejs]], which can be installed via npm i ejs. 

---
# Router Function
[[express.js]] implements a [[router]] feature that allows us to 