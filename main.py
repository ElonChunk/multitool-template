import colorama
import time
from pystyle import System as PYSytem

colorama.init(autoreset=True)

#Here add the your multitool's name
PYSytem.Title("Multitool Template by MrAnergos")

def action1():
    print("Action 1 executed.")
    time.sleep(5)

def action2():
    print("Action 2 executed.")
    time.sleep(5)

def action3():
    print("Action 3 executed.")
    time.sleep(5)

def action4():
    print("Action 4 executed.")
    time.sleep(5)

def discord_link():
    print("Discord link: https://discord.gg/your-link")
    time.sleep(5)



def print_rechtangle_banner():
    print(colorama.Fore.BLUE + """
┌────────────── Multitool Template ──────────────┐
| [1] Action 1  |[3] Action 3 |[5] Discord       |
| [2] Action 2  |[4] Action 4 |Made by MrAnergos |
└────────────────────────────────────────────────┘
""")
    
def print_banner():
    print(colorama.Fore.CYAN + """

███╗   ███╗██╗   ██╗████████╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗         ████████╗███████╗███╗   ███╗██████╗ 
████╗ ████║██║   ██║╚══██╔══╝██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║         ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗
██╔████╔██║██║   ██║   ██║   ██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║            ██║   █████╗  ██╔████╔██║██████╔╝
██║╚██╔╝██║██║   ██║   ██║   ██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║            ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ 
██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗       ██║   ███████╗██║ ╚═╝ ██║██║     
╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     
          
""")

def refresh_cmd():
    PYSytem.Clear()
    print_banner()
    print_rechtangle_banner()

def main():
    PYSytem.Clear()
    print_banner()
    print_rechtangle_banner()
    while True:
        cmd = input(colorama.Fore.YELLOW + "Selection: " + colorama.Fore.WHITE).strip()
        if cmd == "1":
            action1()
            refresh_cmd()
        elif cmd == "2":
            action2()
            refresh_cmd()
        elif cmd == "3":
            action3()
            refresh_cmd()
        elif cmd == "4":
            action4()
            refresh_cmd()
        elif cmd == "5":
            discord_link()
            refresh_cmd()
        elif cmd.lower() == "exit":
            break
        else:
            print(colorama.Fore.RED + "Invalid selection. Please try again.")
            time.sleep(4)
            refresh_cmd()

if __name__ == "__main__":
    main()
