//Builds the extra tabs
function builder1($start)
{
//Append just adds the body, might be a more efficient way to add this in
//Load loads data, figure out how to integrate from the loader backend
//	$(document.getElementById("accordion")).append('<h[$start]></h[$start]><div id ="gato"><p></p></div>');

	var node1 = 'spacecrab/story/node1';
	node1 = node1 + '.node';

//Loads data parsed from the .story in the spacecrabmeat into p
	$("#gato").load(node1);


//Reloads the accordion after all this work has been done
	$('#accordion').accordion("refresh");

//Refocuses on the newest panel
	$("#accordion" ).accordion( "option", "active", 0 );
}

$( "button.startOver" )
.button()
.click(function() 
{
	window.location.reload();
});


//Builds the extra tabs
function builder3($start)
{
//Append just adds the body, might be a more efficient way to add this in
//Load loads data, figure out how to integrate from the loader backend
//	$(document.getElementById("accordion")).append('<h[$start]></h[$start]><div id ="gato"><p></p></div>');

	var node1 = 'spacecrab/story/node3';
	node1 = node1 + '.node';

//Loads data parsed from the .story in the spacecrabmeat into p
	$("#node1").load(node1);


//Reloads the accordion after all this work has been done
	$('#accordion').accordion("refresh");

//Refocuses on the newest panel
	$("#accordion" ).accordion( "option", "active", 0 );
}

$( "button.startOver" )
.button()
.click(function() 
{
	window.location.reload();
});

//Sets up accordion
$(function() 
{
	$( "#accordion" ).accordion(
	{
		collapsible: true,
		heightStyle: "content"
	});
});



//Save button which calls savesys
$( "button.save" )
.button()
.click(function() {
//Checks if browser supports this type of save
	if(typeof(Storage)!=="undefined")
		{
		// Saves data in save
				localStorage.setItem('saveCrab', ($('body').clone().html()));
				
				//Should tell what is actually in the savefile
//				alert( JSON.parse(JSON.stringify(localStorage.getItem('saveCrab'))));
		}
		// If browser dont support it, then can't save
		else
		  {
				alert("Sorry, your browser does not support web storage");
		  }
});

//Load button which loads
$( "button.load" )
.button()
.click(function() {
	//Checks if there is a save called saveCrab
	if(localStorage.getItem('saveCrab') != null)
		{
		// Loads data from variable save and replaces the body
			document.body.innerHTML = localStorage.getItem('saveCrab');

			   var body= document.getElementsByTagName('body')[0];
  var script= document.createElement('script');
   script.id = 'theend';
   script.type= 'text/javascript';
   script.src= 'spacecrabjuice.js';
   body.appendChild(script);
	
		}
		// If browser dont support it, then can't save/load
	else
	  {
			alert("Sorry, no saves detected");
	  }
});

var start = 0;
//Just a button, could remove as its for testing
 $( "button.robot" ).button().click(function() {
	builder(start);
//Unclear if this is actually do +=1
	start += 1;
});
var start = 0;
//Just a button, could remove as its for testing
 $( "button.robot1" ).button().click(function() {
	builder1(start);
//Unclear if this is actually do +=1
	start += 1;
});
var start = 0;
//Just a button, could remove as its for testing
 $( "button.robot3" ).button().click(function() {
	builder3(start);
//Unclear if this is actually do +=1
	start += 1;
});


//Builds the extra tabs
function builder($start)
{
//Append just adds the body, might be a more efficient way to add this in
//Load loads data, figure out how to integrate from the loader backend
//	$(document.getElementById("accordion")).append('<h[$start]></h[$start]><div id ="gato"><p></p></div>');

	var node1 = 'spacecrab/story/node2';
	node1 = node1 + '.node';

//Loads data parsed from the .story in the spacecrabmeat into p
	$("#node1").load(node1);


//Reloads the accordion after all this work has been done
	$('#accordion').accordion("refresh");

//Refocuses on the newest panel
	$("#accordion" ).accordion( "option", "active", 0 );
}

$( "button.startOver" )
.button()
.click(function() 
{
	window.location.reload();
});