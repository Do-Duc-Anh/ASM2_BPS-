import pandas as pd

# Đường dẫn tới file Excel
file_path = 'ASM2_table.xlsx'

try:
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    # Kiểm tra dữ liệu ban đầu
    print("Dữ liệu ban đầu:")
    print(data.head())
    print("\nThông tin dữ liệu:")
    print(data.info())
    print("\nSố lượng giá trị trống trong mỗi cột:")
    print(data.isnull().sum())

    # Xử lý dữ liệu trống
    # Kiểm tra và điền giá trị trống
    if data.isnull().sum().any():
        # Điền giá trị trống bằng giá trị trung bình của cột (nếu cột đó là số)
        for column in data.select_dtypes(include=['float64', 'int64']).columns:
            data[column].fillna(data[column].mean(), inplace=True)

        # Điền giá trị trống bằng chuỗi 'Unknown' cho các cột chuỗi
        for column in data.select_dtypes(include=['object']).columns:
            data[column].fillna('Unknown', inplace=True)

    # Xử lý dữ liệu lỗi
    if 'ChannelKey' in data.columns and (data['ChannelKey'] < 0).any():
        data.loc[data['ChannelKey'] < 0, 'ChannelKey'] = data['ChannelKey'].mean()

    # Chuẩn hóa dữ liệu

    # Kiểm tra lại dữ liệu sau khi làm sạch
    print("\nDữ liệu sau khi làm sạch:")
    print(data.head())
    print("\nThông tin dữ liệu sau khi làm sạch:")
    print(data.info())
    print("\nSố lượng giá trị trống trong mỗi cột sau khi làm sạch:")
    print(data.isnull().sum())

    # Lưu dữ liệu đã làm sạch vào file mới
    cleaned_file_path = '/mnt/data/cleaned_Data_Sale.csv'
    data.to_csv(cleaned_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào file '{cleaned_file_path}'")

except FileNotFoundError:
    print(f"File không tồn tại: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")