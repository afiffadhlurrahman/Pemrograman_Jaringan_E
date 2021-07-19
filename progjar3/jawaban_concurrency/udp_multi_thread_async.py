from library import download_gambar, get_url_list, send_image
import time
import datetime
import concurrent.futures


def download_semua():
    IP_SERVER1 = "192.168.122.129"
    IP_SERVER2 = "192.168.122.77"
    texec = dict()
    urls = get_url_list()
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    flag = 0
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        if flag == 0:
            print("SERVER 1")
            # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
            texec[k] = task.submit(send_image, IP_SERVER1, 4004, f"{k}.jpg")
            flag += 1
        elif flag == 1:
            print("SERVER 2")
            texec[k] = task.submit(send_image, IP_SERVER2, 4004, f"{k}.jpg")

            # setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan memanggil result
    for k in urls:
        status_task[k] = texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)


# fungsi download_gambar akan dijalankan secara multithreading

if __name__ == '__main__':
    download_semua()
