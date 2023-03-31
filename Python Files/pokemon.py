#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.



class Pokemon():
    lista_IDs=[]
    def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        
        if ID not in Pokemon.lista_IDs:
            pass
        else:
            raise ValueError("Este ID pertenece a otro pokemon")
        if isinstance(ID, int)==True:
            pass
        else:
            raise TypeError("El ID debe ser un entero")

        if isinstance(nombre, str)==True:
            pass
        else:
            raise TypeError("El nombre debe ser una cadena de texto")
        
        if isinstance(tipo_arma, Tipo_arma)==True:
            pass
        else:
            raise TypeError("El el tipo de arma debe ser uno de estos 4: punch, kick, elbow o headbutt")

        if isinstance(salud, int)==True and salud>=1 and salud <=100:
            pass
        else:
            raise TypeError("La salud debe ser un entero del 1 al 100")
        
        if isinstance(ataque, int)==True and ataque>=1 and ataque <=10:
            pass
        else:
            raise TypeError("La ataque debe ser un entero entre el 1 y el 10")

        if isinstance(defensa, int)==True and defensa>=1 and defensa <=10:
            pass
        else:
            raise TypeError("La defensa debe ser un entero entre el 1 y el 10")


        self.ID=ID
        self.nombre=nombre
        self.tipo_arma=tipo_arma
        self.salud=salud
        self.ataque=ataque
        self.defensa=defensa
    
    def __del__(self):
        Pokemon.lista_IDs.remove(self.ID)


    def imprimir(self):
        print("Pokemon ID", self.ID, "con nombre", self.nombre, "tiene como arma", self.tipo_arma, "y salud", self.salud)

    
    def get_nombre(self):
        return self.nombre

    def get_tipo_arma(self):
        return self.tipo_arma

    def get_salud(self):
        return self.salud

    def get_ID(self):
        return self.ID
    
    def get_ataque(self):
        return self.ataque
    
    def get_defensa(self):
        return self.defensa

    
    def set_ID(self, ID):
        self.ID=ID

    def set_nombre(self, nombre):
        self.nombre=nombre
    
    def set_tipo_arma(self, tipo_arma):
        self.tipo_arma=tipo_arma
    
    def set_salud(self, salud):
        self.salud=salud
    
    def set_ataque(self, ataque):
        self.ataque=ataque

    def set_defensa(self, defensa):
        self.defensa=defensa

   
    def is_alive(self):
        return self.salud>0
    
    
    def fight_defense(self, puntos_daño):
        if puntos_daño <= self.defensa:
            return False
        else:
            daño_recibido=puntos_daño-self.defensa
            self.salud-=daño_recibido
            return True

    def fight_atack(self, pokemon_a_atacar):
        pokemon_a_atacar.fight_defense(self.ataque)

    

    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """





def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF