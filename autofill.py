from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from random import randint
from datetime import datetime, timedelta

driver = webdriver.Chrome() #kalo menggunakan microsoft edge ganti menjadi webdriver.Edge()

# isi url dengan link form yang sesuai
url = "https://docs.google.com/forms/d/e/1FAIpQLSeepFnZoXDJNO6Li741fIEouheAQPOqj2wgBLxdb6xKWtGo8g/viewform" #Contoh link gform
driver.get(url)

names = ["Brian Pratama", "Muhammad Putra", "Jidan Galung", "Bunga Putri", "Ahmad Firdaus", #contoh array nama bebas bisa dipakai atau gak sesuai kebutuhan
        "Muhammad Rizki", "Arief Setiawan", "Faisal Rahman", "Rizky Pratama", "Aditya Nugraha",
        "Galih Prasetyo", "Rizaldi Ramadhan", "Aldi Saputra", "Ilham Akbar", "Dhani Firmansyah",
        "Arif Gilang", "Farhan Maulana", "Yoga Wiratama", "Fahmi Santoso", "Fauzan Nurhidayat",
        "Dwiki Pratama", "Rafi Prasetyo", "Rizal Effendi", "Ridwan Fauzi", "Siti Nurhaliza",
        "Fitriani Indah", "Rina Amelia", "Putri Dian", "Lia Anggraeni", "Rizka Sari",
        "Nurul Hidayah", "Dewi Ayu", "Laila Safitri", "Anisa Rahma",
        "Ratna Sari", "Eka Putri", "Aisyah Aulia", "Siska Permata",
        "Aulia Rahmi", "Sinta Dewi", "Dian Sari", "Suci Lestari", "Nabila Putri", "Ayu Lestari"]

motto = ["Usaha tidak akan menghianati hasil", #contoh array untuk isian panjang atau paragraf
         "Hidup adalah perjuangan.",
        "Lakukan yang terbaik dan biarkan Tuhan yang mengurus sisanya.",
        "Berani mengambil resiko adalah kunci menuju kesuksesan.",
        "Jadilah perubahan yang ingin Anda lihat di dunia. - Mahatma Gandhi",
        "Keberanian bukanlah ketiadaan rasa takut, tetapi bagaimana Anda mengatasi rasa takut itu. - Nelson Mandela",
        "Jangan menyesali hari yang telah berlalu. Jadikan setiap hari sebagai kesempatan untuk belajar dan berkembang.",
        "Lakukan apa yang benar, bukan apa yang mudah.",
        "Jika Anda tidak pernah gagal, itu berarti Anda tidak pernah mencoba hal baru.",
        "Jangan biarkan impian hanya menjadi impian. Wujudkan mereka dengan tindakan.",
        "Kesempatan tidak pernah datang dua kali. Manfaatkanlah setiap kesempatan yang ada."]

