"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)
    species_list =[]
    for line in file:
        name, species_temp, personality, hobby, motto = line.split('|')
        species_list.append(species_temp)
    
    species = set(species_list)

    # TODO: replace this with your code

    file.close()
    return species



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    file = open(filename)
    villagers = []
    for line in file:
        if search_string == "All":
            name_temp, species, personality, hobby, motto = line.split('|')
            villagers.append(name_temp)
        else:
            name_temp, species, personality, hobby, motto = line.split('|')
            if search_string == species:
                villagers.append(name_temp)
    
    file.close()
    # TODO: replace this with your code

    return sorted(villagers)



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    file = open(filename)

    
    villagers = [[], [], [], [], [], []]
    hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    for line in file:
        name_temp, species, personality, hobby_temp, motto = line.split('|')
        for i, hobby in enumerate(hobbies):
            if hobby == hobby_temp:
                villagers[i].append(name_temp)    
    file.close()

    return [
        sorted(villagers[0]), sorted(villagers[1]), 
        sorted(villagers[2]), sorted(villagers[3]), 
        sorted(villagers[4]), sorted(villagers[5])]

#print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    file = open(filename)
    all_data = []

    for line in file:
        name, species, personality, hobby, motto = line.split('|')
        all_data.append((name, species, personality, hobby, motto))
    file.close()

    # TODO: replace this with your code

    return all_data

#print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    file = open(filename)

    for line in file:
        name, species, personality, hobby, motto = line.split('|')
        if name == villager_name:
            file.close()
            return motto
        
    file.close()
    return None

#print(find_motto("villagers.csv", "haoidjfio") )

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    personality = ""
    file = open(filename)

    for line in file:
        name, species, personality_temp, hobby, motto = line.split('|')
        if name == villager_name:
            personality = personality_temp
    file.close()

    file = open(filename)
    villagers = []

    for line in file:
        name, species, personality_temp, hobby, motto = line.split('|')
        if personality == personality_temp:
            villagers.append(name)
    file.close()

    input_name = {villager_name}
    villagers = set(villagers)

    return villagers ^ input_name

print(find_likeminded_villagers("villagers.csv", "Skye"))

    # TODO: replace this with your code
