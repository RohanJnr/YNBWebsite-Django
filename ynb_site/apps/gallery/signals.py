import os


def delete_image(sender, instance, **kwargs):
	if instance.image:
		pic_path = instance.image.path
		os.remove(pic_path)
		print("Image deleted!")