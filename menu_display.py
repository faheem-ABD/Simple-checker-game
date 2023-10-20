import os 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_menu():

    print("╔════════════════════════════╗")
    print("║        MAIN MENU           ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  1. PLAY                   ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  2. INSTRUCTIONS           ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  3. QUIT                   ║")
    print("╚════════════════════════════╝")
