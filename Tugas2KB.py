import math
import pandas as pd

biaya_produksi_per_kemasan = 800  # dalam Rupiah
permintaan_harian = 25000  # dalam kemasan

def hitung_biaya_produksi(jumlah_kemasan):
    return jumlah_kemasan * biaya_produksi_per_kemasan

def main():
    total_biaya = hitung_biaya_produksi(permintaan_harian)
    
    data = {
        'Parameter': ['Biaya Produksi per Kemasan (Rp)', 'Permintaan Harian (kemasan)', 'Total Biaya Produksi (Rp)'],
        'Nilai': [biaya_produksi_per_kemasan, permintaan_harian, total_biaya]
    }
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()