def fill_h1(nama, Motto, gender, hobi, gol_darah):
    #ini untuk pertanyaan form yang berisi jawaban singkat
    nama = random.choice(names)
    
    names.remove(nama)

    inputs = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    time.sleep(1)

    inputs.clear()
    inputs.send_keys(nama)

    #ini untuk pertanyaan form yang berisi bisa bentuk paragraf atau teks panjang
    Motto = random.choice(motto)
    
    text = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')

    time.sleep(1)
    
    text.clear()
    text.send_keys(Motto) 

    #gender berdasarkan nama
    if nama in ['Brian Pratama', 'Muhammad Putra', 'Jidan Galung', "Ahmad Firdaus",
                        "Muhammad Rizki", "Arief Setiawan", "Faisal Rahman", "Rizky Pratama",
                        "Aditya Nugraha", "Galih Prasetyo", "Rizaldi Ramadhan", "Aldi Saputra",
                        "Ilham Akbar", "Dhani Firmansyah", "Dicky Kurniawan", "Farhan Maulana",
                        "Yoga Wiratama", "Fahmi Santoso", "Fauzan Nurhidayat", "Dwiki Pratama",
                        "Rafi Prasetyo", "Rizal Effendi", "Ridwan Fauzi"]:
        driver.find_element('xpath', '//*[@id="i13"]').click()
    else:
        driver.find_element('xpath', '//*[@id="i16"]').click()  

    #ini jika bentuk pertanyaan formnya pilihan ganda 
    hobi = random.choice(["Menulis", "Membaca", "Olahraga", "Belajar", "Ngoding", "Rebahan"])
    if hobi == "Menulis":
        driver.find_element('xpath', '//*[@id="i24"]').click()
    elif hobi == "Membaca":
        driver.find_element('xpath', '//*[@id="i27"]').click()
    elif hobi == "Olahraga":
        driver.find_element('xpath', '//*[@id="i30"]').click()
    elif hobi == "Belajar":
        driver.find_element('xpath', '//*[@id="i33"]').click()
    elif hobi == "Ngoding":
        driver.find_element('xpath', '//*[@id="i36"]').click()
    elif hobi == "Rebahan":
        driver.find_element('xpath', '//*[@id="i39"]').click()
    #contoh jika pertanyaan formnya chekbox(dapat memilih lebih dari satu)
    elif hobi == "Ngoding" or hobi == "Rebahan":
            checkbox_ngoding = driver.find_element('xpath', '//*[@id="i36"]')
            checkbox_rebahan = driver.find_element('xpath', '//*[@id="i39"]')
            checkbox_ngoding.click()
            checkbox_rebahan.click()

    # jika pertanyaan form berbentuk dropdown
    gol_darah = random.choice(["A", "B", "AB", "O"])

    # Temukan elemen dropdown dan klik untuk membukanya
    dropdown_elem = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()

    time.sleep(1)
    
    if gol_darah == "A":
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]/span').click()
    elif gol_darah == "B":
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[4]/span').click()
    elif gol_darah == "AB":
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[5]/span').click()
    elif gol_darah == "O":
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[6]/span').click()

#membuat function baru yang berisi pertanyaan di halaman kedua
def fill_h2(rating, tanggal, jam):
    rating = random.choice([1, 2, 3, 4, 5])

    if rating == 1 :
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div').click()

    elif rating == 2 :
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div').click()
        
    elif rating == 3 :
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div').click()

    elif rating == 4 :
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div').click()

    elif rating == 5 :
        driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div').click()

    time.sleep(2)

    #jika pertanyaan berupa input tanggal atau kalender
    tanggal = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    
    # Buat input tanggal secara acak dalam rentang waktu tertentu
    # start_year = 1970 # batasan atas untuk tahun 
    # end_year = 2010 # batsan bawah untuk tahun
    # start_date = datetime(start_year, 1, 1)  # Tanggal awal, 1 Januari 1970
    # end_date = datetime(end_year, 12, 31)    # Tanggal akhir, 31 Desember tahun yang ditentukan
    # random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    # tanggal.send_keys(random_date.strftime("%d-%m-%Y"))

    # buat input tanggal hari ini
    date = datetime.now()
    tanggal.send_keys(date.strftime("%d-%m-%Y"))

    time.sleep(2)

    #jika pertanyaan berupa input waktu atau jam
    jam = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    jam_saat_ini = datetime.now()
    jam.send_keys(jam_saat_ini.strftime("%H"))

    time.sleep(1)

    menit = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
    menit_saat_ini = datetime.now()
    menit.send_keys(jam_saat_ini.strftime("%M"))

    time.sleep(2)

# isi form berkali kali 
for i in range(10):
    fill_h1('nama', 'Motto', 'gender', 'hobi', 'gol_darah')

    time.sleep(1)

    #untuk button berikutnya ke halaman selanjutnya jika masih ada halaman selanjutnya kalo tidak ada hapus saja
    next_button = WebDriverWait(driver, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
    )
    next_button.click()
    
    time.sleep(2)
    
    fill_h2('rating', 'tanggal', 'jam')

    #untuk button kirim atau submit 
    submit_button = WebDriverWait(driver, 250).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'))
    )
    submit_button.click()

    time.sleep(2)
    
    #untuk kirim atau submit response lainnya
    another_button = WebDriverWait(driver, 200).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
    )
    another_button.click()