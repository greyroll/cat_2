from classes.action import Action
from classes.cat import Cat
from classes.room import Room
from config import eng_ru

locations_dict: dict = {}
actions_dict: dict = {}
props_dict: dict = {}

for dictionary in eng_ru:
	for topic, translation in dictionary.items():
		if topic == "places":
			locations_dict: dict = translation
		if topic == "actions":
			actions_dict: dict = translation
		if topic == "props":
			props_dict: dict = translation


class UI:

	@staticmethod
	def translate_locations(location: Room) -> dict[int, str]:
		locations_names = location.get_locations_names()
		locations_translated = {}

		n = 1
		for location_name in locations_names:
			locations_translated[n] = locations_dict[location_name]
			n += 1
		return locations_translated

	@staticmethod
	def locations_available_message(location: Room):
		locations_translated = UI.translate_locations(location)

		message = "Доступные комнаты:\n"
		for number, location in locations_translated.items():
			message = message + str(number) + f". {location}\n"
		return message

	@staticmethod
	def translate_actions(location: Room) -> dict[int, str]:
		actions: dict[str, Action] = location.actions_available

		actions_names: list[str] = []
		for action in actions.values():
			actions_names.append(action.name)

		actions_translated: dict[int, str] = {}
		n = 1
		for action_name in actions_names:
			actions_translated[n] = actions_dict[action_name]
			n += 1
		return actions_translated

	@staticmethod
	def actions_available_message(room: Room):
		actions_translated = UI.translate_actions(room)
		message = "Доступные действия:\n"
		for number, action in actions_translated.items():
			message = message + str(number) + f". {action}\n"
		return message

	@staticmethod
	def current_props_message(cat: Cat):
		current_props: dict = cat.props
		props_translated: dict[str, int] = {}
		for name, value in current_props.items():
			props_translated[props_dict[name]] = value

		message = ""
		for name, value in props_translated.items():
			message = message + "\n" + f"{name}: " + str(value)
		return message

	@staticmethod
	def location_message(location: Room):

		place = ""
		if location.name == "living room":
			place = locations_dict["living room"]
		if location.name == "kitchen":
			place = locations_dict["kitchen"]
		if location.name == "bedroom":
			place = locations_dict["bedroom"]

		return f"Ваше местоположение: {place}"



	@staticmethod
	def get_user_choice_action(location: Room, user_choice: int):

		options_available = UI.translate_actions(location)
		user_option: str = ""
		for number, option in options_available.items():
			if number == user_choice:
				user_option = option

		action_name = ""
		for eng, ru in actions_dict.items():
			if ru == user_option:
				action_name = eng

		actions_available: dict[str, Action] = location.get_actions_available()
		chosen_action: Action | None = None
		for name, action in actions_available.items():
			if name == action_name:
				chosen_action = action

		return chosen_action

	@staticmethod
	def get_user_choice_location(location: Room, user_choice: int) -> Room:

		locations_available = UI.translate_locations(location)
		user_option_ru = ""
		for number, location_name_ru in locations_available.items():
			if number == user_choice:
				user_option_ru = location_name_ru

		location_name_eng = ""
		for eng, ru in locations_dict.items():
			if ru == user_option_ru:
				location_name_eng = eng

		chosen_location: Room | None = None
		for room in location.get_locations_available():
			if location_name_eng == room.name:
				chosen_location = room

		return chosen_location