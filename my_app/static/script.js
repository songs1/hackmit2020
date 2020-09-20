$(document).ready(function(){
    $("#info").click(function(){
        const url = "http://localhost:5000/add_user";
        const info = {
        	first: $('#first').val(),
        	last: $('#last').val(),
			dob: $('#dob').val(),
			county: $('#county').val(),
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
