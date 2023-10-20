red_color = "\033[91m"   # Red color escape code
green_color = "\033[92m" # Green color escape code
reset_color = "\033[0m"  # Reset color escape code
import time

class NEMS:
    def __init__(self):
        self.players = {
            1: {
                'symbol': "X",
                'pieces_left': 9,
                'moves': [] 
            },
            2: {
                'symbol': "O",
                'pieces_left': 9,
                'moves': []
            }
        }

        # Two copies, one for current state of the board (positions), the other for keeping track of structure of board,
        # since positions will be edited
        self.positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2",
               "D3", "D4", "D5", "D6", "E1", "E2", "E3", "F1", "F2", "F3", "G1", "G2", "G3", "H1", "H2", "H3"]
        self.state = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2",
               "D3", "D4", "D5", "D6", "E1", "E2", "E3", "F1", "F2", "F3", "G1", "G2", "G3", "H1", "H2", "H3"]
        self.valid_moves = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["A2", "B2", "C2"],
                    ["D1", "D2", "D3"], ["D4", "D5", "D6"], ["E1", "E2", "E3"],
                    ["F1", "F2", "F3"], ["G1", "G2", "G3"], ["A1", "D1", "G1"],
                    ["B1", "D2", "F1"], ["C1", "D3", "E1"], ["C3", "D4", "E3"],
                    ["B3", "D5", "F3"], ["A3", "D6", "G3"], ["E2", "F2", "G2"]]
        print(self.display_board(green_color + "X" + reset_color, red_color + "O" + reset_color))

    def display_board(self, player1, player2):
        # Create the formatted strings for Player 1 and Player 2
        formatted_player1 = f" Player 1  ({player1})"
        formatted_player2 = f" Player 2  ({player2})"

        # Create the game pieces here
        player1_pieces = f"{green_color}{self.players[1]['symbol']}{reset_color} " * self.players[1]['pieces_left']
        player2_pieces = f"{red_color}{self.players[2]['symbol']}{reset_color} " * self.players[2]['pieces_left']

        # Create the game board here
        game_board = f"""
    
    Player 1 pieces (Total: {len(self.players[1]["moves"])+self.players[1]["pieces_left"]}): {player1_pieces} \n
    Player 2 pieces (Total: {len(self.players[1]["moves"])+self.players[1]["pieces_left"]}): {player2_pieces}

    {self.positions[0]}________________________________________ {self.positions[1]} _______________________________________ {self.positions[2]}
    |                                          |                                         |                    
    |                                          |                                         |
    |            {self.positions[3]} ________________________ {self.positions[4]} ___________________________ {self.positions[5]}           |                                       
    |            |                             |                             |           |
    |            |                             |                             |           |
    |            |           {self.positions[6]} _______________{self.positions[7]}____________{self.positions[8]}              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    {self.positions[9]} __________ {self.positions[10]} _________ {self.positions[11]}                                {self.positions[12]} ____________ {self.positions[13]} _________ {self.positions[14]}
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           | 
    |            |           |                                |              |           |
    |            |           {self.positions[15]} ___________  {self.positions[16]}  ___________ {self.positions[17]}              |           |
    |            |                            |                              |           |
    |            |                            |                              |           |
    |            {self.positions[18]} _________________________ {self.positions[19]} __________________________ {self.positions[20]}           |                 
    |                                         |                                          |
    |                                         |                                          |
    {self.positions[21]} _______________________________________ {self.positions[22]} ________________________________________ {self.positions[23]}

    """

        # Replace symbols with colored symbols
        game_board = game_board.replace(self.players[1]['symbol'], green_color + self.players[1]['symbol'] + reset_color)
        game_board = game_board.replace(self.players[2]['symbol'], red_color + self.players[2]['symbol'] + reset_color)

        return game_board

    def already_taken(self, position):
        for player_num in self.players:
            if position in self.players[player_num]['moves']:
                return True
        return False

    def remove_piece(self, position, player):
        if self.already_taken(position):
            self.positions[self.state.index(position)] = position
            self.players[player]['moves'].remove(position)
            

    # Check if 3 in a row
    def check_mills(self, position, player):
        for mills in self.valid_moves:
            if position in mills:
                x = 0
                for s in mills:
                    if s in self.players[player]['moves']:
                        x += 1
                if x == 3:
                    return True
        return False

    def can_reach(self, move_from, move_to):
        # Check if the move is valid (one step in either x or y direction)
        for x in self.valid_moves:
            if move_to in x:
                if move_from in x:
                    # Check if Adjacent
                    # For example, A1 to A3 should be invalid. But A1 to D1 is valid, so we'll need to use indexes.
                    if abs(x.index(move_from) - x.index(move_to)) == 1:
                        return True
        return False

    def place_piece(self, position, move_from, player):
        if self.already_taken(position):
            return False

        player_info = self.players[player]

        if move_from is None:
            player_info['pieces_left'] -= 1
            player_info['moves'].append(position)
        elif self.can_reach(move_from, position):
            player_info['moves'].remove(move_from)
            player_info['moves'].append(position)
        else:
            return False

        placement = self.positions.index(position)

        if move_from is not None:
            self.positions[self.state.index(move_from)] = move_from

        self.positions[placement] = player_info['symbol']

        return True
    def play(self):
        current_player = 1
        moves_left = 300

        time_limit_input = input("Enter the time limit in seconds (default is 10 minutes, press Enter to use default): ")

        if time_limit_input.strip():
            time_limit = int(time_limit_input)
        else:
            time_limit = 600  # Default time limit is 10 minutes (600 seconds)

        start_time = time.time() 

        while moves_left > 0:  
            player_info = self.players[current_player]
            if player_info['pieces_left'] == 0:
                correct_input = False
                while not correct_input:
                    player_position_from = input(f"Player {current_player}, enter your position from: ")
                    player_position_to = input(f"Player {current_player}, enter your position to: ")

                    if player_position_to.lower() == 'f':
                        print("Quitting the game.")
                        return  # Exit the play() function and the game
                    elif player_position_from not in player_info['moves']:
                        print('You do not have a piece in that position.')
                    elif self.already_taken(player_position_to):
                        print('That position is already taken.')
                    elif not self.can_reach(player_position_from, player_position_to):
                        print('You can only move one step sideways or vertically')
                    else:
                        self.place_piece(player_position_to, player_position_from, current_player)
                        print("oh")
                        correct_input = True
            else:
                correct_input = False
                while not correct_input:
                    player_position_to = input(f"Player {current_player}, enter your position to: ")

                    if player_position_to.lower() == 'f':
                        print("Quitting the game.")
                        return  # Exit the play() function and the game
                    try:
                        self.place_piece(player_position_to, None, current_player)
                        correct_input = True
                    except:
                        print("Wrong input, try again.")

            if self.check_mills(player_position_to, current_player):
                removed_piece = input(f"Player {current_player}, enter opponent piece to remove: ")
                self.remove_piece(removed_piece, 3 - current_player)

            print(self.display_board(green_color + "X" + reset_color, red_color + "O" + reset_color))

            if len(self.players[3 - current_player]['moves']) + self.players[3 - current_player]['pieces_left'] == 2:
                print(f"Player {current_player} wins!")
                break

            current_player = 3 - current_player
            moves_left -= 1  # Decrement the move limit

            # Check if the time limit has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print("Time limit exceeded. The game is ending.")
                break

        print("The game has ended due to time limit or move limit")


if __name__ == "__main__":
    game = NEMS()
    game.play()
