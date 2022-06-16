from calendar import c
import re
from unicodedata import category
import mysql.connector 
import pandas as pd
from sqlalchemy import column
from db_con import *
from datetime import date

#DONE
def likeSrcIven(columns = "name", like ='p'):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select drugs.id, drugs.name, drugs.price, drugs.stock,  drugs.exp_date, category_drugs.category
                  from drugs
                  inner join category_drugs on category_drugs.id=drugs.category_id
                  where {} like '%{}%'""".format(columns,like)
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)
    
    df = pd.DataFrame(list,columns=["Id","Name", "Price", "Stock", "Exp Date","Category"])
    cur.close()
    myDb.close()
    return df

def likeSrcStaff(columns = "username", like ='p'):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select staff.username, staff.gender, staff.email,  staff.password, occupation.position
                  from staff
                  inner join occupation on occupation.id=staff.occupation_id;
                  where {} like '%{}%'""".format(columns,like)
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)
    
    df = pd.DataFrame(
        list, columns=["Username", "Gender", "Email", "Pass", "Posisiton"])
    cur.close()
    myDb.close()
    return df
#DONE
def betweenSrcIven(columns = "price", start = 0, end = 1000000):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select drugs.name, drugs.price, drugs.stock, drugs.exp_date, category_drugs.category 
            from drugs
            inner join category_drugs on category_drugs.id = drugs.category_id
            where {} between {} and {};'""".format(columns, start, end)
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)

    df = pd.DataFrame(
        list, columns=["Name", "Price", "Stock", "Exp Date", "Category"])
    cur.close()
    myDb.close()
    return df

#DONE
def stockCalculation(columns='drugs'):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select SUM(stock) from {};'""".format(columns)
    cur.execute(query)
    records = cur.fetchone()
    
    for row in records:
        list.append(row)
    
    res = list[0]
    cur.close()
    myDb.close()
    return res


#DONE
def selectAllInv():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select drugs.id, drugs.name, drugs.price, drugs.stock,  drugs.exp_date, category_drugs.category
                  from drugs
                  inner join category_drugs on category_drugs.id=drugs.category_id;"""
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)
    
    df = pd.DataFrame(list,columns=["Id","Name", "Price", "Stock", "Exp Date","Category"])
    cur.close()
    myDb.close()
    return df

# Done
def selectAllStaff():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select staff.id, staff.username, staff.gender, staff.email,  staff.password, occupation.position
                  from staff
                  inner join occupation on occupation.id=staff.occupation_id;"""
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)

    df = pd.DataFrame(
        list, columns=["Id", "Username", "Gender", "Email", "Pass", "Posisiton"])
    cur.close()
    myDb.close()
    return df

#DONE
def categoryDrugs(category = 'Obat Kapsul'):
    list = []
    key = []
    value = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    addCategory = ("""select id, category from category_drugs;
    """)
    cur.execute(addCategory)
    records = cur.fetchall()
    for row in records:
        list.append(row)
            
    print(len(list))

    for i in range (len(list)):
        for j in range(2):
            if j == 0:
                key.append(list[i][j])
            if j == 1:
                value.append(list[i][j])

    category_dict = dict(zip(value,key))
    categoryId = category_dict.get(category)
    cur.close()
    myDb.close()
    print(type(categoryId))
    return categoryId

#DONE
def insertInv(name,yy,dd,mm,price, stock, category):
    # key= []
    # value = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    print(category)
    print(type(category))
    categoryId = str(categoryDrugs(category))
    addInsert = ('insert into drugs'
                 '(name, exp_date, price, stock, category_id)'
                 'values (%s, %s, %s, %s, %s);')
    data = (name, date(yy,dd,mm), price, stock, categoryId)
    # query = """insert into drugs (name, exp_date, price, stock, category_id)
    #         values ({},{},{},{},{});""".format(name, date(expDate), price, stock, categoryId)
    cur.execute(addInsert,data)

    myDb.commit()
    cur.close()
    myDb.close()

