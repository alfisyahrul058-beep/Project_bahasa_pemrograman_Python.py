print("===================================================================")
print("               Selamat Datang di Program Gaji karyawan             ")
print("===================================================================")

golongan = str(input("Masukkan jenis Karyawan [ Golongan A / Golongan B ] = "))
Pendidikan = str(input("Masukkan Status Pendidikan Terakhir Karyawan [ SMA / S1 ] = "))

if golongan == 'A' or golongan == 'a' :
    if Pendidikan == 'SMA' or Pendidikan == 'sma' :
        gaji_pokok_pendidikan_sma_golongan_a = 3000000
        tunjangan_golongan_a_pendidikan_sma=  2000000
        gaji_yang_didapat_karyawan = gaji_pokok_pendidikan_sma_golongan_a + tunjangan_golongan_a_pendidikan_sma
        print('Gaji Pokok : ','Rp', gaji_pokok_pendidikan_sma_golongan_a)
        print('Tunjangan  : ','Rp', tunjangan_golongan_a_pendidikan_sma)
    elif Pendidikan == 'S1' or Pendidikan == 's1' :
        gaji_pokok_pendidikan_s1_golongan_a= 4000000
        tunjangan_golongan_a_pendidikan_s1 =  3000000
        gaji_yang_didapat_karyawan = gaji_pokok_pendidikan_s1_golongan_a + tunjangan_golongan_a_pendidikan_s1
        print('Gaji Pokok : ','Rp', gaji_pokok_pendidikan_s1_golongan_a)
        print('Tunjangan  : ','RP', tunjangan_golongan_a_pendidikan_s1) 
    else :
        print('Status Pendidikan Tidak ditemukan !')
elif golongan == 'B' or golongan == 'b' :
    if Pendidikan == 'SMA' or Pendidikan == 'sma' :
       gaji_pokok_pendidikan_sma_golongan_b = 4000000
       tunjangan_golongan_b_pendidikan_sma =  3000000
       gaji_yang_didapat_karyawan = gaji_pokok_pendidikan_sma_golongan_b + tunjangan_golongan_b_pendidikan_sma
       print('Gaji Pokok : ','Rp', gaji_pokok_pendidikan_sma_golongan_b)
       print('Tunjangan  : ','Rp', tunjangan_golongan_b_pendidikan_sma)
    elif Pendidikan == 'S1' or Pendidikan == 's1' :
        gaji_pokok_pendidikan_s1_golongan_b= 6000000
        tunjangan_golongan_b_pendidikan_s1 =  5000000
        gaji_yang_didapat_karyawan = gaji_pokok_pendidikan_s1_golongan_b + tunjangan_golongan_b_pendidikan_s1
        print('Gaji Pokok : ','Rp', gaji_pokok_pendidikan_s1_golongan_b)
        print('Tunjangan  : ','Rp', tunjangan_golongan_b_pendidikan_s1)
    else :
        print('Status Pendidikan Tidak ditemukan !')
else :
    print('jenis Golongan Tidak ditemukan !')
    print('ngetiknya jangan ngasal !')

print('========================================================================')
print('     jenis Karyawan        : ', golongan )
print('Status Pendidikan Karyawan : ', Pendidikan)
print('Gaji / Penghasilan yang di dapat ( Perbulan ) : ','Rp', gaji_yang_didapat_karyawan)
print('========================================================================')
print('                      Terima Kasih Kembali                              ')
print('========================================================================')
