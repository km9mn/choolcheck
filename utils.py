import datetime
import pandas as pd

def check(df_response, today, deadline, df_test, tod):
    choolcheck = df_response[['타임스탬프', '이름']]
    choolcheck = choolcheck.loc[choolcheck['타임스탬프'].str.startswith(today)]
    choolcheck = choolcheck.drop_duplicates(['이름'], keep='first')
    choolcheck['출석'] = pd.to_datetime(tod + ' ' + choolcheck['타임스탬프'].str[-8:].replace()) < pd.to_datetime(tod + ' ' + deadline)
    choolcheck['output'] = choolcheck['타임스탬프'].str[-8:].replace()
    name = df_test['성명'].loc[1:].tolist()

    output = []
    late = []
    for n in name:
        if n in choolcheck['이름'].tolist():
            index = choolcheck.index[choolcheck['이름']==n].tolist()[0]
            if choolcheck['출석'][index] == True:
                output.append('O')
            else:
                output.append(choolcheck['output'][index])
                late.append(n)
        else:
            output.append('X')
            late.append(n)
    
    final = []
    for i in output:
        final.append([i])
    
    return final, late
