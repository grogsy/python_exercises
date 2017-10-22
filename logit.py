

class logit(object):
	def __init__(self, func, logfile='out.log'):
		self.logfile = logfile
		self.func = func

	def __call__(self, *args, **kwargs):
		log_string = self.func.__name__ + " was called"
		print(log_string)
		print(self.func(*args, **kwargs))
		#Open the logfile and append
		with open(self.logfile, 'a') as file:
			#Now we log to the specified logfile
			file.write(log_string+ '\n')

		#Now, send a notification
		self.notify()

	def notify(self):
		#not implemented
		pass

if __name__ == '__main__':
	
	@logit
	def foo():
		print("Foo!")

	print("Calling foo()")
	foo()
	