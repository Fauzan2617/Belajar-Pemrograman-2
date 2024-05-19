import unittest
 
class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())
    
    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')
    
if __name__ == '__main__':
    # Test Runner
    unittest.main()
    
'''
Mari kita bahas satu per satu dari kode di atas.

1.	import unittest: Ini adalah baris yang mengimpor modul unittest, yang digunakan untuk menulis dan menjalankan unit test dalam Python.
2.	class TestStringMethods(unittest.TestCase):: Ini adalah deklarasi kelas yang akan berisi serangkaian metode pengujian. Kelas ini menggantungkan kelas unittest.TestCase, yang menyediakan berbagai metode bantu untuk menulis unit test.
3.	def test_strip(self):: Ini adalah definisi metode pengujian pertama yang disebut test_strip. Metode ini akan memeriksa fungsi strip() yang dimiliki oleh string.
4.	self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding'): Ini adalah pernyataan pengujian yang membandingkan hasil dari operasi strip('c.mow') pada string 'www.dicoding.com' dengan string 'dicoding'. Jika kedua hasil tersebut sama, maka pengujian akan berhasil.
5.	def test_isalnum(self):: Ini adalah definisi metode pengujian kedua yang disebut test_isalnum. Metode ini akan memeriksa fungsi isalnum() yang digunakan untuk memeriksa apakah string hanya terdiri dari karakter alfanumerik.
6.	self.assertTrue('c0d1ng'.isalnum()): Ini adalah pernyataan pengujian yang memeriksa apakah string 'c0d1ng' hanya terdiri dari karakter alfanumerik. Jika benar, pengujian akan berhasil.
7.	self.assertFalse('c0d!ng'.isalnum()): Ini adalah pernyataan pengujian yang memeriksa apakah string 'c0d!ng' hanya terdiri dari karakter alfanumerik. Jika salah, pengujian akan berhasil.
8.	def test_index(self):: Ini adalah definisi metode pengujian ketiga yang disebut test_index. Metode ini akan memeriksa fungsi index() yang digunakan untuk mencari indeks pertama dari substring dalam sebuah string.
9.	s = 'dicoding': Membuat variabel s dan menginisialisasinya dengan string 'dicoding'.
10.	self.assertEqual(s.index('coding'), 2): Ini adalah pernyataan pengujian yang memeriksa apakah fungsi index('coding') pada string s mengembalikan nilai 2. Jika benar, pengujian akan berhasil.
11.	with self.assertRaises(ValueError):: Ini adalah pernyataan pengujian yang menunjukkan bahwa kita akan menangkap pengecualian tertentu. Dalam hal ini, kita ingin menangkap pengecualian ValueError.
12.	s.index('decode'): Ini adalah pemanggilan fungsi index() pada string s dengan mencari substring 'decode'. Karena 'decode' tidak ada dalam string 'dicoding', maka ini seharusnya akan menghasilkan pengecualian ValueError.
13.	if __name__ == '__main__':: Ini adalah baris yang memeriksa apakah skrip dijalankan secara langsung sebagai program utama.

'''