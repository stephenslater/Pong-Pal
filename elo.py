# Modified ELO algorithm implemented by Stephen Slater on 7/26/17
# Considers game point differential and ELO percentile when calculating new ELO
# The function expected() was taken from https://github.com/rshk/elo/blob/master/elo.py
# See https://en.wikipedia.org/wiki/Elo_rating_system

from __future__ import division
import sqlite3

conn = sqlite3.connect('pingpong.db')
c = conn.cursor()

def expected(eloA, eloB):
    """
    Calculate expected score of A in a match against B
    Values are in the range [0, 1], where 1 represents 100% expected win
    :param eloA: Elo rating for player A
    :param eloB: Elo rating for player B
    """
    return 1 / (1 + 10 ** ((eloB - eloA) / 400))

# Returns the two new Elo values in a tuple: (newA, newB)
def elo(eloA, eloB, scoreA, scoreB, k=32):
    """
    Calculate the new Elo rating for a player
    :param eloA: The previous Elo rating for player A
    :param eloB: The previous Elo rating for player B
    :param scoreA: Score of Player A
    :param scoreB: Score of Player B
    :param k: The k-factor for Elo, used as a scalar (default: 32)
    :param eloMax: The max rating in the company (default: 3000)
    
    Lost points are based on original ELO algorithm (expected match result and relative ELO rankings).
    Gained points are also based on game point differential and company ranking.
    """
    c.execute('SELECT max(ELO) from players')
    eloMax = c.fetchone()[0]

    if eloMax <= 1800:
        eloMax = 3000

    # Calculated expected score of this match
    expA = expected(eloA, eloB)
    expB = 1 - expA
    wonA = int(scoreA > scoreB)
    wonB = 1 - wonA

    scoreMax = max(scoreA, scoreB)
    diff = abs(scoreA - scoreB)
    flag = 1

    # Calculated ELO scores without factoring in game point differential
    regularA = baseA = eloA + k * (wonA - expA)
    regularB = baseB = eloB + k * (wonB - expB)

    # Span is the distance beyond the base score
    spanA = abs(regularA - eloA) / 3
    spanB = abs(regularB - eloB) / 3

    # Step is the number of ELO points gained/lost per ping-pong point
    stepA = spanA / (0.5 * scoreMax)
    stepB = spanB / (0.5 * scoreMax)

    # Update ELO based on company ranking so that the player does not gain as much at higher levels
    if wonA:
        baseA += spanA * (1 - (wonA * (eloA / eloMax)))
    else:
        baseB += spanB * (1 - (wonB * (eloB / eloMax)))

    score = scoreA if scoreA < scoreB else scoreB
    changeA = stepA * (score - 0.5 * scoreMax) if wonA else 0
    changeB = stepB * (score - 0.5 * scoreMax) if wonB else 0
    if scoreA > scoreB:
        flag *= -1

    # New ELO scores factoring in game point differential
    newA = round(baseA + flag * changeA, 3)
    newB = round(baseB - (flag * changeB), 3)

    # Output for testing
    # print "baseA " + str(baseA)
    # print "baseB " + str(baseB)
    # print "spanA " + str(spanA)
    # print "spanB " + str(spanB)
    # print "stepA " + str(stepA)
    # print "stepB " + str(stepB)
    # print "expA " + str(expA)
    # print "expB " + str(expB)
    # print "wonA " + str(wonA)
    # print "wonB " + str(wonB)
    # print "lower score: " + str(score)
    # print "score diff: " + str(diff)
    # print "oldA, oldB: " + str(eloA) + ", " + str(eloB)
    # print "regularA, regularB: " + str(regularA) + ", " + str(regularB)
    # print "newA, newB: " + str(newA) + ", " + str(newB)
    # gained = abs(newA - eloA)
    # lost = abs(newB - eloB)
    # print "winner regular gained, new gained: " + str(abs(regularA - eloA)) + ", " + str(gained)
    # print "loser regular lost, new lost: " + str(abs(regularB - eloB)) + ", " + str(lost)
    # print "lost points to gained points ratio: " + str(lost / gained)
    # print "total point swing: " + str(gained + lost)
    return newA, newB 
