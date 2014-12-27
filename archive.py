def _untar(fname, extension_stack, output_stack):
	"""
	push the name of the unpacked
	output file and pop whatever
	extensions were dealt with off the
	extension_stack
	"""
	pass

def _tar(fname, extension_stack, output_stack):
	pass

def _unzip(fname, extension_stack, output_stack):
	pass

def _zip(fname, extension_stack, output_stack):
	pass

def reverse_dict(d):
	pass
 
archivers = {'bz2':_tar,
			'xz.':_tar,
			'gz':_tar,
			'tar':_tar,
			'zip':_zip}

unarchivers = {'bz2':_untar,
			'xz':_untar,
			'gz':_untar,
			'tar':_untar,
			'zip':_unzip}

reverse_archivers = reverse_dict(archivers)
reverse_unarchivers = reverse_dict(unarchivers)

output_stack = []

extension_stack = []

def parse(user_string):
	return extension_stack, srcname, destname

def 