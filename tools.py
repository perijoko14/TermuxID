import os, sys, time, urllib, requests

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

def logo():
    os.system('pkg install screenfetch')
    os.system('screenfetch -A u')


def menu():
	os.system('clear')
	logo()
	print 'Menu pilihan'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '1. Dark-fb v1.6'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '2. Dark-fb v1.7'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '3. Autombf v2'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '4. Ycloner'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '5. Sms Gratis'
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '0. Keluar'
	pilih()

def pilih():
    zedd = raw_input('Pilih\x1b[1;91m-\xe2\x96\xba\x1b[1;97m')
    if zedd == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih()
    else:
        if zedd == '1':
            dark()
        else:
            if zedd == '2':
                darkfb()
            else:
            	if zedd == '3':
            	    autombf()
                else:
                    if zedd == '4':
                        yclone()
                    else:
                    	if zedd == '5':
                    	    sms()
                        else:
                            if zedd == '0':
                                jalan('Github : https://github.com/perijoko14\nWa : 089508086318\nGoBye^_^')
                                exit()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
                                pilih()


def dark():
    os.system('clear')
    logo()
    jalan('Tunggu Sebentar...')
    os.system('python2 a.py')

def darkfb():
    os.system('clear')
    logo()
    jalan('Tunggu Sebentar...')
    os.system('python2 b.py')

def autombf():
	os.system('clear')
	logo()
	jalan('Tunggu Sebentar...')
	os.system('python2 c.py')


def yclone():
	os.system('clear')
	logo()
	jalan('Tunggu Sebentar...')
	os.system('python2 d.py')

def sms():
	os.system('clear')
	logo()
	jalan('Tunggu Sebentar...')
	os.system('python e.py')

menu()
