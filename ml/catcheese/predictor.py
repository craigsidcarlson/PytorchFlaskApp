import os
import sys
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import argparse
from PIL import Image

class Predictor:

	model_names = sorted(name for name in models.__dict__
    	if name.islower() and not name.startswith("__")
	    	and callable(models.__dict__[name]))

	def __init__(self, arch='resnet18', checkpoint='static/model_best.pth.tar'):
		global args, labels
		self.model = models.__dict__[arch]()
		self.checkpoint = torch.load(os.path.join(os.path.dirname(__file__), checkpoint))
		self.model.load_state_dict(self.checkpoint['state_dict'])
		self.labels = self.checkpoint['labels']
		self.model.eval()

	def predict(self, input_image):

		print("Predicting")
		img_pil = Image.open(input_image)
		img_pil = self.removeAlpha(img_pil)
		normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

		processor = transforms.Compose([transforms.Scale(256),transforms.CenterCrop(224),
                                    transforms.ToTensor(),  normalize,])
		img_tensor = processor(img_pil)
		img_tensor.unsqueeze_(0)

		img_variable = torch.autograd.Variable(img_tensor)
		output = self.model(img_variable)
		result_index = output.data.numpy().argmax()
		result = self.labels[result_index]
		print("Result {0}".format(result))
		return result
	
	def removeAlpha(self, img_pil):
		if img_pil.mode in ('RGBA', 'LA') or (img_pil.mode == 'P' and 'transparency' in img_pil.info):
			print("removing alpha")
			alpha = img_pil.convert('RGBA').split()[-1]
			bg = Image.new("RGB", img_pil.size, (255,255,255))
			bg.paste(img_pil, mask=alpha)
			return bg
		else:
			return img_pil
