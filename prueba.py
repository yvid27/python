import os.path
import shutil
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files = glob.glob('*.pdf')

for filename in files:
	name = filename[0:6]

	if not os.path.exists(os.path.join(BASE_DIR, name)):
	      	os.makedirs(os.path.join(BASE_DIR, name))
	shutil.move(filename, os.path.join(BASE_DIR, name, filename))
