
# coding: utf-8

# In[3]:

import pandas as pd
import datetime

# load data
data = pd.read_csv('loanData.csv')
df = pd.DataFrame(data)

result=[]
scoreList=[]

# attribute selection
dataset = df[['member_id', 'term', 'verification_status', 'loan_status', 'zip_code', 'addr_state', 'delinq_2yrs',
              'earliest_cr_line',
              'pub_rec', 'revol_bal', 'total_acc', 'open_acc']]

dataset['score'] = None

for index, row in dataset.iterrows():
    
    score = 0
    
    print(dataset.loc[index, 'earliest_cr_line'])
    
    # change string format to int term-column
    if dataset.loc[index, 'term'] == " 60 months":
        dataset.loc[index, 'term'] = 60
    elif dataset.loc[index, 'term'] == " 36 months":
        dataset.loc[index, 'term'] = 36

    # payment history
    if dataset.loc[index, 'pub_rec'] == 0 and dataset.loc[index, 'delinq_2yrs'] == 0 and dataset.loc[
        index, 'revol_bal'] == 0 and dataset.loc[index, 'term'] == 60:
        score= score + 35
    else:
        score= score + 17

    # customer status
    if (dataset.loc[index, 'pub_rec'] + dataset.loc[index, 'delinq_2yrs'] == 0) and dataset.loc[index, 'verification_status'] == "Verified" and dataset.loc[index, 'loan_status'] == "Fully Paid":
        score= score + 30
    else:
        score= score + 15

    # risk level
    score = score - (
                dataset.loc[index, 'open_acc'] / dataset.loc[index, 'total_acc'] + dataset.loc[index, 'pub_rec'] +
                dataset.loc[index, 'delinq_2yrs'])
    
    date2 = int(dataset.loc[index,'earliest_cr_line'][:4])
    print('date2: ', date2)
    
    
    # experienced customer
    if date2 > 2010:
        score = score  + 0
    elif date2  > 2000 and date2  <= 2010:
        score = score  + 2
    elif date2 > 1990 and date2 <= 2000:
        score = score  + 4
    elif date2 > 1980 and date2 <= 1990:
        score = score  + 6
    elif date2 > 1970 and date2 <= 1980:
        score = score  + 8
    elif date2 <= 1970:
        score = score  + 10

    #print('score: ', score)
    scoreList.append(score)
    #dataset['score'].append(score)
    
dataset['score']=scoreList
dataset.sort_values(['score'],ascending=False)
print(dataset.head(3000).sort_values(['earliest_cr_line'][:4]))



out = dataset.to_json(orient='records')

with open('customer.json', 'w') as f:
    f.write(out)
    
f.close()
#result.head(50)
# print(dataset.isnull().values.any())

# dataset.dropna(axis=0, how='all')










# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



