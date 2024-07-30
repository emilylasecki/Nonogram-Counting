#control Excel export in a seperate file for readability

#will need to import lists for this file

#jk doing this step in PIE.py too

import pandas as pd


def PANDAS(Size, Colors, PossibleBoards, ColorPercent, BoardPercent):
    dict = {'Size': Size, 'Colors': Colors, 'PossibleBoards': PossibleBoards, 'ColorPercent': ColorPercent, 'BoardPercent': BoardPercent }

    df = pd.DataFrame(dict)

    df.to_excel("PIEoutput.xlsx")
