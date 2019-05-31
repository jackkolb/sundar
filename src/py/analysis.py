# Generated with SMOP  0.41-beta
from smop.libsmop import *
# analysis.m
import matplotlib as mp
import numpy as np

    #SundarLabProgram
#fft analysis for x,y,z values from accelerometer

def fftDataAnalysis(filename):

    #format long;
    if fid < 0:
        # display an error message and halt execution of the program
        print('File Does Not Exist')
        return
    
    #A = textscan(fid,'%f%f%f%f','Delimiter',':,,\n')

    fd = open(filename,'r')    
    A = np.loadtxt(fd,
            delimiter=':,,\n')
    fd.close()

    A=makeArraySameSize(A)
    A[2]
    
    analysis(A)
    
    avgX=mean(A[2])
    avgY=mean(A[3])
    avgZ=mean(A[4])

    fs=1000
    
    ts=20
# analysis.m:21
    
    num_split=dot(ts,fs)
# analysis.m:22
    
    num_samples=floor(length(A) / num_split)
    for m in range(0,num_samples - 1).reshape(-1):
        A=A(range(dot(m,num_split) + 1,dot(num_split,(m + 1))),range())
# analysis.m:27
        A=fft(A)
# analysis.m:28
    
    #disp(A{2})
    subplot(3,1,1)
    plot(A[2])
    subplot(3,1,2)
    plot(A[3])
    subplot(3,1,3)
    plot(A[4])
    
    fprintf('Average X Reading: %.3f\n',avgX)
    fprintf('Average Y Reading: %.3f\n',avgY)
    fprintf('Average Z Reading: %.3f\n',avgZ)
    
    return Y
    
    
def makeArraySameSize(A):
    maxLength=len(A[1])
    incompleteTest=0

    for i in arange(2,len(A)).reshape(-1):
        lengthTemp=len(A[i])
        if (lengthTemp < maxLength):
            maxLength = lengthTemp
            incompleteTest = 1    
    
    if (incompleteTest == 1):
        for i in range(1, len(A)).reshape(-1):
            if (len(A[i]) != maxLength):
                A[i][maxLength + 1,arange()]=[]
    return A
    
if __name__ == '__main__':
    fftDataAnalysis("testdata.txt")
    