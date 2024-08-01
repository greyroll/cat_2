from classes.action import Action
from classes.room import Room


def long_greeting():
	return (f"Привет!\nДобро пожаловать в симулятор кота. ",
			f"Вы -- кот, ваша задача заниматься обычными кошачьими делами.",
			f"Следите, чтобы жизненные показатели котика сытость, водный баланс и бодрость не упали до 0."
			f"\nУдачи!")


def build_rooms(rooms_data: list[dict], actions_data: list[dict]) -> dict[str, Room]:
	"""
	Функция принимает 1 словарь с комнатами, 2 словарь с действиями. Возращает 3 словарь с экземплярами класса Room.
	:param rooms_data: это информация о комнате в формате
	{"name": "bedroom", "actions": ["sleep"], "available": ["living room"]}
	:param actions_data:
	:return:
	"""
	# получаем список всех действий, чтобы привязать их к комнатам
	actions: dict[str, Action] = build_actions(actions_data)
	rooms = {}
	for one_room_data in rooms_data:
		# Собираем доступные действия для 1 комнаты
		room_actions: dict[str, Action] = {}
		for action_name in one_room_data["actions"]:
			room_actions[action_name] = actions[action_name]
		#добавляем действие "уйти"
		room_actions["go to"] = Action("go to", {"bellyful": -1, "hydration": -1, "wakefulness": -1}, "")
		rooms[one_room_data["name"]] = Room(one_room_data["name"], room_actions)

	for item in rooms_data:
		rooms_available = item["available"]
		current_room_name: str = item["name"]
		current_room: Room = rooms[current_room_name]
		for room_name in rooms_available:
			available_room = rooms[room_name]
			current_room.add_locations_available([available_room])

	return rooms


def build_actions(actions_data):
	actions: dict[str, Action] = {}
	for item in actions_data:
		actions[item["name"]] = Action(**item)
	return actions


def get_room_by_name(name: str,):
	from main import rooms
	for room_name, room in rooms.items():
		if room_name == name:
			return room
