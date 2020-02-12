var express = require('express'),
  app = express(),
  port = process.env.PORT || 8000,
  bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
const consumer = require('./api/listeners/Consumer');
var routes = require('./api/routes/routes'); //importing route
routes(app); //register the route
consumer.runConsumer();
app.listen(port);