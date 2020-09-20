$(document).ready(function(){
    $("#info").click(function(){
		console.log("clicked");
        const url = "http://localhost:5000/add_user";
        const info = {
        	first: $('#first').val(),
        	last: $('#last').val(),
			county: $('#county').val(),
			dob: $('#dob').val(),
			email: $('#email').val(),
        };

        $s.ajax({
        	url: url,
        	type: "POST",
        	data: JSON.stringify(info),
        	processData: false,
        	contentType: "application/json; charset=UTF-8",
        	complete: function() {
        		console.log("request completed!");
        	}
        });
    });
});