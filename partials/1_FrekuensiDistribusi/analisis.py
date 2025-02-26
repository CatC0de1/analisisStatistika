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

def main():
    file_path = "././data.csv"
    df = load_data(file_path)
    
    # Kategori pertanyaan sesuai dengan urutan
    categories_q1 = ["Tidak Pernah", "Jarang", "1-2 kali seminggu", "3-5 kali seminggu", "Setiap Hari"]
        
    with open("partials/1_FrekuensiDistribusi/hasilAnalisis.txt", "w") as f:
        f.write("Distribusi Frekuensi untuk Pertanyaan 1:\n")
        f.write(frequency_distribution(df, df.columns[0], categories_q1).to_string() + "\n\n")

    print("Hasil telah disimpan di hasilAnalisis.txt")
    
if __name__ == "__main__":
    main()