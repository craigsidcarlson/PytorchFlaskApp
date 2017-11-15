$(function() {
	var dropHandler = function(evt) {
		evt.preventDefault();
		console.log("Drop");
		var sound = new Audio("static/audio/beepboop.wav");
		sound.play();
		var files = evt.originalEvent.dataTransfer.files;
		
		var formData = new FormData();
		formData.append("file2upload", files[0]);
		
		var req = {
			url: "/sendfile",
			method: "post",
			processData: false,
			contentType: false,
			data: formData
		};
		
		var promise = $.ajax(req);
		promise.then(fileUploadSuccess, fileUploadFail);
	};

	var fileUploadFail = function(data){
		console.log("failure");
	};

	var fileUploadSuccess = function(data) {
		console.log("Success");
		if (data == "cat") {
			$('#secondContainer').animate({width: 'show'},2000);
		} else {
			$('#secondContainer').animate({width: 'hide'},2000);
		}
	};

	var dragHandler = function(evt) {
		evt.preventDefault();
	};

	var dropHandlerSet = {
		dragover: dragHandler,
		drop: dropHandler,
	};

	$(".bg").on(dropHandlerSet);
	fileUploadSuccess(false);
});	

