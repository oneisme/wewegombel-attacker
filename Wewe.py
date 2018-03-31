dari  impor_fungsi impor __future__ 
platform impor , os
def  tampil ( x ):
	w = { ' m ' : 31 , ' h ' : 32 , ' k ' : 33 , ' b ' : 34 , ' p ' : 35 , ' c ' : 36 }
	untuk saya di w:
		x = x.replace ( ' \ r % s ' % i, ' \ 033 [ % s ; 1m ' % w [i])
	x + = ' \ 033 [0m '
	x = x.replace ( ' \ r 0 ' , ' \ 033 [0m ' )
	cetak (x)
jika platform.python_version (). split ( ' . ' ) [ 0 ] ! =  ' 2 ' :
	tampil ( ' \ r m [!] Anda menggunakan versi python % s menggunakan versi 2.xx ' % v (). split ( '  ' ) [ 0 ])
	os.sys.exit ()
impor cookielib, kembali, urllib2, urllib, threading
coba :
	mekanisasi impor
kecuali  ImportError :
	tampil ( ' \ r m [!] SepertiNya Modul \ r cmechanize \ r m belum di install ... ' )
	os.sys.exit ()
def  Keluar ():
	simpan ()
	tampil ( ' \ r m [!] Keluar ' )
	os.sys.exit ()
log =  0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser ()
br.set_handle_robots ( Salah )
br.set_handle_equiv ( Benar )
br.set_handle_referer ( Benar )
br.set_cookiejar (cookielib.LWPCookieJar ())
br.set_handle_redirect ( Benar )
br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1 )
br.addheaders = [( ' User-Agent ' , ' Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Versi / 12.16 ' )]
def  bacaData ():
	global fid_bgroup, fid_bteman
	coba :
		fid_bgroup =  terbuka (os.sys.path [ 0 ] + ' /MBFbgroup.txt ' , ' r ' ) .readlines ()
	kecuali : lulus
	coba :
		fid_bteman =  buka (os.sys.path [ 0 ] + ' /MBFbteman.txt ' , ' r ' ) .readlines ()
	kecuali : lulus
def  inputD ( x , v = 0 ):
	sementara  1 :
		coba :
			a =  raw_input ( ' \ x1b [32; 1m % s \ x1b [31; 1m: \ x1b [33; 1m ' % x)
		kecuali :
			tampil ( ' \ n \ r m [!] Batal ' )
			keluar ()
		jika v:
			jika a.upper () di v:
				istirahat
			lain :
				Tampil ( ' \ r m [!] Masukan Opsinya Bro ... ' )
				terus
		lain :
			jika  len (a) ==  0 :
				Tampil ( ' \ r m [!] Masukan DENGAN Benar ' )
				terus
			lain :
				istirahat
	kembalikan a
def  inputM ( x , d ):
	sementara  1 :
		coba :
			i =  int (inputD (x))
		kecuali :
			tampil ( ' \ r m [!] Pilihan tidak ada ' )
			terus
		jika saya di d:
			istirahat
		lain :
			tampil ( ' \ r m [!] Pilihan tidak ada ' )
	kembalikan saya
def  simpan ():
	jika  len (id_bgroup) ! =  0 :
		tampil ( ' \ r h [*] Menyimpan hasil dari grup ' )
		coba :
			buka (os.sys.path [ 0 ] + ' /MBFbgroup.txt ' , ' w ' ) .write ( ' \ n ' .join (id_bgroup))
			tampil ( ' \ r h [!] Berhasil meyimpan \ r cMBFbgroup.txt ' )
		kecuali :
			Tampil ( ' \ r m [!] Gagal meyimpan ' )
	jika  len (id_bteman) ! =  0 :
		tampil ( ' \ r h [*] Menyimpan hasil daftar Teman ... ' )
		coba :
			buka (os.sys.path [ 0 ] + ' /MBFbteman.txt ' , ' w ' ) .tulis ( ' \ n ' .join (id_bteman))
			tampil ( ' \ r h [!] Berhasil meyimpan \ r cMBFbgteman.txt ' )
		kecuali :
			Tampil ( ' \ r m [!] Gagal meyimpan ' )
def  buka ( d ):
	tampil ( ' \ r h [*] Membuka \ r p ' + d)
	coba :
		x = br.open (d)
		br._factory.is_html =  Benar
		x = x.baca ()
	kecuali :
		tampil ( ' \ r m [!] Gagal membuka \ r p ' + d)
		keluar ()
	jika  ' <link rel = "redirect" href = " '  di x:
		kembali buka (br.find_link (). url)
	lain:
  
		kembali x
