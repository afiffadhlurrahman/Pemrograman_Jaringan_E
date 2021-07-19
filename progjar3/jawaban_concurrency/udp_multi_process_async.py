from library import download_gambar, get_url_list, send_image
import time
import datetime
from multiprocessing import Process, Pool


def download_semua():
    IP_SERVER1 = "192.168.122.129"
    IP_SERVER2 = "192.168.122.77"
    texec = dict()
    urls = get_url_list()
    status_task = dict()
    flag = 0
    # 2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    task_pool = Pool(processes=20)
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        if flag == 0:
            print("SERVER 1")
            texec[k] = task_pool.apply_async(
                func=send_image, args=(IP_SERVER1, 4004, f"{k}.jpg"))
            flag += 1
        elif flag == 1:
            print("SERVER 2")
            texec[k] = task_pool.apply_async(
                func=send_image, args=(IP_SERVER2, 4004, f"{k}.jpg"))
    # setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in urls:
        status_task[k] = texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)


# fungsi download_gambar akan dijalankan secara multi process

if __name__ == '__main__':
    download_semua()
