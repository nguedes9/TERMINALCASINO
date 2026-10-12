from casino.utils import cprint

def show_uno_stats(players, winner):
    cprint("\n===== UNO POSTGAME STATS =====")

    for player in players:
        cprint("\nPlayer: " + player.name)

        if player == winner:
            cprint("Result: WIN")
        else:
            cprint("Result: LOSS")

        cprint("\nTurns Taken: " + str(player.turns_taken))
        cprint("\nCards Drawn: " + str(player.cards_drawn))
        cprint("\nCards Played: " + str(player.cards_played))
        cprint("\nSpecial Cards Played: " + str(player.special_cards_played))
        cprint("\nLargest Hand Size: " + str(player.largest_hand_size))
        cprint("\nCards Remaining: " + str(len(player.hand)))
        cprint("\n\n------------------------------")

    cprint("\n==============================")