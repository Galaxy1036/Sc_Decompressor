#!/usr/bin/env python3
#Forked on csv_decrypt

import os
import sys
import lzma
import glob

def process_file(path):
    basename = os.path.splitext(path)[0]
    decodedname = basename + ".decompressed.sc"

    print("[+] process:", path, "->", decodedname)

    with open(path, 'rb') as f:
        data = f.read()

    tempdata = bytearray()
    tempdata2 = bytearray()

    try:

        for i in range(26, 35):
            tempdata.append(data[i])

        for i in range(0, 4):
            tempdata.append(0)

        for i in range(35, len(data)):
            tempdata.append(data[i])

        with open(decodedname, 'wb') as f:
            unpack_data = lzma.decompress(tempdata)
            f.write(unpack_data)
        print("[+] Decompressed using latest format")
            
    except:

        for i in range(0,8):
            tempdata2.append(data[i])

        for i in range(0,4):
            tempdata2.append(0)

        for i in range(8,len(data)):
            tempdata2.append(data[i])

        with open(decodedname, 'wb') as f:
            unpack_data2 = lzma.decompress(tempdata2)
            f.write(unpack_data2)
        print("[+] Decompressed using old format")


def process_dir(path):
    for filename in glob.iglob(path + '/**/*.sc', recursive=True):
        if "decompressed.sc" in filename:
            continue
        process_file(filename)

process_dir(sys.argv[1])
