CC = gcc
CFLAGS = -O3 -Wall

PROGRAMS = dealer example_player

all: $(PROGRAMS)

clean:
	rm -f $(PROGRAMS)

clean_log:
	rm ./logs/*

dealer: game.c game.h evalHandTables rng.c rng.h dealer.c net.c net.h
	$(CC) $(CFLAGS) -o $@ game.c rng.c dealer.c net.c

example_player: game.c game.h evalHandTables rng.c rng.h example_player.c net.c net.h
	$(CC) $(CFLAGS) -o $@ game.c rng.c example_player.c net.c
