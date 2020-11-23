import socketserver
from constants import HOST, PORT, PLAYER_SIZE, DATA_TYPE


class GameServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    players = dict()

    def send(self, data):
        if not isinstance(data, str):
            data = str(data)
        if not isinstance(data, bytes):
            data = bytes(data, 'utf-8')
        self.request.sendall(data)

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        data = self.data.decode('utf-8')
        try:
            data = eval(data)
        except Exception as e:
            print("## error")
            data = dict()
        data_type = data.get('data_type')
        if data_type == DATA_TYPE['INITIALIZING_PLAYER']:
            player = data.get('player', {})
            if player:
                for key, value in player.items():
                    self.players[key] = value
        if len(self.players) != PLAYER_SIZE:
            data = {
                "data_type": DATA_TYPE['WAITING_PLAYER'],
                "message": "waiting for player 2 to join.",
                'turn': None
            }
            self.send(data)



if __name__ == "__main__":

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), GameServer) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print("Listening...")
        server.serve_forever()
