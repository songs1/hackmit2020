$(document).ready(function(){
	$( "#voter-form" ).submit(function( event ) {
		event.preventDefault();
	});
    $("#info").click(function(){
        const url = "http://localhost:5000/add_user";
        const info = {
        	first: $('#first').val(),
        	last: $('#last').val(),
			county: $('#county').val(),
			dob: $('#dob').val(),
			email: $('#email').val(),
        };
		
        $.ajax({
        	url: url,
        	type: "POST",
        	data: JSON.stringify(info),
        	processData: false,
        	contentType: "application/json; charset=UTF-8",
        	success: function(foundAcct) {
        		if (foundAcct === "yes") {
					console.log("yes")
				}
				if (foundAcct === "no") {
					console.log("no")
				}
        	}
        });
    });
});