from file_client_cli import remote_get
import time
import datetime
import threading
import socket


def send_all():
    texec = dict()
    daftar = 'pokijan.jpg'
    catat_awal = datetime.datetime.now()
    for k in range(100):
        print(f"mengirim {k}")
        waktu = time.time()
        # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi send >
        texec[k] = threading.Thread(target=remote_get, args=(daftar,))
        texec[k].start()
    # setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in range(100):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d{catat_akhir}")


# fungsi send all akan dijalankan secara multithreading
if __name__ == '__main__':
    send_all()
