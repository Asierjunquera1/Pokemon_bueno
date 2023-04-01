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
    print( coach_to_ask ,"Estos son tus pokemons, elige uno:")
    print(list_of_pokemons)
    eleccion=int(input("Pulse 1 si elige a su pokemon nº 1, 2 si elige su pokemon nº 2 y 3 si elige su pokemon nº3:"))
    while eleccion!=1 and eleccion!=2 and eleccion!=3:
        eleccion= int(input("Debes elegir un numero del 1 al 3. Pulse 1 si elige a su pokemon nº 1, 2 si elige su pokemon nº 2 y 3 si elige su pokemon nº3:"))
    pokemon_eleccion=list_of_pokemons[eleccion]
    tipo=input("¿De que tipo es tu pokemon: tierra, aire, electricidad agua o normal (si no es de ninguno de estos tipos teclea normal)?")
    while tipo!="tierra" and tipo!="aire" and tipo!="electricidad" and tipo!="agua" and tipo!="normal":
        print("Tu eleccion no está dentro de las posibles. Quizá no lo hayas escrito igual de como viene en las opciones(sin mayusculas, tildes, ni ningun signo)")
        tipo=input("¿De que tipo es tu pokemon: tierra, aire, electricidad agua o normal (si no es de ninguno de estos tipos teclea normal)?")
    if tipo=="tierra":
        pokemon_elegido=PokemonEarth(pokemon_eleccion[1], pokemon_eleccion[2], pokemon_eleccion[3], pokemon_eleccion[4], pokemon_eleccion[5], pokemon_eleccion[6])
    elif tipo=="aire":
        pokemon_elegido=PokemonAir(pokemon_eleccion[1], pokemon_eleccion[2], pokemon_eleccion[3], pokemon_eleccion[4], pokemon_eleccion[5], pokemon_eleccion[6])
    elif tipo=="electricidad":
        pokemon_elegido=PokemonElectricity(pokemon_eleccion[1], pokemon_eleccion[2], pokemon_eleccion[3], pokemon_eleccion[4], pokemon_eleccion[5], pokemon_eleccion[6])
    elif tipo=="agua":
        pokemon_elegido=PokemonWater(pokemon_eleccion[1], pokemon_eleccion[2], pokemon_eleccion[3], pokemon_eleccion[4], pokemon_eleccion[5], pokemon_eleccion[6])
    elif tipo=="normal":
        pokemon_elegido=Pokemon(pokemon_eleccion[1], pokemon_eleccion[2], pokemon_eleccion[3], pokemon_eleccion[4], pokemon_eleccion[5], pokemon_eleccion[6])
    return pokemon_elegido
    


    
    
    
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
    if list_of_pokemons[1][4]<=0 and  list_of_pokemons[2][4]<=0 and list_of_pokemons[3][4]<=0:
        return False
    else: 
        return True
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

    get_data_from_user(coach_1_pokemons.csv)

    # Get configuration for Game User 2.
    get_data_from_user(coach_2_pokemons.csv)

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:


    # Choose first pokemons
 

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
