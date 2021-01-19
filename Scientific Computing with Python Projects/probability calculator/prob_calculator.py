import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for i, j in args.items():
            self.contents += j*[i]

    def draw(self, n):
        """ We remove n elements from the hat and return them"""
        if n <= len(self.contents):
            copy_contents = copy.copy(self.contents)
            to_remove = random.sample(copy_contents, n)
            for element in to_remove:
                self.contents.remove(element)
            return to_remove
        else:
            return self.contents


def filter_dict(dictionary, callback):
    """To filter dictionary for a condition"""
    new_dict = dict()
    for (key, value) in dictionary.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            new_dict[key] = value
    return new_dict


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    results_with_count = []
    filtered_results = []
    list_fav_cases = []
    fav_cases = 0

    for i in range(num_experiments):
        # Get a list with all experiments
        copy_hat = copy.deepcopy(hat)
        results += [copy_hat.draw(num_balls_drawn)]

    for i in range(len(results)):
        # Get a dictionary with the count of the times that a colour has been drawn
        results_with_count = results_with_count.__add__([{x: results[i].count(x) for x in results[i]}])

    for i in range(len(results)):
        # Get only the results that match the keys with the expected_balls
        filtered_results = filtered_results.__add__([filter_dict(results_with_count[i], lambda elem : elem[0] in expected_balls.keys())])

    for i in range(len(results)):
        # Get the number of cases that the count of colours matches with expected_values
        list_fav_cases = list_fav_cases.__add__([len({k: filtered_results[i][k] for k in filtered_results[i].keys() if k in expected_balls.keys() and filtered_results[i][k] >= expected_balls[k]})])

    for i in range(len(list_fav_cases)):
        # Get the number of favorables cases
        if list_fav_cases[i] == len(expected_balls.keys()):
            fav_cases += 1

    return fav_cases/num_experiments





