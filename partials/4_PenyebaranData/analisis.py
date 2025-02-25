import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    
    return df

def range_value(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    range_val = numeric_data.max() - numeric_data.min()
    return f"Range [Kelas Online]:\n{range_val}\n\n"

def interquartile_range(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    q1 = numeric_data.quantile(0.25)
    q3 = numeric_data.quantile(0.75)
    iqr = q3 - q1
    return f"Interquartile Range [Belajar]:\n{iqr}\n\n"

def ordinal_dispersion_index(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    mean_val = numeric_data.mean()
    max_val = max(mapping.values())
    min_val = min(mapping.values())
    dispersion_index = (mean_val - min_val) / (max_val - min_val)
    return f"Ordinal Dispersion Index [Mengerjakan Tugas]:\n{dispersion_index:.2f}\n\n"

def data_location(data):
    q9q11_mapping = {"Sangat Tidak Setuju":1, "Tidak Setuju":2, "Netral":3, "Setuju":4, "Sangat Setuju":5}
    result = ""
    result += range_value(data, data.columns[8], q9q11_mapping)
    result += interquartile_range(data, data.columns[9], q9q11_mapping)
    result += ordinal_dispersion_index(data, data.columns[10], q9q11_mapping)
    return result

def main():
    file_path = "././data.csv"
    df = load_data(file_path)
    
    with open("partials/4_PenyebaranData/hasilAnalisis.txt", "w") as f:
        f.write("Penyebaran Data:\n")
        f.write("Pertanyaan: Dengan Wifi yang mendukung, apakah kamu lebih termotivasi dalam mengikuti kegiatan akademik\n\n\n")
        f.write(data_location(df))
    
    print("Hasil telah disimpan di hasilAnalisis.txt")
    
if __name__ == "__main__":
    main()