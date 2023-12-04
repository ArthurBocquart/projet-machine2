# Projet Pierre, Feuille, Ciseaux

Ce projet utilise Docker-compose pour containeriser une application client-serveur.

## Explications

### Déroulement du jeu

Deux client vont commencer par s'affronter dans un pierre, feuille, ciseaux à 1 manche gagnante sur chaque machine.
Les gagnants de chaque machine vont ensuite s'affronter dans une finale.

### Mise en place

Sur la première machine linux (celle avec interface), il y a 4 conteneurs docker.
Deux conteneurs pour les 2 clients qui vont s'affronter, un server pour la première manche entre ces deux clients, et un server pour la finale entre un client de cette machine, et un client de l'autre machine.

Sur la seconde machine (celle sans interface), il y a 3 conteneurs docker.
Deux conteneurs pour les 2 clients qui vont s'affronter, et un server pour la première manche entre ces deux clients. Le client gagnant affrontera le client de l'autre machine, via le server de l'autre machine.

## Instructions de construction des images

### Images des clients

Pour construire l'image des deux clients sur les deux machines, se placer dans le répertoire 'client', et utiliser les commandes suivantes :

```bash
docker build -t client1 .
docker build -t client2 .
```


### Images des serveurs

Pour construire l'image du serveur sur les deux machines, se placer dans le répertoire 'server' et utiliser la commande suivante :

```bash
docker build -t server1 .
```

Sur la machine avec interface, saisir en plus la commande suivante pour lancer le second server pour la finale :

```bash
docker build -t server2 .
```

## Exécution avec Docker Compose

Une fois que les images ont été construites, vous pouvez exécuter l'application à l'aide de Docker Compose. Utilisez les commandes suivantes :

```bash
docker-compose up -d
```

Cela construira les images nécessaires et lancera les conteneurs en arrière-plan.

### Jouer

## Instruction pour jouer

Maintenant que les conteneurs sont lancés, il ne reste plus qu'a attacher les terminaux des clients sur chaque machine avec les commandes suivantes :

```bash
docker attach client1
docker attach client2
```

On peut également attacher les terminaux des servers pour voir ce qui s'y passe pour les curieux. Utilisez la commande suivante :

```bash
docker attach server1
```

Même chose pour la finale. Si des curieux veulent voir ce qui se passe dans le terminal du server, il suffit de taper la commande suivante sur la machine avec interface (où le server finale est lancé) :

```bash
docker attach server2
```

Que le meilleur gagne !# projet-machine2
