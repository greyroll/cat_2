from classes.cat import Cat
from classes.room import Room
from classes.ui import UI
from config import rooms_data, actions_data
from function import long_greeting, build_rooms, get_room_by_name
from main import rooms

cat = Cat()

def test_props():
	cat.go_to("kitchen")
	print(cat.props)


def test_long_greeting():
	for element in long_greeting():
		print(element)


def test_build_rooms():
	print(build_rooms(rooms_data, actions_data))


def test_get_room_by_name():
	print(get_room_by_name("living room"))


def test_check_status():
	cat.cat_props = (1, 1, 1)  # bellyful, hydration, wakefulness
	print(cat.go_to("living room"))


def test_cat_location():
	print(cat.location)


def test_make_location_message():
	print(UI.location_message(get_room_by_name("living room")))


def test_make_actions_available_message():
	print(UI.actions_available_message(get_room_by_name("living room")))


def test_go_to():
	cat.go_to("kitchen")
	print(cat.location)
	print(cat.props)


def test_apply():
	cat.go_to("kitchen")
	cat.apply("eat")
	print(cat.props)


def test_current_props_message():
	cat.go_to("bedroom")
	print(UI.current_props_message(cat))


def test_ui_locations_available():
	print(UI.locations_available_message(get_room_by_name("living room")))


def test_get_user_choice_action():
	location = get_room_by_name("living room")
	print(UI.get_user_choice_action(location, 2))


def test_get_user_choice_location():
	location: Room = get_room_by_name("living room")
	print(UI.locations_available_message(location))
	print(UI.get_user_choice_location(location, 2))
