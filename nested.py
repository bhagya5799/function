def outfn(text):
	def infn():
		print(text)
	infn()
outfn('hello')