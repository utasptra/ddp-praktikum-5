kendaraan = ["Kodrat", "Motor", 200, "Coklat", "Ban - Cacing"]

harga_kendaraan = 2500000 
tipe_kendaraan = "Drag"
merk_kendaraan = "Yamaha"

kendaraan.append(harga_kendaraan)  
kendaraan.append(tipe_kendaraan)  
print(kendaraan)
print()

def hitung_luas():
    pilihan = input("Pilih bangun datar (1: persegi, 2: lingkaran, 3: segitiga): ")

    match pilihan:
        case "1":
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas_persegi = sisi * sisi
            print(f"Luas persegi: {luas_persegi}")

        case "2":
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas_lingkaran = 3.14 * jari_jari * jari_jari
            print(f"Luas lingkaran: {luas_lingkaran}")

        case "3":
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas_segitiga = 0.5 * alas * tinggi
            print(f"Luas segitiga: {luas_segitiga}")

        case _:
            print("Salah pilih angka")

if __name__ == "__main__":
    hitung_luas()