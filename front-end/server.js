const express = require('express')
const serveStatic = require('serve-static')

const PORT = 4000

const app = express()
app.use(serveStatic(__dirname + "/dist"))

const server = app.listen(PORT)

console.log("server is running on port " + PORT)


// app.get('/', function (req, res) {
//     res.sendFile(__dirname + '/inddxex.html')
// })

//app.use(express.static('dist'))