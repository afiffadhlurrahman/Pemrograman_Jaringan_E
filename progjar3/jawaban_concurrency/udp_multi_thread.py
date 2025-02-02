from library import download_gambar, get_url_list, send_image
import time
import datetime
import threading


def download_semua():
    IP_SERVER1 = "192.168.122.129"
    IP_SERVER2 = "192.168.122.77"
    texec = dict()
    urls = get_url_list()
    flag = 0
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        if flag == 0:
            print("SERVER 1")
            # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
            texec[k] = threading.Thread(
                target=send_image, args=(IP_SERVER1, 5005, f"{k}.jpg"))
            flag += 1
        elif flag == 1:
            print("SERVER 2")
            texec[k] = threading.Thread(
                target=send_image, args=(IP_SERVER2, 5005, f"{k}.jpg"))
        texec[k].start()

    # setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in urls:
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


# fungsi download_gambar akan dijalankan secara multithreading
if __name__ == '__main__':
    download_semua()
