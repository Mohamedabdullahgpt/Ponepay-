import os 
import pandas as pd
import json
path1 = r'C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\transaction\country\india\state'
agg_trans_list = os.listdir(path1) # [tamilnadu,kerala,...]

columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in agg_trans_list:
    #  state = tamilnadu
    cur_state = path1 + "\\" + state #"C:\Users\jaini\Downloads\pulse\data\aggregated\transaction\country\india\state\tamilnadu"
    # print(cur_state)
    agg_year_list = os.listdir(cur_state) #[2021,2022,....]

    for year in agg_year_list:
        # 2022
        cur_year = cur_state + '\\' + year #"C:\Users\jaini\Downloads\pulse\data\aggregated\transaction\country\india\state\tamilnadu\2022"
        agg_file_list = os.listdir(cur_year) # [1.json,2.json,....]

        for file in agg_file_list:
            cur_file = cur_year + '\\' + file #C:\Users\jaini\Downloads\pulse\data\aggregated\transaction\country\india\state\tamilnadu\2022\1.json"
            data = open(cur_file, 'r')
            A = json.load(data) # {'suscss':'dd,....}

            for i in A['data']['transactionData']:
                '''
                  i = {
                    "name":"Merchant payments",
                    "paymentInstruments":[
                            {
                                "type":"TOTAL",
                                "count":139788772,
                                "amount":8.179820897587326E10
                                }
                        ]
                    },
                '''
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['State'].append(state)
                columns1['Year'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))

df1 = pd.DataFrame(columns1)

df1.to_csv('Aggregated transcations .csv', index=False)

