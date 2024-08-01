from classes.action import Action
from config import rooms_data, actions_data
from function import long_greeting, build_rooms
from classes.cat import Cat
from classes.room import Room
from classes.ui import UI

rooms: dict[str, Room] = build_rooms(rooms_data, actions_data)
cat = Cat()
print(long_greeting())
while True:
	print(UI.current_props_message(cat))
	print(UI.location_message(cat.location))
	print(UI.actions_available_message(cat.location))
	print("Введите номер действия")

	user_choice = int(input())

	chosen_action: Action = UI.get_user_choice_action(cat.location, user_choice)

	if chosen_action.name == "go to":
		print(UI.locations_available_message(cat.location))
		print("Введите номер комнаты")
		user_choice_room = int(input())
		chosen_room: Room = UI.get_user_choice_location(cat.location, user_choice_room)
		cat.go_to(chosen_room)
	else:
		cat.apply(chosen_action.name)


