# -*- coding: utf-8 -*-



  # position groups
CB = ["CB"]
S = ["FS", "SS"]
DB = CB + S
DL = ["DL", "DE", "NT"]
OLB = ["OLB"]
ILB = ["ILB"]
LB = OLB + ILB 
OL = ["C", "OC", "OG", "OT"]
RB = ["RB", "FB"]
WR = ["WR"]
QB = ["QB"]
TE = ["TE"]
K = ["K", "P"]
LINE = DL + OL 
    
# round the values in the dictionary and scale up by 100
def percentage_for(items):
    return map(lambda k_v: (k_v[0], round(k_v[1] * 100, 3)), items)

# get the percentage of players who were drafted with a performance at a given percentile
def get_position_by_drill_lt_percentile_and_drafted(master_dataframe, drill, percentile):
    import operator
    position_names = ["CB", "S", "DB", "DL", "OLB", "ILB", "LB", "OL", "RB", "WR", "QB", "TE", "LINE"]
    position = [CB, S, DB, DL, OLB , ILB , LB , OL , RB , WR, QB, TE, LINE]
    
    percent_drafted_at_percentile = {}

    for pos_str, position in zip(position_names, position):
        # exclude 2015 because presetly there id no draft status for that year
        df_by_position = master_dataframe.loc[(master_dataframe['year'] != 2015) & (master_dataframe["position"].isin(position))]
        df_by_position_and_drill = df_by_position.loc[df_by_position[drill] >= 1]
        
        # total number of athletes who performed the drill 
        total = df_by_position_and_drill[drill].size

        drill_percentile_performance = df_by_position_and_drill[drill].quantile(percentile)
        # total number of athletes who performed equal to or better than the given percentile
        # also use le(a,b) or ge(a,b)    --->  <= or >=
        total_within_percentile = df_by_position_and_drill.loc[(df_by_position_and_drill[drill] <= drill_percentile_performance)][drill].size
        number_drafted = df_by_position_and_drill.loc[(df_by_position_and_drill[drill] <= drill_percentile_performance) & (df_by_position_and_drill["drafted"] == 1)]["drafted"].size  
        percent_drafted_at_percentile[pos_str] = number_drafted/float(total_within_percentile)
        print number_drafted, "/", total_within_percentile, pos_str
        
        # make the dictionary items more easily readable
        pretty_print = percentage_for(percent_drafted_at_percentile.items())
        sorted_percent_drafted_at_percentile = sorted(pretty_print, key=lambda x: x[1], reverse = True)
    return sorted_percent_drafted_at_percentile
    
def get_position_by_drill_gt_percentile_and_drafted(master_dataframe, drill, percentile):
    position_names = ["CB", "S", "DB", "DL", "OLB", "ILB", "LB", "OL", "RB", "WR", "QB", "TE", "LINE"]
    position = [CB, S, DB, DL, OLB , ILB , LB , OL , RB , WR, QB, TE, LINE]
    
    percent_drafted_at_percentile = {}

    for pos_str, position in zip(position_names, position):
        # exclude 2015 because presetly there id no draft status for that year
        df_by_position = master_dataframe.loc[(master_dataframe['year'] != 2015) & (master_dataframe["position"].isin(position))]
        df_by_position_and_drill = df_by_position.loc[df_by_position[drill] >= 1]

        drill_percentile_performance = df_by_position_and_drill[drill].quantile(percentile)
        # total number of athletes who performed equal to or better than the given percentile
        # also use le(a,b) or ge(a,b)    --->  <= or >=
        total_within_percentile = df_by_position_and_drill.loc[(df_by_position_and_drill[drill] >= drill_percentile_performance)][drill].size
        number_drafted = df_by_position_and_drill.loc[(df_by_position_and_drill[drill] >= drill_percentile_performance) & (df_by_position_and_drill["drafted"] == 1)]["drafted"].size  
        percent_drafted_at_percentile[pos_str] = number_drafted/float(total_within_percentile)
        print number_drafted, "/", total_within_percentile, pos_str
        
        # make the dictionary items more easily readable
        pretty_print = percentage_for(percent_drafted_at_percentile.items())
        sorted_percent_drafted_at_percentile = sorted(pretty_print, key=lambda x: x[1], reverse = True)
    return sorted_percent_drafted_at_percentile