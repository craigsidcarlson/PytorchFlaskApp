Welcome to Cat or Cheese

This is the full source code for Cat or Cheese. Cat or Cheese is a flask application capable of running on an AWS elastic beanstalk linux server. The application allows to to drop and image file (png, jpg, or jpeg) and the pre built model will predict if the image is a Cat or Cheese.

Also included is the pytorch convolutional neural net classifier. This code is label agnostic and can be rebuilt to any N number of catagories given train and test data is supplied. Once the model is complete the flask application can use it for prediction.

app - contains the flask application

ml - contains the machine learning code

Train and test images are not included. Recommend using http://www.image-net.org/ for image data.
