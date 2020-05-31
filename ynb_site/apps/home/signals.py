from django.core.exceptions import ValidationError


def limit_instances(sender, instance, created, *args, **kwargs):
	"""Check if more than 1 instance(s) is/are being created."""
	if created:
		raise ValidationError("There can only be 1 instance of this model.")
