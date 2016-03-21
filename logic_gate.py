"""
Using classes and class inheritance to make logic gates.
Pretty cool stuff.
"""

class LogicGate:

	def __init__(self, label):
		self.label = label
		self.output = None

	def get_label(self):
		return self.label

	def get_output(self):
		self.output = self.perform_gate_logic()
		# we do not define perform_gate_logic here because each logic gate
		# does something different. It's ok to refer to something that will
		# appear in child classes but doesn't exist in the parent class.
		return self.output


class BinaryGate(LogicGate):

	def __init__(self, label):
		LogicGate.__init__(self, label)

		self.pinA = None
		self.pinB = None

	def get_pinA(self):
		return int(input("Enter Pin A input for gate "
			+ self.get_label() + "--> "))

	def get_pinB(self):
		return int(input("Enter Pin B input for gate "
			+ self.get_label() + "--> "))

class UnaryGate(LogicGate):

	def __init__(self, label):
		LogicGate.__init__(self, label)

		self.pin = None

	def get_pin(self):
		return int(input("Enter Pin input for gate " +
			self.get_label + "-->"))
