from statistics import Statistics
from player_reader import PlayerReader
import matchers


class QueryBuilder:
    def __init__(self, pino=matchers.All()):
        self.pino_olio = pino

    def playsIn(self, team):

        return QueryBuilder(matchers.And(self.pino_olio, matchers.PlaysIn(team)))

    def hasAtLeast(self, value, attr):

        return QueryBuilder(matchers.And(self.pino_olio, matchers.HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(matchers.And(self.pino_olio, matchers.HasFewerThan(value, attr)))

    def oneOf(self, *query):
        return QueryBuilder(matchers.Or(*query))

    def build(self):
        return self.pino_olio


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(40, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
