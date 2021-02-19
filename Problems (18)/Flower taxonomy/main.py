iris = {}


def add_iris(id_n, species, petal_length, petal_width, **add_features):
    parameters = {}
    parameters['species'] = species
    parameters['petal_length'] = petal_length
    parameters['petal_width'] = petal_width
    for feature in add_features.items():
        parameters[feature[0]] = feature[1]

    iris[id_n] = parameters
