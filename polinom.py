class polinom:
	def poly_al(self,second,once,constant):
		self.second = second
		self.once = once
		self.constant = constant
	def poly_al_1(self,second_1,once_1,constant_1):
		self.second_1 = second_1
		self.once_1 = once_1
		self.constant_1 = constant_1
	
	
	def poly_print(self):
		print 'first polynom: ',self.second,'x^2','+',self.once,'x','+',self.constant,
		print '\n','Second polynom:',self.second_1,'x^2','+',self.once_1,'x','+',self.constant_1
	
	def sum(self):
		self.new_s =  self.second+self.second_1
		self.new_o = self.once+self.once_1
		self.new_c =self.constant + self.constant_1
	def sub(self):
		self.new_s =  self.second-self.second_1
		self.new_o = self.once-self.once_1
		self.new_c =self.constant - self.constant_1
	def poly_expr(self):
		print self.new_s,'x^2','+',self.new_o,'x','+',self.new_c
        
