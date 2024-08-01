class Action:
	"""
	Здесь информация про класс Action  и как с ним работать
	"""
	def __init__(self, name, props_change, message):
		self.name = name
		self.props_change = props_change
		self.message = message

	def __repr__(self):
		return f"{self.__class__.__name__}(name={self.name}, props_change={self.props_change}, message={self.message})"