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
def selectAllInventory():
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

#DONE
def categoryDrugs(category):
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
    return categoryId

#DONE
def insertInv(name,expDate,price, stock, category):
    key= []
    value = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    categoryId = categoryDrugs(category)
    addInsert = ('insert into drugs'
                 '(name, exp_date, price, stock, category_id)'
                 'values (%s, %s, %s, %s, %s);')
    data = (name, date(expDate), price, stock, categoryId)
    # query = """insert into drugs (name, exp_date, price, stock, category_id)
    #         values ({},{},{},{},{});""".format(name, expDate, price, stock, categoryId)
    cur.execute(addInsert,data)

    myDb.commit()
    cur.close()
    myDb.close()

#DONE
def updateInv(id, name, expDate, price, stock, category):
    myDb = connecntionDb()
    cur = myDb.cursor()
    categoryId = categoryDrugs(category)
    addUpdate = ('update drugs set'
                 "name= %s, exp_date=%s, price=%s, stock=%s, category_id=%s"
                 'where id = %s')
    data = (name, date(expDate), price, stock, categoryId, id)
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
    delData = ('delete from %s'
            'where id = %s')
    data = (columns, id)
    cur.execute(delData,data)
    myDb.commint()
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

    return res

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
    print(countDrugs())
    print(countExp())
    print(countQuantity())
    print(sumDrugs())

