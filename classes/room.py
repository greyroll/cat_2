from classes.action import Action



class Room:
	def __init__(self, name, actions):
		self.name = name
		self.actions_available: dict[str, Action] = actions
		self.locations_available: list[Room] = []

	def get_locations_names(self):
		return [location.name for location in self.locations_available]

	def __repr__(self):
		return f"Room(name={self.name}, actions_available = {self.actions_available}, locations_available={self.get_locations_names()})"

	def get_locations_available(self):
		return self.locations_available

	def get_actions_available(self):
		return self.actions_available

	def add_locations_available(self, rooms: list["Room"]):
		self.locations_available.extend(rooms)



