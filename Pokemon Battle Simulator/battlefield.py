#st. num: 12751571
from pokemon_elem import *
from trainer import Trainer

class Battle(object):
    """ Args:
            This class simulates the actual battle between the two pokemons. In particular the following code
            will use attributes and methods from the Trainer class and from Pokemon:element class, present 
            respectivele in the files trainer.py and pokemon_elements.py.
    """
    def __init__(self, trainer1, trainer2):
        """ Args:
                I created two dummy trainer objects, in the battle. Furthure on the code i'll use the
                class Trainer imported from trainer.py file to create the actual trainer object.
        """
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def hasPokemon(self, trainer):
        """ 
            Args:
                The idea is when my pokemon is dead the trainer will get another pokemon to 
                fight to his team. To do this we can iterate through the pokemon_team as it's an attribute 
                of the class tratiner.

            Return:
                The method will return a boolean True/False. In particular If the method can find another pokemon
                that has more than 0 hp, then the value will be true. Othewis eit will return False.
        """
        for pokemon in trainer.pokemon_team:
            if pokemon.hp>0:
                return True
            
        else:
            return False
        
        
    def getNextPokemon(self,trainer):
        """ Args:
                This method is to get the next pokemon in the team. To do so we are using the attribute pokemon_team
                that we've created in the trainer.py file previously. Since its a private varaible we can't access
                directly to it. The only way to get information from that attribute is to access by 

            Return:
                This will return the next pokemon in the team
        """
   
        for pokemon in trainer.pokemon_team:
            if pokemon.hp>0:                return pokemon
        else:
            return None
            
    def startBattle(self):
        """ Args:
                This method starts the battle. Since the trainer 1 and trainer 2 will be some Trainer 
                objects, we can use the attributes that we've stated in the Trainer class and also the
                methods.

                The while loop check  if the returned value from the method haspokemon is true, if it is true it will run
                the code after that. It will break when one of the trainer will be without any pokemon in their team.
        """
        print(f"Battle Starts: {self.trainer1.name} vs {self.trainer2.name}\n")
        chosen_pokemon1 = self.trainer1.choosePokemon()
        chosen_pokemon2 = self.trainer2.choosePokemon()
        print(f"{self.trainer1.name} chooses {chosen_pokemon1.name}")
        print(f"{self.trainer2.name} chooses {chosen_pokemon2.name}\n")

        while self.hasPokemon(self.trainer1) and self.hasPokemon(self.trainer2):
                # Trainer 1 attack with his pokemon
                print(f"{self.trainer1.name}'s turn!")
                chosen_pokemon1.attack(chosen_pokemon2)
                print(chosen_pokemon1)

                if chosen_pokemon2.hp == 0:
                    print(f"{chosen_pokemon2.name} is KO!")
                    if self.hasPokemon(self.trainer2):
                        chosen_pokemon2 = self.getNextPokemon(self.trainer2)
                        print(f"{self.trainer2.name}: {chosen_pokemon2.name}, i choose uuu!\n")
                    else:
                        print(f"{self.trainer2.name} is out of Pokemon!")
                        print(f"{self.trainer1.name} wins!")
                        break

                # Trainer 2 attack with his pokemon
                print(f"{self.trainer2.name}'s turn!")
                chosen_pokemon2.attack(chosen_pokemon1)
                print(chosen_pokemon2)

                if chosen_pokemon1.hp == 0:
                    print(f"{chosen_pokemon1.name} is KO!")
                    if self.hasPokemon(self.trainer1):
                        chosen_pokemon1 = self.getNextPokemon(self.trainer1)
                        print(f"{self.trainer1.name}: {chosen_pokemon1.name}, i choose uuu!\n")
                    else:
                        print(f"{self.trainer1.name} is out of Pokemon!")
                        print(f"{self.trainer2.name} wins!")
                        break

if __name__ == "__main__":
    trainer1 = Trainer("Ash")
    trainer2 = Trainer("Brook")

    trainer1.addPokemon(PokemonElectric("Pikachu",100))
    trainer1.addPokemon(PokemonFire("Flameon",120))
    trainer2.addPokemon(PokemonGrass("Psyduck",120))
    trainer2.addPokemon(PokemonWater("Piplup",100))

    battle = Battle(trainer1, trainer2)
    battle.startBattle()

####################
#TO DO: 
# The implementation is fine. The choosing system is random, since is random even if the input size
#increase the complexity stays O(1) on avarage. Need to change the random system in a way such that the user can
#can choose. Need to consider the complexity in this case
###################
#Suggestion:
#Consider using the python library PyGame to implement it

