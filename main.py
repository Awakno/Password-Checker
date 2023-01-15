from random import *
import string
from colorama import *
import time
from pystyle import *
init()


def main():
    System.Clear()
    System.Size(100,25)
    banner =r"""

      _____                                    _   ______ _           _           
     |  __ \                                  | | |  ____(_)         | |          
     | |__) |_ _ ___ _____      _____  _ __ __| | | |__   _ _ __   __| | ___ _ __ 
     |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | |  __| | | '_ \ / _` |/ _ \ '__|
     | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |    | | | | | (_| |  __/ |   
     |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|    |_|_| |_|\__,_|\___|_|   
                                                                                  
                                                                                  

    """
    banner = Colorate.Vertical(Colors.DynamicMIX((Colors.blue_to_purple)), Center.XCenter(banner))

    print(banner)
    mdp = Write.Input("Mot De Passe à essayer\n     > ",Colors.blue_to_cyan,interval=0.00001)
    print("\n")
    n = 0
    start_time=time.time()
    while True:
        password = "".join(choice(string.digits)for x in range(len(mdp)))
        if password == mdp:
            n+= 1
            time_stop=time.time()
            break
        else:
            n+=1
            print(f"{Fore.YELLOW} {n} {Fore.RED} | {Fore.LIGHTRED_EX} Invalid {Fore.RED} | {Fore.LIGHTRED_EX}{password}", end="\r")
            pass


    print(f"\n{Fore.YELLOW} {n} {Fore.GREEN} | {Fore.LIGHTGREEN_EX} Valid {Fore.GREEN} |{Fore.LIGHTGREEN_EX} {mdp}")
    print(f"{Fore.LIGHTMAGENTA_EX} Trouvé en {Fore.CYAN} {round(time_stop - start_time)} seconds")
    input()
    main()
main()
