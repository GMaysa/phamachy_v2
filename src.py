from calendar import c
import re
from unicodedata import category
import mysql.connector 
import pandas as pd
from db_con import *
from datetime import date

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

    return df


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
    
    return df

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
    
    return res

def delData(columns, where):
    list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    query = """select SUM(stock) from {};'""".format(columns)
    cur.execute(query)
    records = cur.fetchone()
    
    for row in records:
        list.append(row)
    
    res = list[0]
    
    return res

def selectAll():
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

    return df

def insertInv(name,expDate,price, stock, categoryId):
    # list = []
    myDb = connecntionDb()
    cur = myDb.cursor()
    addInsert = ('insert into drugs'
                 '(name, exp_date, price, stock, category_id)'
                 'values (%s, %s, %s, %s, %s);')
    data = ('Sanmol', date(2024, 2, 7), '50000', '75', '2')
    # query = """insert into drugs (name, exp_date, price, stock, category_id)
    #         values ({},{},{},{},{});""".format(name, expDate, price, stock, categoryId)
    cur.execute(addInsert,data)

    myDb.commit()
    cur.close()
    myDb.close()
    # records = cur.fetchall()
    # for row in records:
    #     list.append(row)
    
    # df = pd.DataFrame(list,columns=["","Name", "Price", "Stock", "Exp Date","Category"])

    # return df

# def updateInv()

# if __name__ == '__main__':
# #     print(likeSrcIven())
# #     print(betweenSrcIven())
# #     print(stockCalculation())
