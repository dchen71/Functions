// Test server utilizing express for dishes/promotions/leaders

var express = require('express');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var dishRouter = require('./dishRouter');
var leaderRouter = require('./leaderRouter');
var promoRouter = require('./promoRouter');

var hostname = 'localhost';
var port = 3000;

var app = express();

app.use(morgan('dev'));

app.use('/dishes', dishRouter)
app.use('/leaders', leaderRouter)
app.use('/promos', promoRouter)

app.use(express.static(__dirname + '/public'));

app.listen(port, hostname, function(){
  console.log(`Server running at http://${hostname}:${port}/`);
});