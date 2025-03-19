import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#  Create connection using SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:Mohan%40123@localhost/sales_data")

#  Test connection
try:
    with engine.connect() as connection:
        print("Successfully connected to MySQL!")

    #  Query 1: Fetch top 10 rows from sales
    query = "SELECT * FROM sales LIMIT 10;"
    df = pd.read_sql(query, engine)
    print(df)

    # Query 2: Check column names and data types
    print("Info about data:")
    df.info()

    print(df.head())  

    #  Query 3: Total Sales Revenue
    query = "SELECT SUM(Sales) AS total_revenue FROM sales;"
    df = pd.read_sql(query, engine)
    print("\n3rd query Total Revenue:")
    print(df)

    #  Query 4: Total Number of Orders
    query = "SELECT COUNT(*) AS total_orders FROM sales;"
    df = pd.read_sql(query, engine)
    print("\n 4th query Total Orders:")
    print(df)

    #  Query 5: Top 5 Best-Selling Products (Visualization)
    query = """
    SELECT `Product Name`, SUM(Sales) AS total_sales
    FROM sales
    GROUP BY `Product Name`
    ORDER BY total_sales DESC
    LIMIT 5;
    """
    df = pd.read_sql(query, engine)
    print("\n 5th query : Top 5 Best-Selling Products:")
    print(df)
    
   
    #  1st Plot : Plot Bar Chart - Top 5 Best-Selling Products
   
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df["Product Name"], y=df["total_sales"], palette="viridis")

    plt.xlabel("Product Name")
    plt.ylabel("Total Sales")
    plt.title("Top 5 Best-Selling Products")

    plt.xticks(rotation=65, ha='right') # Rotate product names for better readability
    plt.show()
       
     
    # 2nd Plot :  Plot Bar Chart - Sales by region (central , south , East , West ) 

    df = pd.read_csv("train.csv") 
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()
    plt.figure(figsize=(10,5))
    sns.barplot(x="Region", y="Sales", data=region_sales, palette="viridis")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)  # Rotate x-axis labels if needed
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()    
     
    # 3rd Plot :  Plot Bar Chart - Sales by Customer Segment 

    df = pd.read_csv("train.csv") 
    segment_sales = df.groupby("Segment")["Sales"].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Segment", y="Sales", data=segment_sales, palette="coolwarm")
    plt.title("Total Sales by Customer Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Total Sales")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()



except Exception as e:
    print(f" Error: {e}")
