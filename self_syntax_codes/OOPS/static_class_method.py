class Foo(object):
	@staticmethod
	def bar(x):
		print x
	@classmethod
	def spam(cls):
		print cls
		

Foo.bar(3)
Foo.spam()