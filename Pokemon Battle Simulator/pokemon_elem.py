#st. num: 12751571
from pokemon import Pokemon
""" Args:
        Here im implementing the pokemon elements. Each Pokemontype is a Pokemon.
        Every Pokemontype has there own superattacks. Every Pokemon can based on the type
        of the enemy can inflict a greater damage and for this reason every pokemon will 
        have its own method called _damage_element. Its labelled as private variable since
        if we access the method or we manage it inconciously then it will not work as expected.
        Each Pokemonelement class will have a check_increment dummy variable. 
        This helps us to undestand if there was an actual increment or not.
"""

class PokemonGrass(Pokemon):
    def __init__(self,name,hp):
        """ Args:
                We initialize two variables name and hp. These two variables are given to the superclass
                Pokemon. Each Pokemon has a dictionary that represents the name of the attack as the 
                key and the damage as the value.
        """
        super_attack = {"Seed bomb": 10, "Mega drain": 15, "Needle arm": 20,
                        "Bullet speed": 15, "Energy Ball": 40, "Apple Acid": 25,
                        "Vine whip": 35}
        
        super().__init__(name, "Grass", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        """ Args:
                 This method has an underscore at the beginning of its name, indicating that it is intended 
                 for internal use. I consider it a method that should not be modified by the programmer, as any 
                 changes could compromise the proper functioning of the simulator.

            Return:
                   It returns the damage incremented by 1.5 if the type of the pokemon is inside the list  of 
                   enemies.                 
        """
        enemy_list = ["Water", "Rock", "Ground"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5

        return int(damage_base)
    
    
    def __str__(self):
        """ Args:
                 Here we check if the check_increment is true or false. If it is true then 
                 we can add the string that says that there was an increment. Otherwise we need
                 to stick with the base string given by the superclass Pokemon.
        """
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name} attack was super effective against {self.enemyName}\n"

        return base_str
    
    
class PokemonFire(Pokemon):

    def __init__(self, name, hp):
        super_attack = {
            "Flamethrower": 40, "Fire Spin": 30, "Ember": 20,
            "Heat Wave": 35, "Fire Blast": 50
        }

        super().__init__(name, "Fire", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Grass", "Ice", "Bug", "Steel"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonWater(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Water Gun": 20, "Bubble Beam": 25, "Hydro Pump": 45,
            "Surf": 40, "Aqua Tail": 35
        }


        super().__init__(name, "Water", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Fire", "Rock", "Ground"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonElectric(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Thunderbolt": 40, "Spark": 25, "Thunder Shock": 30,
            "Volt Tackle": 45, "Discharge": 35
        }
        super().__init__(name, "Electric", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Water", "Flying"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonRock(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Rock Slide": 35, "Stone Edge": 40, "Smack Down": 25,
            "Rock Throw": 30, "Power Gem": 45
        }
        super().__init__(name, "Rock", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Fire", "Flying", "Bug", "Ice"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonIce(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Ice Beam": 40, "Blizzard": 50, "Frost Breath": 35,
            "Aurora Beam": 30, "Icy Wind": 25
        }
        super().__init__(name, "Ice", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Grass", "Ground", "Flying", "Dragon"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonGround(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Earthquake": 50, "Mud Slap": 20, "Bulldoze": 35,
            "Dig": 40, "Sand Tomb": 25
        }
        super().__init__(name, "Ground", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Fire", "Electric", "Poison", "Rock", "Steel"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}\n"
        return base_str

class PokemonFlying(Pokemon):
    def __init__(self, name, hp):
        super_attack = {
            "Air Slash": 35, "Sky Attack": 45, "Gust": 25,
            "Hurricane": 40, "Wing Attack": 30
        }
        super().__init__(name, "Flying", hp, super_attack)
        self.check_increment = False

    def _damage_element_bonus(self, damage_base, enemy):
        enemy_list = ["Grass", "Bug", "Fighting"]
        if enemy.type in enemy_list:
            self.check_increment = True
            damage_base *= 1.5
        return int(damage_base)

    def __str__(self):
        base_str = super().__str__()
        if self.check_increment:
            base_str += f"{self.name}'s attack was super effective against {self.enemyName}"
        return base_str
    

if __name__ == "__main__":
    pokemon1 = PokemonGrass("Bulbasaur", 100)
    pokemon2 = PokemonWater("Piplup", 120)
    while pokemon1.hp > 0 and pokemon2.hp > 0:
            
            pokemon1.attack(pokemon2)
            print(pokemon1)
            if pokemon2 == 0:
                print(f"{pokemon2.name} is KO!")
                break

            pokemon2.attack(pokemon1)
            print(pokemon2)
            if pokemon1.hp == 0:
                print(f"{pokemon1.name} is KO!")
                break