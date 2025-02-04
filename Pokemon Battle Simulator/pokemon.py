#st. num: 12751571
import random
class Pokemon(object):
    def __init__(self, name, type, hp, special_attacks):
        """ In this method we initialize an object pokemon. This will be a blueprint
            for the future pokemons that our user will create. The pokemon object has a:
            
                - name --> name of the pokemon

                - type --> type of the pokemon, this is important because based on this the 
                          the life of the pokemon will depend

                - hp --> life of the pokemon 

                - initial_hp --> the initial hp of the pkemon because we need to compute the life 
                                 percentage

                - special_attack --> Every pokemon will have some special attacks. This will be
                                     implemented is a dictionary in the respective pokemon type classes.

                The other attributes are made to save the information during the attack so we can register
                the attack once done with the python reserved method __str__().
        """
        self._name = name
        self._type = type
        self._hp = hp
        self._initial_hp = hp
        self._special_attacks = special_attacks
        
        # Variables to save the information of the attack
        self.lastAttack = None
        self.lastDamage = None
        self.enemyName = None
        self.enemyHP = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_hp(self):
        return self._hp

    def set_hp(self, value):
        self._hp = max(0, value)  

    def get_special_attack(self):
        return self._special_attacks

    def set_special_attack(self, special_attacks):
        self._special_attacks = special_attacks

    
    def choose_attack(self):
        """ This will allow the pokemon to randomly choose a special attack."""
        attack = random.choice(list(self._special_attacks)) #randomly choose an attack from a dic that is casted
        damage = self._special_attacks[attack]

        return attack,damage
    
    def _damage_element_bonus(self, damage_base, enemy):
        """ Args:
                This is the damage element method. Since normal type pokemon will not have
                an element bonus then it return the damage. However in the subclasses, this
                method will change the final damage inflicted because some pokemon inflict
                more damage to those that are from a certain type of element. I need this because 
                the value damage here will be returned to the attack method. 
                Even tho here is nothing changed in the subclass there will some changes.

        """
        return damage_base
    
    def _remaining_hp(self, damage):
        """Args:
                This will compute the final life(hp) of the pokemon after every attack.
                We use the max function because it might occur that the life goes negative
                when we substract. To avoid negative values we use max between 0 and the damage value.
                As we want to compute that ad a percentage we divide it to the initial hp and do *100

            Return:
                It will return the amount of damage inflicted in percentage and rounded by 2 deciimal places.
        """
        self._hp = max(0, self._hp - damage)
        damage_inflicted = round((self._hp/self._initial_hp) * 100,2)
        return damage_inflicted
    
    
    def attack(self, enemy):
        """ Args:
                In this method the pokemon attack the other one. We compute take the basic damage
                defined by the dictionary. Once done that we give that to the function damage element bonus
                because every pokemon can be stronger if they have against a certain type of pokemon.
                After we've computed that we start to save our pokemon moves inside some variables so we can
                take track of what is going on.

            Given: 
                To this method as input is given a enemy variable. This is necessery if we want to take track
                of the information of the enemy pokemon as well. To do this we are using the dummy variabels
                initialized before:

                    self.enemyName --> gets enemy name
                    self.enemyHp --> gets enemy hp

            Return:
                The attack method call the function string which will return the output, which will be ideally a 
                report of the battle.
                The main variables involved apart from the previous already mentioned are:

                    self.lastAttack --> take track of the attack of the pokemon
                    self.lastDamage --> take trake of the damage, in particular this variable can vary to pokemon to pokemon
        """
        #calculating damage and memorizinsg 
        attack,damage_base = self.choose_attack()
        damage = self._damage_element_bonus(damage_base,enemy)
           
        #memoriziing the information durinf the attack
        self.lastAttack = attack
        self.lastDamage = damage
        self.enemyName = enemy.get_name()
        self.enemyHP = enemy._remaining_hp(damage)

        return str(self)
    
    
    def __str__(self):
        """ Args:
                This the main output of the pokemon game. It will every time return how the pokemon move
                we have also a seperator variable, which is used to seperate the strings after the 
                first pokemon move.
                We use strip method after that to get rid of the extra line that would occur in the other
                case

            Return:
                The string method will return first of all a seperator, we need this to seperate every move
                made by the respective pokemon. 
                After we make sure that the dummy variables are not type None, beacause other wise it will raise 
                an error.

        """
        seperator = "---------------------------⚔-----------------------------\n"
        if self.lastAttack and self.lastDamage and self.enemyName and self.enemyHP is not None:
            return(f"{seperator}"
                   f"{self._name} uses {self.lastAttack}! --- Damage done|-> {self.lastDamage}% \n"
                   f"{self.enemyName} is left with {self.enemyHP}% of HP\n")
        
        else:
            return"Error"
        
    name = property(get_name, set_name)
    type = property(get_type, set_type)
    hp = property(get_hp, set_hp)
    special_attack = property(get_special_attack, set_special_attack)


if __name__ == "__main__":
    pikachu_attacks = {'Thunder Shock': 40, 'Quick Attack': 30}
    bulbasaur_attacks = {'Vine Whip': 45, 'Tackle': 20}

    p1 = Pokemon("Pikachu", "Elettric", 100, pikachu_attacks)
    p2 = Pokemon("Bulbasaur", "Grass", 120, bulbasaur_attacks)

    #getting pokemon 1 name
    print(p1.name)
    #getting pokemon 2 type
    print(p2.type)


    p1.name = "Pikachuu"
    print(p1.name)
    #fight simuation
    while p1.hp > 0 and p2.hp > 0:
            #p1 attack
            p1.attack(p2)
            print(p1)
            if p2.hp == 0:
                print(f"{p2.name} is KO!")
                break

            #p2 attack
            p2.attack(p1)
            print(p2)
            if p1.hp == 0:
                print(f"{p1.name} is KO!")
                break