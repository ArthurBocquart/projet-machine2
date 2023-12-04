import socket
import time
import os

# Mapping des choix possibles
CHOICES = ["pierre", "feuille", "ciseaux"]

# Configuration du client
HOST_SERVER_1 = os.getenv('HOST_SERVER_1')
HOST_SERVER_2 = '192.168.100.14' #IP de la machine linux avec interface graphique
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST_SERVER_1, PORT))

        while True:
            print('Manche 1')
            player_choice = input("Veuillez entrer 'p' (pierre), 'f' (feuille) ou 'c' (ciseaux), ou bien exit pour quitter : ").lower()

            if player_choice == "exit":
                break

            if player_choice not in ["p", "f", "c"]:
                print('Manche 1')
                print("Choix invalide. Veuillez entrer p, f ou c.")
                continue

            player_choice = CHOICES[["p", "f", "c"].index(player_choice)]

            print(f"Choix du joueur: {player_choice}")
            client_socket.sendall(player_choice.encode())

            result = client_socket.recv(1024).decode()
            while not result:
                result = client_socket.recv(1024).decode()
                time.sleep(1)
            print(result)

            if "gagné" in result:
                #On va maintenant faire jouer le client gagnant sur cette machine, contre
                #le client perdant sur la machine où le server 2 pour la finale tourne (sur le port 12346)
                
                #On va d'abord créer le client
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket2:
                    #On va ensuite se connecter au server 2 pour la finale
                    client_socket2.connect((HOST_SERVER_2, 12346))

                    print('Manche 2')
                    player_choice = input("Veuillez entrer 'p' (pierre), 'f' (feuille) ou 'c' (ciseaux), ou bien exit pour quitter : ").lower()

                    if player_choice == "exit":
                        break

                    if player_choice not in ["p", "f", "c"]:
                        print('Manche 2')
                        print("Choix invalide. Veuillez entrer p, f ou c.")
                        continue

                    player_choice = CHOICES[["p", "f", "c"].index(player_choice)]

                    print(f"Choix du joueur: {player_choice}")

                    #On va ensuite envoyer le choix du client gagnant au server 2
                    client_socket2.sendall(player_choice.encode())

                    #On va ensuite recevoir le résultat du server 2
                    result2 = client_socket2.recv(1024).decode()
                    while not result2:
                        result2 = client_socket2.recv(1024).decode()
                        time.sleep(1)
                    print(result2)
                break

if __name__ == "__main__":
    main()