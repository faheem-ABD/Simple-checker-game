def get_instructions():
    instructions = """
NEMS Instructions:
NEMS is a two-player board game played in the terminal. Please ensure you have Python installed on your system.

Game Overview:
- NEMS is played on a 24-intersection square board.
- Each player has two sets of 9 pieces, one in red and one in green, allowing for variety and strategy.
- Turns alternate between players, starting with Player 1.
- The game is divided into three phases: Fill the board, move pieces, and advanced strategy (optional).

Game Phases:
- In Phase 1, both players fill the board with their pieces.
- In Phase 2, players take turns moving one piece to an adjacent intersection.
- In Phase 3 (optional), when only three pieces are left for each player, they can move to any available intersection, adding an extra layer of strategy.

Winning and Losing:
- Players aim to form 'mills' by placing three of their pieces in a row on the same line (excluding diagonals).
- Forming a mill allows a player to remove one opponent's piece.
- The game continues until one player is left with only two pieces, resulting in a loss for that player.
- The game can also end after a total of 300 moves with no clear winner.

GET READY TO PLAY! Enjoy NEMS!
"""
    return instructions
