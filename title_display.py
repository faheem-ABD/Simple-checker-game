import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    clear_screen()
    neon_green = "\033[1;32m"  # ANSI escape code for neon green text
    reset_color = "\033[0m"    # ANSI escape code to reset text color

    print(f"{neon_green}███╗   ██╗███████╗███╗   ███╗███████╗")
    print(f"████╗  ██║██╔════╝████╗ ████║██╔════╝")
    print(f"██╔██╗ ██║█████╗  ██╔████╔██║███████╗")
    print(f"██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║")
    print(f"██║ ╚████║███████╗██║ ╚═╝ ██║███████║")
    print(f"╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝{reset_color}")
    input("Press Enter to continue...")
