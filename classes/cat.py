from classes.room import Room
from config import props_data
from function import get_room_by_name


class Cat:

	def __init__(self):
		self.props: dict = props_data
		self._location = get_room_by_name("living room")

	def __repr__(self):
		return f"Cat(bellyful={self.props["bellyful"]}, hydration={self.props["hydration"]}, wakefulness={self.props["wakefulness"]}, location={self.location})"

	@property
	def cat_props(self) -> tuple:
		return self.props["bellyful"], self.props["hydration"], self.props["wakefulness"]

	@cat_props.setter
	def cat_props(self, new_props: tuple) -> None:
		"""
		:param new_props: (bellyful, hydration, wakefulness)
		:return: None
		"""
		self.props["bellyful"] = new_props[0]
		self.props["hydration"] = new_props[1]
		self.props["wakefulness"] = new_props[2]


	@property
	def location(self):
		return self._location

	@location.setter
	def location(self, location: Room):
		self._location = location

	def apply(self, action_name: str):
		action = self.location.actions_available[action_name]
		props_change = action.props_change

		self.props["bellyful"] += props_change["bellyful"]
		self.props["hydration"] += props_change["hydration"]
		self.props["wakefulness"] += props_change["wakefulness"]
		self.limit_props()
		self.check_status()

	def go_to(self, room: Room):
		self.location = room
		self.props["bellyful"] -= 1
		self.props["hydration"] -= 1
		self.props["wakefulness"] -= 1
		self.check_status()


	def check_status(self):
		if self.props["bellyful"] < 1 or self.props["hydration"] < 1 or self.props["wakefulness"] < 1:
			print("О нет! Я умер ☠️")
			exit()

	def limit_props(self):
		self.props["bellyful"] = min(self.props["bellyful"], 5)
		self.props["hydration"] = min(self.props["hydration"], 5)
		self.props["wakefulness"] = min(self.props["wakefulness"], 5)
