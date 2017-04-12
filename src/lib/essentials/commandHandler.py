import src.lib.modules.memes
import src.lib.modules.comics
import src.lib.modules.plusplus
import src.lib.modules.flipcoin
import src.lib.modules.calc
import src.lib.runtimes.games.mathwars
import src.lib.runtimes.games.reaction
import src.lib.runtimes.games.scrabble


def handle(payload):
    if payload.content.lower() == "$help":
        return ["Single", [["text", """```Ubi Help
    Standard commands
        1. $flipcoin ~ flips a coin
        2. $comic ~ uploads a comic from xkcd
        3. $meme ~ uploads a meme from memes.com
        4. $scrabble ~ starts a game of scrabble
    Music commands
        1. $music add (url) ~ replace (url) with youtube link, adds link to quene
        2. $music skip ~ adds vote to skip current song (2 votes = skip)
        3. $music playlist ~ shows all songs in the playlist quene
        To use these commands must be in a voice channel
    Plus Plus commands
        plus plus is a system built within ubi to award teammates with 'points'
        1. $stats ~ gets a leaderboard of plus plus scores
        2. $++(user) ~ adds a point to a specific user (don't put a space between the last + and the users name)
        3. $--(user) ~ removes a point from a specific user (don't put a space between the last - and the users name)
        ```"""]]]
    elif payload.content.lower() == "$flipcoin":
        return ["Single", src.lib.modules.flipcoin.main()]
    elif payload.content.lower() == "$comic":
        return ["Single", src.lib.modules.comics.main()]
    elif payload.content.lower() == "$meme":
        return ["Single", src.lib.modules.memes.main()]
    elif payload.content.lower() == "$stats":
        return ["Single", src.lib.modules.plusplus.main_stats(payload)]
    elif payload.content.lower().startswith("$++") or payload.content.lower().startswith("$--"):
        return ["Single", src.lib.modules.plusplus.main_alter(payload)]
    elif payload.content.lower().startswith("$calc "):
        return ["Single", src.lib.modules.calc.main(payload)]
    elif payload.content.lower().startswith("$scrabble"):
        return ["Socket", "Scrabble"]
    elif payload.content.lower().startswith("$music"):
        return ["Socket", "Music"]