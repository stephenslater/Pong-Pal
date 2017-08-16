from elo import elo

print "Match 1: higher rank A wins big"
elo(1200, 1000, 11, 0)
print "\n" + "Match 2: higher rank A wins small"
elo(1200, 1000, 11, 9)
print "\n" + "Match 3: smaller rank A wins big"
elo(1200, 1000, 0, 11)
print "\n" + "Match 4: smaller rank A wins small"
elo(1200, 1000, 9, 11)
print "\n" + "Match 5: expert player A wins with 0.75 exp"
elo(2900, 2700, 11, 7)
print "\n" + "Match 6: normal player A wins with 0.75 exp"
elo(1800, 1600, 11, 7)
print "\n" + "Match 7: expert player A loses with 0.75 exp"
elo(2900, 2700, 0, 11)
print "\n" + "Match 8: normal player A loses with 0.75 exp"
elo(1800, 1600, 5, 11)
print "\n" + "Match 9: normal player A loses 0-11 with 0.75 exp"
elo(1800, 1600, 0, 11)
print "\n" + "Match 10: normal player A loses 1-11 with 0.75 exp"
elo(1800, 1600, 1, 11)
print "\n" + "Match 11: normal player A loses 5-11 with 0.75 exp"
elo(1800, 1600, 5, 11)
print "\n" + "Match 12: normal player A loses 6-11 with 0.75 exp"
elo(1800, 1600, 6, 11)
print "\n" + "Match 13: normal player A loses 9-11 with 0.75 exp"
elo(1800, 1600, 9, 11)
print "\n" + "Match 14: normal player A wins 11-9 with 0.75 exp"
elo(1800, 1600, 11, 9)
print "\n" + "Match 15: normal player A wins 11-6 with 0.75 exp"
elo(1800, 1600, 11, 6)
print "\n" + "Match 16: normal player A wins 11-5 with 0.75 exp"
elo(1800, 1600, 11, 5)
print "\n" + "Match 17: normal player A wins 11-1 with 0.75 exp"
elo(1800, 1600, 11, 1)
print "\n" + "Match 18: normal player A wins 11-0 with 0.75 exp"
elo(1800, 1600, 11, 0)
print "\n" + "Match 19: equally ranked players compete at 1200"
elo(1200, 1200, 11, 0)
print "\n" + "Now score is 11-5"
elo(1200, 1200, 11, 5)
print "\n" + "Now score is 11-9"
elo(1200, 1200, 11, 9)
print "\n" + "Match 20: equally ranked players compete at 1200"
elo(1600, 1600, 11, 0)
print "\n" + "Now score is 11-5"
elo(1600, 1600, 11, 5)
print "\n" + "Now score is 11-9"
elo(1600, 1600, 11, 9)
print "\n" + "Match 21: equally ranked players compete at 2000"
elo(2000, 2000, 11, 0)
print "\n" + "Now score is 11-5"
elo(2000, 2000, 11, 5)
print "\n" + "Now score is 11-9"
elo(2000, 2000, 11, 9)
print "\n" + "Match 22: max rank wins a game"
elo(3000, 2000, 11, 9)
print "\n" + "Match 23: max rank loses a game"
elo(3000, 2000, 9, 11)
print "\n" + "Now score is 0-11"
elo(3000, 2000, 0, 11)
print "\n" + "Match 23: max rank loses a game"
elo(2200, 1200, 9, 11)
print "\n" + "Now score is 0-11"
elo(2200, 1200, 0, 11)