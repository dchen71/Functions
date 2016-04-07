// Test server utilizing express for dishes/promotions/leaders

var express = require('express');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var dishRouter = require('dishRouter');
var leaderRouter = require('leaderRouter');
var promoRouter = require('promoRouter');

var hostname = 'localhost';
var port = 3000;

var app = express();

app.use(morgan('dev'));


app.use('/dishes', dishRouter(express))
app.use('/leaders', leaderRouter(express))
app.use('/promos', promoRouter(express))