#DONE
def updateInv(id, name, yy,mm,dd, price, stock, category):
    myDb = connecntionDb()
    cur = myDb.cursor()
    categoryId = categoryDrugs(category)
    addUpdate = ('update drugs set'
                 "name= %s, exp_date=%s, price=%s, stock=%s, category_id=%s"
                 'where id = %s')
    data = (name, date(yy,mm,dd), price, stock, categoryId, id)
    # query = """insert into drugs (name, exp_date, price, stock, category_id)
    #         values ({},{},{},{},{});""".format(name, expDate, price, stock, categoryId)
    cur.execute(addUpdate,data)

    myDb.commit()
    cur.close()
    myDb.close()

#DONE
def delData(columns, id):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    delQuery = ('delete from {} where id = {};').format(columns,id)
    cur.execute(delQuery)
    myDb.commit()
    cur.close()
    myDb.close()

#DONE
def sumAmount():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """SELECT SUM(amount) FROM history_sales as h WHERE month(h.date) = month(now());"""
    cur.execute(query)
    records = cur.fetchone()
    
    for row in records:
        list.append(row)
    
    res = list[0]
    cur.close()
    myDb.close()
    return res

# DONE
def countQuantity():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """SELECT COUNT(quantity) 
FROM history_sales as h 
WHERE month(h.date) 
= 
month(now());"""
    cur.execute(query)
    records = cur.fetchone()

    for row in records:
        list.append(row)

    res = list[0]
    cur.close()
    myDb.close()
    return res

# DONE
def sumDrugs():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """SELECT SUM(price) 
FROM drugs as d 
WHERE month(d.updated_at) 
= 
month(now())"""
    cur.execute(query)
    records = cur.fetchone()

    for row in records:
        list.append(row)
    cur.close()
    myDb.close()
    res = list[0]

    return int(res)

# DONE
def countDrugs():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """SELECT COUNT(stock) 
FROM drugs as d 
WHERE month(d.updated_at) 
= 
month(now())"""
    cur.execute(query)
    records = cur.fetchone()

    for row in records:
        list.append(row)

    res = list[0]
    cur.close()
    myDb.close()
    return res

# DONE
def countExp():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """SELECT COUNT(exp_date) 
FROM drugs as d 
WHERE d.exp_date 
< 
now()"""
    cur.execute(query)
    records = cur.fetchone()

    for row in records:
        list.append(row)

    res = list[0]
    cur.close()
    myDb.close()
    return res

#DONE
def viewTransaction():
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """CREATE OR REPLACE VIEW transaksi AS
SELECT 'buy'price, created_at
FROM drugs
UNION
SELECT 'sell'ammount, date 
FROM history_sales;"""
    cur.execute(query)
    view = "SELECT * FROM transaksi"
    cur.execute(view)
    records = cur.fetchall()

    for row in records:
        list.append(row)
    df = pd.DataFrame(list, columns=['Status','Date'])
    cur.close()
    myDb.close()
    return df

#DONE
def orderBy(order):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    
    query = """select drugs.name, drugs.price, drugs.stock, drugs.exp_date, category_drugs.category 
from drugs
inner join category_drugs on category_drugs.id = drugs.category_id
WHERE category_drugs.category IN {} ORDER BY category_drugs.id;""".format(tuple(order))
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        list.append(row)
    
    df = pd.DataFrame(list,columns=["Name", "Price", "Stock", "Exp Date","Category"])
    cur.close()
    myDb.close()
    return df

if __name__ == '__main__':
# #     print(likeSrcIven())
# #     print(betweenSrcIven())
# #     print(stockCalculation())
    # print(sumAmount())
    # print(countQuantity())
    # print(viewTransaction())
    # order = ['Obat Sirup', 'Obat Tablet']
    # print(orderBy(order))
    # print(countDrugs())
    # print(countExp())
    # print(countQuantity())
    # print(sumDrugs())
    # insertInv('Sanmol', (2000,1,1),'15000','15','Obat Kapsul')
    # categoryDrugs()
    print(selectAllStaff())
