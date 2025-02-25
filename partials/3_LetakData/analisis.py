import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    
    return df

def quartiles(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    q1 = numeric_data.quantile(0.25)
    q2 = numeric_data.quantile(0.50)
    q3 = numeric_data.quantile(0.75)
    return f"Quartiles [Kelas Online]:\nQ1={q1}, Q2={q2}, Q3={q3}\n\n"

def deciles(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    deciles = [numeric_data.quantile(i / 10) for i in range(1, 10)]
    return f"Deciles [Belajar]:\n{', '.join(map(str, deciles))}\n\n"

def percentiles(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    percentiles = [numeric_data.quantile(i / 100) for i in range(1, 100)]
    return f"Percentiles [Mengerjakan Tugas]:\n{', '.join(map(str, percentiles[:10]))}...\n\n"


def data_location(data):
    q6q8_mapping = {"Tidak Pernah":1, "Jarang":2, "Terkadang":3, "Sering":4, "Selalu":5}
    result = ""
    result += quartiles(data, data.columns[5], q6q8_mapping)
    result += deciles(data, data.columns[6], q6q8_mapping)
    result += percentiles(data, data.columns[7], q6q8_mapping)
    return result

def main():
    file_path = "././data.csv"
    df = load_data(file_path)
    
    with open("partials/3_LetakData/hasilAnalisis.txt", "w") as f:
        f.write("Letak Data:\n")
        f.write("Pertanyaan: Apakah kamu memanfaatkan Wifi kampus untuk menunjang kegiatan akademik\n\n\n")
        f.write(data_location(df))
    
    print("Hasil telah disimpan di hasilAnalisis.txt")
    
if __name__ == "__main__":
    main()