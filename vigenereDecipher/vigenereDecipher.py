# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:00:01 2016

@author: w
"""
from functools import reduce
from itertools import cycle
string="wubefiqlzurmvofehmymwtixcgtmpifkrzupmvoirqmmwozmpulmbnyvqqqmvmvjleimhfefnzpsdlppsdlpevqmwcxymdavqeefiqcaytqowcxymwmsemefcfwyeyqetrliqycgmtwcwfbsmyfplrxtqyeexmruluksgwfptlrqaerlqvpmvyqycxtwfqlmtelsfjpqehmozciwciwfpzslmaeziqvlqmzvppxawcsmzmorvgwwqszetrlqzpbjazvqiyxewwoiccgdwhqmmvowsgntjpfppaibiybjutwelqklllmdpyvacdcfqnzpifppksdvptidgxmqqvebmqalkezmgcvkuzkizbzliuammvz"
gramLength=4

locations = [];
distances = [];
def longitudLlave(string,gramLength):	
    #locate all grams
    for i in range(len(string)):
        gram = string[i:i+gramLength];	
        # make sure we don't get stuck with shorties
        if len(gram) < gramLength: break
        locations.append([]);
    
        find = string.find(gram,0);
        while find != -1:
            locations[i].append(find);
            find = string.find(gram,find+1);
        	
        	# only calculate the distances if need be
        if len(locations[i]) > 1:
             for j in range(1,len(locations[i])):
                 distances.append(locations[i][j] - locations[i][0])     
    miMcd = McdArray(distances);
    return miMcd
print(distances)


def mcd(a,b):
	while b != 0:
		t = b;
		b = a % b;
		a = t;
	return a


def McdArray(mcdz):

	""" Takes the greatest common divisor of an entire array """

	if len(mcdz) < 2: return mcdz[0];
	
	miMcd = mcd(mcdz[0],mcdz[1]);	

	for i in range(2,len(mcdz)):
		miMcd = mcd(mcdz[i],miMcd);

	return miMcd;
 
def separarString(cipherText,longitudLlave):
        freqList=[]
        
        for i in range(longitudLlave):freqList.append('');

        for i in range(len(cipherText)):
            index=i%longitudLlave
            freqList[index]+=cipherText[i]
            
        return freqList


def calcFreq(freqList):
     cNums = map(chr, range(97, 123))
     prob = []
     f = range(len(cNums))
     p = [.082,.015,.028,.043,.127,.022,.020,.061,.070,.002,.008,.040,.024,.067,.075,.019,.001,.060,.063,.091,.028,.010,.023,.001,.020,.001];

     for i in range(len(cNums)):
         f[i] = freqList.count(cNums[i])
         prob.append(0)

     print f
	
     for g in range(len(cNums)):
         print g
         for i in range(len(cNums)):
             print i
             fig = f[(i+g)% len(f)]
             prob[g] += ((p[i]*fig) / float(len(freqList)))
             print "pos",(i+g)% len(f)
             print "prob",prob
             
             #print(p[i])
     return prob;


def sugKey(prob):
	
	""" Suggestes a key, given the maximum likelihood """

	#contend = [];
	cNums = map(chr, range(97, 123));

	i = max(prob);
      
	return cNums[prob.index(i)];


def criptoAnalisis(string,n):
	
	# construct y[i]
	y = separarString(string,n);
	#if verbose:
	#	for i in range(n): print 'y(%i): %s' % (i,y[i]);

	prob = [];
	# calculate Mg
	for i in range(n): 
         m = calcFreq(y[i]);
         prob.append(m);
         print prob
		#if verbose: print "M_g(y[i])=",m;		

	# suggest the key
	key = "";
	for i in range(n):
		key += sugKey(prob[i]);

	return key;

def decrypt(ciphermessage, key):
    pairs = zip(ciphermessage, cycle(key))
    cNums = map(chr, range(97, 123));
    result = ''

    for i in pairs:
        total = reduce(lambda x, y: cNums.index(x) - cNums.index(y), i)
        result += cNums[total % 26]

    return result
        
        
    
v=longitudLlave(string,gramLength)
x=separarString(string,v)
a=criptoAnalisis(string,v)
print "llave:",a
dec=decrypt(string,a)
print dec
