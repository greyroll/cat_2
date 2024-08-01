props_data = {"bellyful": 5, "hydration": 5, "wakefulness": 5}

rooms_data = [
	{"name": "bedroom", "actions": ["sleep"], "available": ["living room"]},
	{"name": "kitchen", "actions": ["eat", "drink"], "available": ["living room"]},
	{"name": "living room", "actions": ["sleep"], "available": ["kitchen", "bedroom"]},
]

actions_data = [{
	"name": "eat",
	"props_change": {"bellyful": 3, "hydration": -1, "wakefulness": -1},
	"message": ""
	}, {
	"name": "drink",
	"props_change": {"bellyful": -1, "hydration": 3, "wakefulness": -1},
	"message": ""
	}, {
	"name": "sleep",
	"props_change": {"bellyful": -1, "hydration": -1, "wakefulness": 3},
	"message": ""
},]

eng_ru = [{
	"actions": {
		"eat": "кушац",
		"drink": "пить",
		"sleep": "спать 😴",
		"go to": "уйти"
	}
}, {
	"places": {
		"bedroom": "спальня",
		"kitchen": "кухня",
		"living room": "гостинная"
	}
}, {
	"props": {
		"bellyful": "сытость",
		"hydration": "водный баланс",
		"wakefulness": "бодрость"
	}
}
]