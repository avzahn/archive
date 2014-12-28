def _untar(extension_stack, output_stack):
	"""
	push the name of the unpacked
	output file and pop whatever
	extensions were dealt with off the
	extension_stack
	"""
	pass

def _tar(extension_stack, output_stack):
	"""
	same as the unpacking version, except
	pops from the opposite end of the
	extension_stack
	"""
	pass

def _unzip(extension_stack, output_stack):
	pass

def _zip(extension_stack, output_stack):
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

from os.path import exists, isfile

def parse_compress(argv):


	if len(argv) > 3:
		raise Exception('too many arguments')

	# single argument case
	if len(argv) == 2:
		if exists(argv[1]):
			# assume the user wants .tar.gz
			src_name = argv[1]
			extension_stack = ['tar','gz']
			destname = src_name + '.tar.gz'
		else:
			# starting with the file stem, add extensions
			# on one at a time until an existing
			# file is found

			found = False

			split = argv[1].split('.')
			src_stem = split[0]
			_extension_stack = split[1:]
			src = src_stem
			for i,ext in enumerate(_extension_stack):
				src += '.'+ext
				if isfile(src):
					src_name = src
					extension_stack = _extension_stack[i+1:]
					destname = argv[1]
					found = True
					break

			if found == False:
				raise Exception('input not found')

	# two argument case
	if len(argv) == 3:

		# find the argument that exists
		arg1 = argv[1]
		arg2 = argv[2]

		if exists(arg1):
			src_name = arg1
			destname = arg2
		elif exists(arg2):
			src_name = arg2
			destname = arg1
		else:
			raise Exception('input not found')

		# handle destnames of the form
		# src_name.ext0.ext1....extn
		if destname.startswith(src_name):
			extension_stack = destname[len(src_name):].split('.')
		else:
			extension_stack = destname.split('.')[1:]











	return extension_stack, src_stem, destname


from os.path import isfile

def parse_decompress(argv):

	if len(argv) > 3:
		raise Exception('too many arguments')

	src_name = None

	# will use the last intermediate file
	# as the destination if this stays None
	destname = None

	# single argument case
	if len(argv) == 2:
		src_name = argv[-1]


	if len(argv) == 3:

		arg1 = argv[1]
		arg2 = argv[2]

		# assume the source is the
		# arg that currently exists
		if isfile(arg1):
			src_name = arg1
		elif isfile(arg2):
			src_name = arg2
		else:
			raise Exception('input file not found')

		split = src_name.split('.')
		extension_stack = split[1:]
		src_stem = split[0]

	return extension_stack, src_stem, destname

from sys import exit

def usage():

	exit()


from os import remove, rename

def clean(destname, output_stack):
	"""
	delete all intermediate files
	except for the most recent one,
	which should be renamed
	"""
	if destname == None:
		destname = output_stack[-1]

	last = output_stack.pop()

	rename(last, destname)

	for f in output_stack:
		remove(f)

from sys import argv

def compress():

	output_stack = []
	parse = parse_compress

	try:
		extension_stack, src_stem, destname = parse(argv)
	except:
		usage()

	while(len(extension_stack) != 0):
		try:
			f = archivers[extension_stack[0]]
		except:
			break
		f(extension_stack, output_stack)

	clean(destname,output_stack)

def decompress():

	output_stack = []
	parse = parse_decompress

	try:
		extension_stack, srcname, destname = parse(argv)
	except:
		usage()

	while(len(extension_stack) != 0):

		try:
			f = unarchivers[extension_stack[-1]]
		except:
			break
		f(extension_stack, output_stack)

	clean(destname,output_stack)