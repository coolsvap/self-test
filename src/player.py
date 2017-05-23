import requests


class Player:
    """Server side representation of a 'player'.

    Actual players are independent services that must conform to a specfic
    RESTful interface. The implementation details are up to whoever codes up
    the player service.

    This class is responsible for wrapping an actual player endpoint.
    """

    def __init__(self, id, host, port):
        self._id = id
        self._remote_host = host
        self._remote_port = port
        self._chosen_number = 0
        self._defense_matrix = set()

        self._remote_url_base = 'http://{host}:{port}/'.format(
            host=self._remote_host, port=self._remote_port
        )

    @property
    def id(self):
        return self._id

    @property
    def remote_host(self):
        return self._remote_host

    @property
    def remote_port(self):
        return self._remote_port

    def choose_number(self):
        endpoint = self.get_endpoint_url('/choose-number/')
        response = requests.post(endpoint)
        data = response.json()
        self._chosen_number = data['chosen_number']

    def get_chosen_number(self):
        return self._chosen_number

    def make_defense_matrix(self):
        endpoint = self.get_endpoint_url('/make-defense-matrix/')
        response = requests.post(endpoint)
        data = response.json()
        self._defense_matrix = set(data['defense_matrix'])

    def get_defense_matrix(self):
        return self._defense_matrix

    def get_endpoint_url(self, path):
        if path:
            if path.startswith('/'):
                path = path[1:]
            if not path.endswith('/'):
                path += '/'
        return '{base_url}{path}'.format(
            base_url=self._remote_url_base,
            path=path
        )

    def __repr__(self):
        return 'Player ID: {} (Host: {}, Port: {})'.format(
            self.id, self.remote_host, self.remote_port
        )

