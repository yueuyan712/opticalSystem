#  used for dealing with data frame
# -*- coding: UTF-8 -*-
class wr():
    read = 0
    write = 1

def packageReadFrame(board, codeArr): # code:str array
    readWrite = padZero(1, str(wr.read))
    board = padZero(1, str(bin(int(board,16))[2:]))
    codelen = padZero(1, str(len(codeArr)))
    codeTotal = ''
    for item in codeArr:
        codeTotal += padZero(2, str(bin(int(item,16))[2:]))
    result = board + codelen + codeTotal
    return result

def padZero(target, text):
    strLen = len(text)
    zeroLen = target*8 - strLen
    result = text
    count = 0
    while (count < zeroLen):
        result = '0' + result
        count = count + 1
    return result
    