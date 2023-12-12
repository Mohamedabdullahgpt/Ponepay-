import pandas as pd
# import mysql.connector as sql
import os
import json

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dataframe of aggregated Transactions
path1 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\transaction\country\india\state"
agg_trans_list = os.listdir(path1) # [tamilnadu,kerala,...]

columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in agg_trans_list:
    #  state = tamilnadu
    cur_state = path1 + "\\" + state #"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\transaction\country\india\state\tamilnadu"
    # print(cur_state)
    agg_year_list = os.listdir(cur_state) #[2021,2022,....]

    for year in agg_year_list:
        # 2022
        cur_year = cur_state + '\\' + year #"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\transaction\country\india\state\tamilnadu\2022"
        agg_file_list = os.listdir(cur_year) # [1.json,2.json,....]

        for file in agg_file_list:
            cur_file = cur_year + '\\' + file #C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\transaction\country\india\state\tamilnadu\2022\1.json"
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

df_agg_trans = pd.DataFrame(columns1)
print(df_agg_trans)



# data frame of aggregated user
path2 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\aggregated\user\country\india\state"

agg_user_list = os.listdir(path2)

columns2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
for state in agg_user_list:
    cur_state = path2 + '\\' + state
    agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + '\\' + year
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + '\\' + file
            data = open(cur_file, 'r')
            B = json.load(data)
            try:
                for i in B["data"]["usersByDevice"]:
                    brand_name = i["brand"]
                    counts = i["count"]
                    percents = i["percentage"]
                    columns2["Brands"].append(brand_name)
                    columns2["Count"].append(counts)
                    columns2["Percentage"].append(percents)
                    columns2["State"].append(state)
                    columns2["Year"].append(year)
                    columns2["Quarter"].append(int(file.strip('.json')))
            except:
                pass
df_agg_user = pd.DataFrame(columns2)
df_agg_user

# Data frame of map transactions
path3 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\map\transaction\hover\country\india\state"

map_trans_list = os.listdir(path3)

columns3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}

for state in map_trans_list:
    cur_state = path3 + '\\' + state
    map_year_list = os.listdir(cur_state)

    for year in map_year_list:
        cur_year = cur_state + '\\' + year
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year + '\\' + file
            data = open(cur_file, 'r')
            C = json.load(data)

            for i in C["data"]["hoverDataList"]:
                district = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns3["District"].append(district)
                columns3["Count"].append(count)
                columns3["Amount"].append(amount)
                columns3['State'].append(state)
                columns3['Year'].append(year)
                columns3['Quarter'].append(int(file.strip('.json')))

df_map_trans = pd.DataFrame(columns3)
df_map_trans


# Data frame of map user
path4 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\map\user\hover\country\india\state"

map_user_list = os.listdir(path4)

columns4 = {"State": [], "Year": [], "Quarter": [], "District": [],
            "RegisteredUser": [], "AppOpens": []}

for state in map_user_list:
    cur_state = path4 + '\\' + state
    map_year_list = os.listdir(cur_state)

    for year in map_year_list:
        cur_year = cur_state + '\\' + year
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year + '\\' + file
            data = open(cur_file, 'r')
            D = json.load(data)

            for i in D["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appOpens = i[1]['appOpens']
                columns4["District"].append(district)
                columns4["RegisteredUser"].append(registereduser)
                columns4["AppOpens"].append(appOpens)
                columns4['State'].append(state)
                columns4['Year'].append(year)
                columns4['Quarter'].append(int(file.strip('.json')))

df_map_user = pd.DataFrame(columns4)
df_map_user

# Data frame of top transactions
path5 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\top\transaction\country\india\state"

top_trans_list = os.listdir(path5)
columns5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans_list:
    cur_state = path5 + '\\' + state
    top_year_list = os.listdir(cur_state)

    for year in top_year_list:
        cur_year = cur_state + '\\' + year
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year + '\\' + file
            data = open(cur_file, 'r')
            E = json.load(data)

            for i in E['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                columns5['Pincode'].append(name)
                columns5['Transaction_count'].append(count)
                columns5['Transaction_amount'].append(amount)
                columns5['State'].append(state)
                columns5['Year'].append(year)
                columns5['Quarter'].append(int(file.strip('.json')))
df_top_trans = pd.DataFrame(columns5)
df_top_trans

# Data frame of top users
path6 = r"C:\Users\Harish\Desktop\PHONEPAY\pulse\data\top\user\country\india\state"
top_user_list = os.listdir(path6)
columns6 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}

for state in top_user_list:
    cur_state = path6 + '\\' + state
    top_year_list = os.listdir(cur_state)

    for year in top_year_list:
        cur_year = cur_state + '\\' + year
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year + '\\' + file
            data = open(cur_file, 'r')
            F = json.load(data)

            for i in F['data']['pincodes']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                columns6['Pincode'].append(name)
                columns6['RegisteredUsers'].append(registeredUsers)
                columns6['State'].append(state)
                columns6['Year'].append(year)
                columns6['Quarter'].append(int(file.strip('.json')))
df_top_user = pd.DataFrame(columns6)
df_top_user
# Coverting Data frames to csv files
df_agg_trans.to_csv('agg_trans.csv',index=False)
df_agg_user.to_csv('agg_user.csv',index=False)
df_map_trans.to_csv('map_trans.csv',index=False)
df_map_user.to_csv('map_user.csv',index=False)
df_top_trans.to_csv('top_trans.csv',index=False)
df_top_user.to_csv('top_user.csv',index=False)

# Creating connection with MySQL
# Connecting with SQL
import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root",
                   password="12345",
                   
                   database="phonepe_pulse"
                   )
mycursor = mydb.cursor(buffered=True)

# Creating new database and tables
mycursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_pulse")

mycursor.execute("USE Phonepe_pulse")

# Creating agg_trans table
mycursor.execute(
    "create table IF NOT EXISTS agg_trans (State varchar(100), Year int, Quarter int, Transaction_type varchar(100), Transaction_count int, Transaction_amount double)")

for i, row in df_agg_trans.iterrows():
    # here %S means string values
    sql = "INSERT INTO agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

# Creating agg_user table
mycursor.execute(
    "create table IF NOT EXISTS agg_user (State varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")

for i, row in df_agg_user.iterrows():
    sql = "INSERT INTO agg_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()

# Creating map_trans table
mycursor.execute(
    "create table IF NOT EXISTS map_trans (State varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")

for i, row in df_map_trans.iterrows():
    sql = "INSERT INTO map_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()

# Creating map_user table
mycursor.execute(
    "create table IF NOT EXISTS map_user (State varchar(100), Year int, Quarter int, District varchar(100), Registered_user int, App_opens int)")

for i, row in df_map_user.iterrows():
    sql = "INSERT INTO map_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()

# Creating top_trans table
mycursor.execute(
    "create table IF NOT EXISTS top_trans (State varchar(100), Year int, Quarter int, Pincode int, Transaction_count int, Transaction_amount double)")

for i, row in df_top_trans.iterrows():
    sql = "INSERT INTO top_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
# Creating top_user table
mycursor.execute(
    "create table IF NOT EXISTS top_user (State varchar(100), Year int, Quarter int, Pincode int, Registered_users int)")

for i, row in df_top_user.iterrows():
    sql = "INSERT INTO top_user VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()