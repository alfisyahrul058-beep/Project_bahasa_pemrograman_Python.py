print('--------------------------------------------------')
nama_penumpang = str(input('Masukkan Nama anda = '))
berat_bagasi_pesawat = int(input('Berat Bagasi ( kg ) = '))

if berat_bagasi_pesawat > 20 :
    kelebihan = berat_bagasi_pesawat - 20 
    print('[ PERINGATAN ! ] Bagasi anda melebihi batas 20 kg !')
    print('Kelebihan Berat :', kelebihan,'kg')
    biaya_tambahan = kelebihan * 50000
else :
    biaya_tambahan = 0 
    print('Tidak ada biaya yang dikenakan')

print('===================================================')
print('Nama Penumpang : ', nama_penumpang)
print('Berat Bagasi   : ', berat_bagasi_pesawat,'kg' )
print('Biaya Tambahan : Rp', biaya_tambahan)
print('===================================================')
