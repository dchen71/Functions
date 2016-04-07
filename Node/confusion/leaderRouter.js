// Node module to support leaders endpoint

var express = require('express');
var bodyParser = require('body-parser');

var leaderRouter = express.Router();

leaderRouter.use(bodyParser.json());

leaderRouter.route('/')
  .all(function(req,res,next) {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        next();
  })
  
  .get(function(req,res,next){
          res.end('Will send all the leaders to you!');
  })
  
  .post(function(req, res, next){
      res.end('Will add the leader: ' + req.body.name + ' with details: ' + req.body.description);    
  })
  
  .delete(function(req, res, next){
          res.end('Deleting all leaders');
  });
  
  leaderRouter.route('/:leaderId')
  .all(function(req,res,next) {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        next();
  })
  
  .get(function(req,res,next){
          res.end('Will send details of the leader: ' + req.params.leaderId +' to you!');
  })
  
  .put(function(req, res, next){
          res.write('Updating the leader: ' + req.params.leaderId + '\n');
      res.end('Will update the leader: ' + req.body.name + 
              ' with details: ' + req.body.description);
})

.delete(function(req, res, next){
        res.end('Deleting leader: ' + req.params.leaderId);
});

app.use('/leaders',leaderRouter);

app.use(express.static(__dirname + '/public'));

app.listen(port, hostname, function(){
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = leaderRouter;