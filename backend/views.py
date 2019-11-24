# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ctypes import *
import numpy as np
import codecs
import datetime

SHM_SIZE = 1024*1024*20  
SHM_KEY = 123559  
OUTFILE="httpd_cdorked_config.bin"   

 
def getTempData(request):
    return HttpResponse("get temperature curve")

def getOriginData(request):
    return HttpResponse("get origin curve")

def getStrainData(request):
    return HttpResponse("get strain curve")

def getParaValue(request): # according to the code got from get request to get value
    code = request.GET.get("code")
    res = {"data": code}
    try:  
        rt = CDLL('librt.so')  
    except:  
        rt = CDLL('librt.so.1')  
    shmget = rt.shmget  
    shmget.argtypes = [c_int, c_size_t, c_int]  
    shmget.restype = c_int  
    shmat = rt.shmat  
    shmat.argtypes = [c_int, POINTER(c_void_p), c_int]  
    shmat.restype = c_void_p  
     
    shmid = shmget(SHM_KEY, SHM_SIZE, 0o666)
    if shmid < 0:  
        print ("System not infected")  
    else:   
        begin_time=datetime.datetime.now()
        addr = shmat(shmid, None, 0)  
        f=open(OUTFILE, 'wb')
        rate=string_at(addr,4)
        len_a=string_at(addr+4,4)  
        len_b=string_at(addr+8,4)
        print(rate,len_a,len_b)
        f.write(string_at(addr+12,SHM_SIZE))
        f.close()  
    #print ("Dumped %d bytes in %s" % (SHM_SIZE, OUTFILE))
    print("Success!",datetime.datetime.now()-begin_time)
    return JsonResponse(res)
