import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    
    return df

def mean_value(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    mean = numeric_data.mean()
    return f"Mean [Kecepatan]: {mean:.2f}\n"

def median_value(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    median = numeric_data.median()
    return f"Median [Kestabilan]: {median}\n"

def mode_value(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    mode = numeric_data.mode()
    mode_result = ", ".join(map(str, mode)) if not mode.empty else "No mode"
    return f"Mode [Aksesibilitas]: {mode_result}\n"

def central_tendency(data):
    q3q5_mapping = {"Sangat Tidak Bagus":1, "Tidak Bagus":2, "Netral":3, "Bagus":4, "Sangat Bagus":5}
    result = ""
    result += mean_value(data, data.columns[2], q3q5_mapping)
    result += median_value(data, data.columns[3], q3q5_mapping)
    result += mode_value(data, data.columns[4], q3q5_mapping)
    return result

def main():
    file_path = "././data.csv"
    df = load_data(file_path)
    
    with open("partials/2_PemusatanData/hasilAnalisis.txt", "w") as f:
        f.write("Ukuran Pemusatan Data:\n")
        f.write("Pertanyaan: Bagaimana kualitas Wifi Kampus dalam menunjang kegiatan akademik\n\n")
        f.write(central_tendency(df))
    
    print("Hasil telah disimpan di hasilAnalisis.txt")
    
if __name__ == "__main__":
    main()