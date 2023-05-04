import random

class Superhero:
    def __init__(self, name, strength, speed, intelligence, durability):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence
        self.durability = durability

    def get_stats(self):
        return f"{self.name}: Str {self.strength}, Spd {self.speed}, Int {self.intelligence}, Dur {self.durability}"

    def __repr__(self):
        return f"<Superhero: {self.name}>"

class SuperheroTeam:
    def __init__(self, name):
        self.name = name
        self.members = set()
        self.enemies = set()

    def add_member(self, member):
        self.members.add(member)

    def add_enemy(self, enemy):
        self.enemies.add(enemy)

    def get_members(self):
        return self.members

    def get_enemies(self):
        return self.enemies

    def __repr__(self):
        return f"<SuperheroTeam: {self.name}>"

class SuperheroUniverse:
    def __init__(self):
        self.superheroes = []
        self.teams = []

    def add_superhero(self, superhero):
        self.superheroes.append(superhero)

    def create_team(self, name):
        team = SuperheroTeam(name)
        self.teams.append(team)
        return team

    def get_superheroes(self):
        return self.superheroes

    def get_teams(self):
        return self.teams

def generate_random_superhero():
    name = random.choice(["Iron Man", "Spider-Man", "Captain America", "Thor", "Hulk", "Black Widow", "Scarlet Witch", "Doctor Strange", "Ant-Man", "Black Panther", "Captain Marvel", "Vision"])
    strength = random.randint(1, 10)
    speed = random.randint(1, 10)
    intelligence = random.randint(1, 10)
    durability = random.randint(1, 10)
    return Superhero(name, strength, speed, intelligence, durability)

def generate_random_teams_and_relationships(universe):
    team_names = ["Avengers", "X-Men", "Justice League", "Suicide Squad", "Fantastic Four", "Guardians of the Galaxy", "Defenders", "Young Avengers", "Thunderbolts", "X-Force"]

    for i in range(10):
        superhero = generate_random_superhero()
        universe.add_superhero(superhero)

    for i in range(10):
        team_name = random.choice(team_names)
        team = universe.create_team(team_name)

        for j in range(3):
            member = random.choice(universe.get_superheroes())
            team.add_member(member)

        for j in range(3):
            enemy = random.choice(universe.get_superheroes())
            team.add_enemy(enemy)

if __name__ == "__main__":
    universe = SuperheroUniverse()
    generate_random_teams_and_relationships(universe)

    print("Superheroes:")
    for superhero in universe.get_superheroes():
        print(superhero.get_stats())

    print("\nTeams:")
    for team in universe.get_teams():
        print(f"{team.name}:")
        print("Members:", [member.name for member in team.get_members()])
        print("Enemies:", [enemy.name for enemy in team.get_enemies()])

