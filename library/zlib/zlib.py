"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class zlib(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		#From http://www.zlib.net/
		shutit.send('mkdir -p /opt/zlib')
		shutit.send('pushd /opt/zlib')
		shutit.send('wget http://zlib.net/zlib-1.2.8.tar.gz')
		shutit.send('gunzip zlib-1.2.8.tar.gz')
		shutit.send('tar -xf zlib-1.2.8.tar')
		shutit.send('pushd zlib-1.2.8')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		shutit.send('rm -rf /opt/zlib')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return zlib(
		'shutit.tk.zlib.zlib', 0.01326125136,
		description='',
		maintainer='',
		depends=['shutit.tk.automake.automake']
	)

