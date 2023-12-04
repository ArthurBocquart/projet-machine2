import socket
import os

# Mapping des choix possibles
CHOICES = ["rock", "paper", "scissors"]

# Fonction pour déterminer le gagnant
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 3
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return 1
    else:
        return 2

# Configuration du serveur
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Server listening on", (HOST, PORT))

    conn1, addr1 = server_socket.accept()
    conn2, addr2 = server_socket.accept()

    with conn1, conn2:
        print('Connected by', addr1, 'and', addr2)

        while True:
            data1 = conn1.recv(1024).decode()
            print(f"Choix du joueur 1: {data1}")

            data2 = conn2.recv(1024).decode()
            print(f"Choix du joueur 2: {data2}")

            if not data1 or not data2:
                break

            winner = determine_winner(data1, data2)
            player1_result = "Egalité !"
            player2_result = "Egalité !"

            if winner == 1:
                player1_result = "Tu as gagné !"
                player2_result = "Tu as perdu !"
            elif winner == 2:
                player1_result = "Tu as perdu !"
                player2_result = "Tu as gagné !"

            conn1.send(player1_result.encode())
            conn2.send(player2_result.encode())