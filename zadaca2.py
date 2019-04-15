import json

with open("igraci.txt", "r") as igraci_file:
    igraci_list = json.loads(igraci_file.read())

def input_player():
    first_name = input("\t- first name: ")
    last_name = input("\t- last name: ")
    height_cm = input("\t- height: ")
    weight_kg = input("\t- weight: ")
    igrac.update({"first_name": first_name, "last_name": last_name, "height_cm": height_cm, "weight_kg": weight_kg})


def input_basketball_player():
    points = input("\t- points: ")
    rebounds = input("\t- rebounds: ")
    assists = input("\t- assists: ")
    kosarkas.update({"points": points, "rebounds": rebounds, "assists": assists})


def input_football_player():
    goals = input("\t- goals: ")
    yellow_cards = input("\t- yellow cards: ")
    red_cards = input("\t- red cards: ")
    nogometas.update({"goals": goals, "yellow_cards": yellow_cards, "red_cards": red_cards})



class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

igrac = {}
kosarkas = {}
nogometas = {}

print(lebron.__dict__)


while True:
    sport = input("Unos košarkaša (1) ili nogometaša (2), (q) za prekid: ").lower()

    if sport == str(1):
        print("Basketball player:")
        input_player()
        input_basketball_player()
        kosarkas = {**igrac, **kosarkas}
        with open("igraci.txt", "a") as igraci_file:
            igraci_file.write(json.dumps(kosarkas))
            igraci_file.write("\n")

    elif sport == str(2):
        print("Football player:")
        input_player()
        input_football_player()
        nogometas = {**igrac, **nogometas}
        with open("igraci.txt", "a") as igraci_file:
            igraci_file.write(json.dumps(nogometas))

    elif sport == "q":
        break
    else:
        print("Pogrešan unos!")

print(igrac)
print(kosarkas)
print(nogometas)