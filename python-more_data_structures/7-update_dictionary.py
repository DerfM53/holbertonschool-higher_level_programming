#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for clé, valeur in a_dictionary.items():
        if key == clé:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
        return a_dictionary
