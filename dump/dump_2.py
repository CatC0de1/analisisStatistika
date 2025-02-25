import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def frequency_distribution(data, column_name, categories):
    frequency = data[column_name].value_counts().reindex(categories, fill_value=0)
    total = frequency.sum()
    relative_freq = frequency / total
    cumulative_freq_le = frequency.cumsum()
    cumulative_freq_ge = frequency[::-1].cumsum()[::-1]
    
    relative_cumulative_freq_le = cumulative_freq_le / total
    relative_cumulative_freq_ge = cumulative_freq_ge / total
    
    result = pd.DataFrame({
        'Frequency': frequency,
        'Relative Frequency': relative_freq.round(4),
        'Cumulative Frequency (<=)': cumulative_freq_le,
        'Cumulative Frequency (>=)': cumulative_freq_ge,
        'Relative Cumulative Frequency (<=)': relative_cumulative_freq_le.round(4),
        'Relative Cumulative Frequency (>=)': relative_cumulative_freq_ge.round(4)
    })
    return result

def central_tendency(data, column_name, mapping):
    numeric_data = data[column_name].map(mapping)
    mean = numeric_data.mean()
    median = numeric_data.median()
    mode = numeric_data.mode()[0] if not numeric_data.mode().empty else None
    
    result = f"Mean: {mean:.2f}\nMedian: {median}\nMode: {mode}\n"
    return result

def main():
    file_path = "responden.csv"  # Ubah dengan path file yang sesuai
    df = load_data(file_path)
    
    # Kategori pertanyaan sesuai dengan urutan
    categories_q1 = ["Tidak Pernah", "Jarang", "1-2 kali seminggu", "3-5 kali seminggu", "Setiap Hari"]
    categories_q2 = ["<1 Jam", "1 - 3 Jam", "4 - 6 Jam", "> 6 Jam"]
    categories_q3q4 = ["Sangat Tidak Bagus", "Tidak Bagus", "Netral", "Bagus", "Sangat Bagus"]
    
    # Mapping kategori ke nilai numerik untuk central tendency
    q1_mapping = {"Tidak Pernah": 1, "Jarang": 2, "1-2 kali seminggu": 3, "3-5 kali seminggu": 4, "Setiap Hari": 5}
    q2_mapping = {"<1 Jam":1, "1 - 3 Jam":2, "4 - 6 Jam":3, "> 6 Jam":4}
    q3q4_mapping = {"Sangat Tidak Bagus":1, "Tidak Bagus":2, "Netral":3, "Bagus":4, "Sangat Bagus":5}
    
    with open("analisis.txt", "w") as f:
        f.write("Distribusi Frekuensi untuk Pertanyaan 1:\n")
        f.write(frequency_distribution(df, df.columns[0], categories_q1).to_string() + "\n\n")
        f.write("Ukuran Pemusatan Data untuk Pertanyaan 1:\n")
        f.write(central_tendency(df, df.columns[0], q1_mapping) + "\n\n")

        f.write("Distribusi Frekuensi untuk Pertanyaan 2:\n")
        f.write(frequency_distribution(df, df.columns[1], categories_q2).to_string() + "\n\n")
        f.write("Ukuran Pemusatan Data untuk Pertanyaan 2:\n")
        f.write(central_tendency(df, df.columns[1], q2_mapping) + "\n\n")

        f.write("Distribusi Frekuensi untuk Pertanyaan 3:\n")
        f.write(frequency_distribution(df, df.columns[2], categories_q3q4).to_string() + "\n\n")
        f.write("Ukuran Pemusatan Data untuk Pertanyaan 3:\n")
        f.write(central_tendency(df, df.columns[2], q3q4_mapping) + "\n\n")

        f.write("Distribusi Frekuensi untuk Pertanyaan 4:\n")
        f.write(frequency_distribution(df, df.columns[3], categories_q3q4).to_string() + "\n\n")
        f.write("Ukuran Pemusatan Data untuk Pertanyaan 4:\n")
        f.write(central_tendency(df, df.columns[3], q3q4_mapping) + "\n\n")
    
    print("Hasil telah disimpan di analisis.txt")
    
if __name__ == "__main__":
    main()