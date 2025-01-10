# Amazon Sales Analysis Project

This repository contains the cleaned dataset and analysis code for the Amazon Sales Analysis project. The objective of this project is to provide actionable insights into sales performance, product trends, fulfillment efficiency, customer segmentation, and geographical distribution of sales.


## **Key Objectives**
1. **Sales Overview**: Understand sales trends and patterns over time.
2. **Product Analysis**: Identify popular product categories, sizes, and quantities sold.
3. **Fulfillment Analysis**: Evaluate fulfillment methods and their efficiency.
4. **Customer Segmentation**: Analyze customer behavior based on location and purchase habits.
5. **Geographical Analysis**: Explore sales distribution across states and cities.
6. **Business Insights**: Provide recommendations for optimizing sales strategies and improving customer satisfaction.


## **Deliverables**
1. Comprehensive cleaned dataset for analysis.
2. Visualizations illustrating trends and insights (built using Power BI).
3. Actionable insights for inventory management, sales strategies, and customer service improvements.


## **Steps to Reproduce**
### **1. Data Cleaning in Python**
The dataset was cleaned using Python to ensure data quality:
- Removed duplicates and handled missing values.
- Standardized categorical columns.
- Engineered features such as profit margins and extracted months from dates.

you can find the Python code used for data cleaning in `clean_data.py`.

### **2. Visualization in Power BI**
- Data was imported into Power BI for visualization.
- Charts include sales trends, product performance, fulfillment methods, and geographical analysis.
- Months were extracted from the cleaned `Order Date` column to aggregate sales data by month.


## **Project Files**
1. `cleaned_amazon_data.csv`: Cleaned dataset ready for analysis.
2. `clean_data.py`: Python script used to clean the raw dataset.
3. `amazon_sales.pbix`: Power BI report file with visualizations.
4. `README.md`: This file, explaining the project details.


## **Insights**
1. **Top Categories**: Identify high-performing product categories.
2. **Sales Trends**: Monitor seasonal and monthly sales fluctuations.
3. **Fulfillment Efficiency**: Evaluate shipping methods for optimization.
4. **Customer Behavior**: Segment customers for targeted marketing.
