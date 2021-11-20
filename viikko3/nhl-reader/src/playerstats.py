from player import Player
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self,nationality):
        players = []
        for player_dict in self.reader.response:
            if player_dict['nationality'] == nationality:
                player = Player(
                    player_dict['name'],
                    player_dict['team'],
                    player_dict['goals'],
                    player_dict['assists']
                )
                players.append(player)
        players.sort(key=lambda x: (x.points, x.goals), reverse=True)
        return players