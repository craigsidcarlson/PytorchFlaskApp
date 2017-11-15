import os,base64
from predictor import Predictor
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash, jsonify
from werkzeug.utils import secure_filename

application = app = Flask(__name__)
app.config.from_object(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png','jpg','jpeg','gif'])
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 #1MB

@app.route('/')
def render():
	global predictor
	predictor = Predictor()
	return render_template('index.html')

@app.route("/sendfile", methods=["POST"])
def send_file():
	global predictor
	if predictor is None:
		predictor = Predictor()

	result = ''
	if 'file2upload' not in request.files:
		print('No file part')
		return redirect(request.url)

	fileob = request.files["file2upload"]

	if fileob.filename == '':
		print('No selected file')
		return redirect(request.url)

	if fileob and allowed_file(fileob.filename):
		filename = secure_filename(fileob.filename)
		#result = predictor.predict(fileob)

		#Once we want to store the files on the server
		save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
		fileob.save(save_path)

		with open(save_path, "r") as f:
			result = predictor.predict(f)
		
		#try:
	        #    os.remove(save_path)
        	#except Exception as error:
            	#	app.logger.error("Error deleting file after processing", error)


	return result

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

if __name__ == "__main__":
	app.run()
