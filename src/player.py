import random

CHOSEN_NUMBER_RANGE = (1, 11)


class Player:
    """Represents a 'player' of a tournament
    """

    def __init__(self, player_data):
        self.id = int(player_data['id'])
        self.name = player_data['name']
        self._chosen_number = 0
        self.make_defense_matrix(int(player_data['length']))

    def choose_number(self):
        self._chosen_number = random.randrange(*CHOSEN_NUMBER_RANGE)

    def get_chosen_number(self):
        return self._chosen_number

    def make_defense_matrix(self, length):
        self._defense_matrix = random.sample(
            range(*CHOSEN_NUMBER_RANGE), length
        )

    def get_defense_matrix(self):
        return self._defense_matrix
