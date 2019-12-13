"""
Answer the following questions (each is from a single table):

What are the ten most expensive items (per unit price) in the database?
What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
(Stretch) How does the average age of employee at hire vary by city?
"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

def q_all(query):
    curs = conn.cursor()
    curs.execute(query)
    rows = curs.fetchall()
    curs.close()
    return rows

def q_one(query):
    row = q_all(query)
    return row[0][0]




print('Top 10 most Expensive:', q_all("SELECT * FROM OrderDetail GROUP BY ProductID ORDER BY UnitPrice DESC LIMIT 10"))
print('Avg Emp Hire Age', q_one("SELECT (SUM(HireDate)-SUM(BirthDate))/COUNT(HireDate) FROM Employee"))

# Part 3 Questions:
# - What are the ten most expensive items (per unit price) in the database *and*
#   their suppliers?
# - What is the largest category (by number of unique products in it)?
# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
#   (not name, region, or other fields) as the unique identifier for territories.

print('Top Exp and Sup', q_all("""
SELECT *
FROM OrderDetail, Product, Supplier
WHERE OrderDetail.ProductId=Product.Id AND Product.SupplierId=Supplier.Id
GROUP BY CompanyName
ORDER BY UnitPrice DESC LIMIT 10"""))

print('Largest Cat', q_all("""
SELECT MAX(DISTINCT(ProductName)) as Prod, COUNT(CategoryId)
FROM Product
ORDER BY Prod"""))

#part 4

#See elsewhere
