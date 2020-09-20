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
					window.location.href = "/form-submit"
				}
				if (foundAcct === "no") {
					alert("Oops! We couldn't find your registration.\nPlease make sure you've filled out the form correctly and your registration information can be found at mvp.sos.ga.gov.")
				}
        	}
        });
    });
});