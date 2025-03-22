# Sales-Insights-Visualization


## Overview
This project analyzes sales data using MySQL, Python (Pandas, Matplotlib, Seaborn), and SQLAlchemy. It connects to a MySQL database, retrieves relevant data, and visualizes key business insights such as total revenue, top-selling products, and sales distribution by region and customer segment.

## Features
- Connects to a MySQL database using SQLAlchemy.
- Retrieves and processes sales data.
- Computes total revenue and total number of orders.
- Identifies the top 5 best-selling products.
- Visualizes sales trends using Matplotlib and Seaborn.
- Analyzes sales by region and customer segment from a CSV file.

## Technologies Used
- **Python**
- **MySQL**
- **SQLAlchemy**
- **Pandas**
- **Matplotlib**
- **Seaborn**

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL Server
- Required Python libraries:

```sh
pip install pandas matplotlib seaborn sqlalchemy mysql-connector-python
```

## Database Setup
1. Create a MySQL database named `sales_data`.
2. Import your sales data into a table named `sales`.
3. Update the connection string in the script if needed:

```python
engine = create_engine("mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/sales_data")
```

## Usage
1. Run the script to test the database connection and retrieve data:

```sh
python sales_analysis.py
```

2. Ensure `train.csv` (containing `Region`, `Segment`, and `Sales` columns) is present in the working directory.

## SQL Queries Used
- Fetch top 10 sales records:
  ```sql
  SELECT * FROM sales LIMIT 10;
  ```
- Calculate total sales revenue:
  ```sql
  SELECT SUM(Sales) AS total_revenue FROM sales;
  ```
- Count total number of orders:
  ```sql
  SELECT COUNT(*) AS total_orders FROM sales;
  ```
- Identify top 5 best-selling products:
  ```sql
  SELECT `Product Name`, SUM(Sales) AS total_sales
  FROM sales
  GROUP BY `Product Name`
  ORDER BY total_sales DESC
  LIMIT 5;
  ```

## Visualizations
- **Top 5 Best-Selling Products** (Bar Chart)
- **Sales by Region** (Bar Chart using `train.csv`)
- **Sales by Customer Segment** (Bar Chart using `train.csv`)

## Error Handling
The script is wrapped in a `try-except` block to handle connection or query failures.

## Visualizations

### 📊 Top 5 Best-Selling Products
![Top 5 Best-Selling Products](https://raw.githubusercontent.com/mohan10jaiswal/Sales-Insights-Visualization/main/Output/OP1.png)

### 🌍 Total Sales by Region
![Total Sales by Region](https://raw.githubusercontent.com/mohan10jaiswal/Sales-Insights-Visualization/main/Output/OP2.png)

### 👥 Sales by Customer Segment
![Sales by Customer Segment](https://raw.githubusercontent.com/mohan10jaiswal/Sales-Insights-Visualization/main/Output/OP3.png)



## Author
**Mohan Kumar**

