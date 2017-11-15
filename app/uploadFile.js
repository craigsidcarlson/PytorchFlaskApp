var dropHandler = function(evt) {
	evt.preventDefault();
	var files = evt.originalEvent.dataTransfer.files;

	var formData = new FormData();
	formData.append("file2upload, files[0]);

	var req = {
		url: "/sendfile",
		method: "post",
		processData: false,
		contentType: false,
		data: formData
	};

	var promise = $.ajax(req);
};
