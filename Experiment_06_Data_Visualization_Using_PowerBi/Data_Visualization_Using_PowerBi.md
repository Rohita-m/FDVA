# VI. Data Visualization Using PowerBi

## AIM:
To learn the Power BI Desktop interface and workflow by connecting to Excel/CSV/SQL data sources, creating basic visualizations (bar, line, pie), writing calculated columns and measures (DAX), and assembling an interactive dashboard that answers simple business questions.

## PROCEDURE:

### 1. Open Power BI Desktop & Inspect Interface
1. Launch Power BI Desktop.
2. Note key panes: Fields, Visualizations, Filters, Data/Report/Model view.
3. Switch to Data view briefly to understand where tables and columns appear.

### 2. Connect to Data Sources
**A. Excel**
1. Home → Get data → Excel → choose `SalesData.xlsx`.
2. In Navigator, check the Sales sheet and click Load.

**B. CSV**
1. Home → Get data → Text/CSV → choose `Targets.csv`.
2. Preview and click Load.

### 3. Clean & Transform (Power Query)
1. Home → Transform data to open Power Query Editor.
2. For Sales table:
   - Ensure Date column has Date datatype.
   - Create a TotalSales column: Quantity * UnitPrice (Add Column → Custom Column → `=[Quantity]*[UnitPrice]`).
   - Trim whitespace in text columns; remove duplicates if needed.
3. For `Targets.csv`:
   - Convert Month to date or text format consistently (e.g., YYYY-MM).
4. Close & Apply.

### 4. Create Basic Visualizations
Create a new report page and add visualizations:
1. **Bar chart** — Sales by Category
   - Axis: Category
   - Value: Total Sales
   - Add data labels, sort descending.
2. **Line chart** — Monthly Sales Trend
   - Axis: Sales[YearMonth] (set type to categorical or continuous as needed)
   - Values: Total Sales
   - Add a slicer for Region.
3. **Pie chart / Donut** — Sales proportion by Region
   - Legend: Region
   - Values: Total Sales
4. **Card visuals** — Key KPIs
   - Cards showing Total Sales, Total Quantity, Avg Order Value.
5. **Table / Matrix** — Top 10 Products by Sales
   - Columns: Product, Total Sales, Total Quantity
   - Use Top N filter on Product to show top 10.

### 5. Build a Dashboard-like Report Page
1. Arrange visuals into a clean layout:
   - Top row: KPI cards and a date/region slicer.
   - Left column: bar chart (Category) & table (Top products).
   - Right column: line chart (trend) & pie/donut (region share).
   - Bottom: gauge or variance chart comparing sales vs target.
2. Add titles, tooltips, and consistent formatting (font sizes, number formats).
3. Save the `.pbix` file.

## RESULT:
Thus, the given program was written and executed successfully.
