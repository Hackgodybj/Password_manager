import hashlib as hb
from random import *
import string
import  pymysql,pbkdf2
import os,binascii,secrets,pyaes
def generate_salt():
    table=string.printable
    password=""
    for i in range(randint(0,20)):
        x=randint(0,94)
        password+=string.printable[x]
    password_encoded=password.encode("utf-8")
    return password_encoded

def sha256_algo(s,a):


    m=hb.sha256()
    m.update(s.encode("utf-8")+a)
    return m.hexdigest()

def initialization_vector():
    iv =secrets.randbits(256)
    return iv
def key_salt():
    salt = os.urandom(32)
    return salt
def take_iv_id_salt(username,list):
    db=pymysql.connect(host=list[0],port=int(list[1]),user=list[2],password=list[3],database="password_database")
    cur=db.cursor()
    cur.execute("select iv,key_salt,id from user where Username=%s",(username))
    db.close()
    return cur.fetchone()
def security_key(password,salt):
    key = pbkdf2.PBKDF2(password,salt, 1500).read(32)
    return key
def encrypt(plaintext,key,iv):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    return binascii.hexlify(ciphertext).decode()
def decrypt(ciphertext,key,iv):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    return decrypted.decode()
def id_required(username,list):
    db = pymysql.connect(host=list[0],port=int(list[1]),user=list[2],password=list[3],database="password_database")
    cur = db.cursor()
    cur.execute("select id from user where Username=%s", (username))
    data=cur.fetchone()
    db.close()
    return data[0]



def random_ID_generator():
    table = string.printable
    password = ""
    for i in range(randint(10, 30)):
        x = randint(0, 94)
        password += string.printable[x]

    return password





