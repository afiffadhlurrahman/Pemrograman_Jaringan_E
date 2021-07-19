import logging
import requests
import os
import time
import datetime
import socket


def get_url_list():
    urls = dict()
    urls['kompas'] = 'https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg'
    urls['its'] = 'https://www.its.ac.id/wp-content/uploads/2020/07/Lambang-ITS-2-300x300.png'
    # urls['detik'] = 'https://akcdn.detik.net.id/community/media/visual/2021/07/16/1307596016_169.jpg'
    # urls['file1'] = 'https://file-examples-com.github.io/uploads/2018/04/file_example_MOV_480_700kB.mov'
    # urls['file2']='https://file-examples-com.github.io/uploads/2018/04/file_example_MOV_1280_1_4MB.mov'
    # urls['file3'] = 'https://file-examples-com.github.io/uploads/2017/02/zip_2MB.zip'
    return urls


def download_gambar(url=None, tuliskefile=False):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/gif'] = 'gif'
    tipe['image/jpeg'] = 'jpg'
    tipe['application/zip'] = 'jpg'
    tipe['video/quicktime'] = 'mov'
    time.sleep(2)  # untuk simulasi, diberi tambahan delay 2 detik

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{namafile}.{ekstensi}", "wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir = datetime.datetime.now()
        logging.warning(
            f"writing {namafile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False


def send_image(IP_ADDRESS, PORT, filename):
    print(IP_ADDRESS, PORT, filename)
    ukuran = os.stat(filename).st_size
    sckclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    fp = open(filename, 'rb')
    file = fp.read()
    for i in file:
        file_bytes = bytes([i])
        sckclient.sendto(file_bytes, (IP_ADDRESS, PORT))
        sent = sent+1


if __name__ == '__main__':
    # check fungsi
    k = download_gambar(
        'https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
    print(k)
