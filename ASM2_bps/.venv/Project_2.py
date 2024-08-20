import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file Excel
file_path = 'ASM2_table.xlsx'
data = pd.read_excel(file_path)

# Thiết lập phong cách chung cho biểu đồ
plt.style.use('ggplot')  # Sử dụng phong cách 'ggplot'
# Lọc các cột số trước khi tính ma trận tương quan
numeric_data = data.select_dtypes(include=[np.number])

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='TotalAmount', data=numeric_data, color='green', marker='o')
plt.title('Scatter Plot of Total Amount vs Quantity', fontsize=16)
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Total Amount', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['TotalAmount'], bins=20, color='purple', edgecolor='black')
plt.title('Histogram of Total Amount', fontsize=16)
plt.xlabel('Total Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['TotalAmount'], kde=True, color='blue', bins=20)
plt.title('Distribution Plot of Total Amount', fontsize=16)
plt.xlabel('Total Amount', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(12, 6))
for channel in data['SalesChannel'].unique():
    sns.kdeplot(data[data['SalesChannel'] == channel]['TotalAmount'], label=channel)
plt.title('Density Plot of Total Amount by Sales Channel', fontsize=16)
plt.xlabel('Total Amount', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(title='Sales Channel')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
