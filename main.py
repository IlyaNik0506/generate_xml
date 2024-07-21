import argparse
import json
import random

from file_type.acq import acq
from func_gener import date_time

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='Generate XML document.')
# , required=True
parser.add_argument('--count', type=int, default=5, help='Number of documents.')
parser.add_argument('--file', type=int, default=2, help='Number of files.')
parser.add_argument('--doc', type=int, default=1, choices=[1, 2, 3], help='1-ACQ, 2-RESP_ERR, 3-NET_ERR')
# Обрабатываем аргументы командной строки
args = parser.parse_args()
print(args.file)
while args.file > 0:
    procent = 0    
    ls = []
    for _ in range(args.count):
        if args.doc == 1:
            ls.append(acq())
            procent += 1
            print(procent)
            SENDER = 'MK'
            NAME = f'ACQ{args.file}'
    DOC = '\n        '.join(ls)
    # Добавляем начало и конец XML
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <DocFile>
        <FileHeader>
            <FileLabel>DOCUMENT</FileLabel>
            <FormatVersion>2.3.34</FormatVersion>
            <Sender>{SENDER}</Sender> //MK
            <CreationDate>{date_time()}</CreationDate> 
            <CreationTime>{date_time()}</CreationTime> 
            <FileSeqNumber>108</FileSeqNumber>
            <Receiver>VTB24</Receiver>
        </FileHeader>
        <DocList>
            {DOC}
        </DocList>
    </DocFile>
    """

    with open(f'{NAME}.xml', 'w', encoding='utf-8') as file:
        file.write(xml_content)
    
    args.file -= 1