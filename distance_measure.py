
import numpy as np
import pandas as pd
import random


# get data
df = pd.read_csv("combines.csv")

# columns: [year, name, firstname, lastname, position, heightfeet, heightinches,
# heightinchestotal, weight, arms, hands, fortyyd, twentyyd, tenyd, twentyss,
# threecone, vertical, broad, bench, round, college, pick, pickround, picktotal,
# wonderlic, nflgrade]

# columns: [0:year, 1:name, 2:firstname, 3:lastname, 4:position, 5:heightfeet, 
# 6:heightinches, 7:heightinchestotal, 8:weight, 9:arms, 10:hands, 11:fortyyd, 12:twentyyd, 
# 13:tenyd, 14:twentyss, 15:threecone, 16:vertical, 17:broad, 18:bench, 19:round, 
# 20:college, 21:pick, 22:pickround, 23:picktotal, 24:wonderlic, 25:nflgrade]





def distanceRank(target_player, player_list):
    ranked_list = [(euclidean(target_player, player_i), i) for i, player_i in enumerate(player_list)]
    ranked_list.sort()

    ranked_player_by_index = [i[1] + 1 for i in ranked_list]
    return ranked_player_by_index
    
    



def euclidean(person1, person2):
    score = sum((person1 - person2)**2)
    score = np.sqrt(score)
    return score
    
    
    
dat = df.loc[:5, ['name','fortyyd', 'nflgrade']].values

print "Players closest to {} are: {}".format(dat[0, 0], dat[distanceRank(dat[0, 1:], dat[1:, 1:]), 0])