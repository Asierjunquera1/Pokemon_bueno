#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
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
from pokemon import Pokemon
from pokemon import Pokemon
from weapon_type import WeaponType
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity
from pokemon_water import PokemonWater
import random


def get_data_from_user(name_file):
    lista=[]
    with open(name_file, "r") as archivo:
        for linea in archivo:
            linea=linea.rstrip()
            lista1=linea.split(",")
            lista.append(lista1)
    return lista
   
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    print("Entrenador",coach_to_ask, ", estos son tus pokemons:")
    for i in range(len(list_of_pokemons)):
        print(list_of_pokemons[i][1])
    pokemon_elegido=input("Escoge un pokemon: ")
    existe=False
    while existe==False:
        for i in range(len(list_of_pokemons)):
            if pokemon_elegido.lower()==list_of_pokemons[i][1].lower():
                existe=True
                eleccion=list_of_pokemons[i]
        if existe==True:
            pass
        else:
            print("No has elegido un pokemon dentro de tus opciones: Quizá hayas escrito mal el nombre.")
            pokemon_elegido=input("Escoge un pokemon: ")
    return eleccion


    
    
    
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """

    

def coach_is_undefeated(list_of_pokemons):
    
    if len(list_of_pokemons)>=1:
        return True
    else:
        return False
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

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

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    archivo1="Python Files\coach_1_pokemons.csv"
    lista_entrenador1=get_data_from_user(archivo1)

    # Get configuration for Game User 2.
    archivo2="Python Files\coach_2_pokemons.csv"
    lista_entrenador2=get_data_from_user(archivo2)

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
 
    # Choose first pokemons
    pokemon1=get_pokemon_in_a_list_of_pokemons(1, lista_entrenador1)
    pokemon_elegido_entrenador1=Pokemon(int(pokemon1[0]), pokemon1[1], pokemon1[2], int(pokemon1[3]), int(pokemon1[4]), int(pokemon1[5]))
    pokemon2=get_pokemon_in_a_list_of_pokemons(2, lista_entrenador2)
    pokemon_elegido_entrenador2=Pokemon(int(pokemon2[0]), pokemon2[1], pokemon2[2], int(pokemon2[3]), int(pokemon2[4]), int(pokemon2[5]))
    # Main loop.
    while coach_is_undefeated(lista_entrenador1)==True and coach_is_undefeated(lista_entrenador2)==True:
        while pokemon_elegido_entrenador1.health_points>0 and pokemon_elegido_entrenador2.health_points>0:
            pokemon_elegido_entrenador1.fight_attack(pokemon_elegido_entrenador2)
            pokemon_elegido_entrenador2.fight_attack(pokemon_elegido_entrenador1)
        if pokemon_elegido_entrenador1.health_points>0 and pokemon_elegido_entrenador2.health_points<=0:
            print("              ")
            print("Entrenador 2, tu", pokemon_elegido_entrenador2.pokemon_name, "ha muerto")
            print("              ")
            for i in range(len(lista_entrenador1)):
                if pokemon_elegido_entrenador1.pokemon_name==lista_entrenador1[i-1][1]:
                    lista_entrenador1[i-1][3]=pokemon_elegido_entrenador1.health_points
            pokemon_elegido_entrenador1.__del__()

            for i in range(len(lista_entrenador2)):
                if pokemon_elegido_entrenador2.pokemon_name==lista_entrenador2[i-1][1]:
                    linea=lista_entrenador2[i-1]
                    lista_entrenador2.remove(linea)
        elif pokemon_elegido_entrenador2.health_points>0 and pokemon_elegido_entrenador1.health_points<=0:
            print("              ")
            print("Entrenador 1, tu", pokemon_elegido_entrenador1.pokemon_name, "ha muerto")
            print("              ")
            for i in range(len(lista_entrenador2)):
                if pokemon_elegido_entrenador2.pokemon_name==lista_entrenador2[i-1][1]:
                    lista_entrenador2[i-1][3]=pokemon_elegido_entrenador2.health_points
            pokemon_elegido_entrenador2.__del__()

            for i in range(len(lista_entrenador1)):
                if pokemon_elegido_entrenador1.pokemon_name==lista_entrenador1[i-1][1]:
                    linea=lista_entrenador1[i-1]
                    lista_entrenador1.remove(linea)
        else:
            print("              ")
            print("Entrenadores, ambos pokemons,", pokemon_elegido_entrenador1.pokemon_name ,"y", pokemon_elegido_entrenador2.pokemon_name ,"han muerto")
            print("              ")
            for i in range(len(lista_entrenador1)):
                if pokemon_elegido_entrenador1.pokemon_name==lista_entrenador1[i-1][i]:
                    linea=lista_entrenador1[i-1]
                    lista_entrenador1.remove(linea)
        if coach_is_undefeated(lista_entrenador1)==True and coach_is_undefeated(lista_entrenador2)==True:
            
            pokemon1=get_pokemon_in_a_list_of_pokemons(1, lista_entrenador1)
            pokemon_elegido_entrenador1=Pokemon(int(pokemon1[0]), pokemon1[1], pokemon1[2], int(pokemon1[3]), int(pokemon1[4]), int(pokemon1[5]))
            pokemon2=get_pokemon_in_a_list_of_pokemons(2, lista_entrenador2)
            pokemon_elegido_entrenador2=Pokemon(int(pokemon2[0]), pokemon2[1], pokemon2[2], int(pokemon2[3]), int(pokemon2[4]), int(pokemon2[5]))



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    if coach_is_undefeated(lista_entrenador1)==False:
        print("Entrenador 2, has ganado")
    elif coach_is_undefeated(lista_entrenador2)==False:
        print("Entrenador 1, has ganado")
    else:
        print("Habeis empatado")

    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    if coach_is_undefeated(lista_entrenador1)==False:
        print("Todos tus pokemons han muerto")
    else:
        for i in range(len(lista_entrenador1)):
            print("Tu", lista_entrenador1[i][1], "quedó con la siguiente vida:", lista_entrenador1[i][3])

    print("Game User 2:")
    if coach_is_undefeated(lista_entrenador2)==False:
        print("Todos tus pokemons han muerto")
    else:
        for i in range(len(lista_entrenador2)):
            print("Tu", lista_entrenador2[i][1], "quedó con la siguiente vida:", lista_entrenador2[i][3])



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
