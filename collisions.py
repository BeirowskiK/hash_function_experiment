import hashlib
import random
import string
import time
from collections import Counter

def md5(message):
    return hashlib.md5(b""+ bytes(message.encode())).hexdigest()


def sha_256(message):
    return hashlib.sha256(b""+ bytes(message.encode())).hexdigest()


def sha_3(message):
    return hashlib.sha3_256(b""+ bytes(message.encode())).hexdigest()


def sha_1(message):
    return hashlib.sha1(b""+ bytes(message.encode())).hexdigest()


def blake2s(message):
    return hashlib.blake2s(b""+ bytes(message.encode())).hexdigest()


def generateString(length, number):
    output = []
    for i in range(0, number):
        output.append(''.join(random.choices(string.ascii_lowercase, k=length)))
    return output


def checkCollisions(hashArray):
    temp = []
    for hash in hashArray:
        if hash not in temp and hashArray.count(hash) > 1:
            temp.append(hash)

    collisions = len(temp)

    return collisions

def test(stringArray):
    #MD5
    start_time = time.time()
    hashArray = []
    for word in stringArray:
       hashArray.append(md5(word))
    print("MD5 - Time: %.4f  seconds" % (time.time() - start_time), "Collisions: %i" % checkCollisions(hashArray))

    #SHA-256
    start_time = time.time()
    hashArray = []
    for word in stringArray:
        hashArray.append(sha_256(word))
    print("SHA-256 - Time: %.4f  seconds" % (time.time() - start_time), "Collisions: %i" % checkCollisions(hashArray))

    #SHA3-256
    start_time = time.time()
    hashArray = []
    for word in stringArray:
        hashArray.append(sha_3(word))
    print("SHA3-256 - Time: %.4f  seconds" % (time.time() - start_time), "Collisions: %i" % checkCollisions(hashArray))

    #BLAKE2S
    start_time = time.time()
    hashArray = []
    for word in stringArray:
        hashArray.append(blake2s(word))
    print("BLAKE2S - Time: %.4f  seconds" % (time.time() - start_time), "Collisions: %i" % checkCollisions(hashArray))

    #SHA1
    start_time = time.time()
    hashArray = []
    for word in stringArray:
        hashArray.append(sha_1(word))
    print("SHA1 - Time: %.4f  seconds" % (time.time() - start_time), "Collisions: %i" % checkCollisions(hashArray))


def main():
    stringLengths = [1, 10, 100, 1000, 10000]
    for length in stringLengths:
        print('String length: ', length)
        test(generateString(length, 10000))
        print()
main()
