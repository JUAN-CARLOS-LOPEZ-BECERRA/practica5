import cv2
import numpy as np

def threshold(img):
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshold',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg',)
cv2.imshow('original',img)
x=cv2.waitKey(0)

def thresholdinv(img):
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('threshold_inv',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
x=cv2.waitKey(0)

def ToZero(img):
    retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    cv2.imshow('ToZero',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
x=cv2.waitKey(0)

def ToZeroinv(img):
    retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('ToZeroinv',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
x=cv2.waitKey(0)

def TRUNC(img):
    
    retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    cv2.imshow('TRUNC',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
x=cv2.waitKey(0)

def otsu(img):
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('otsu',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
x=cv2.waitKey(0)

def gaus(img):
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('gaus',th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Mean(img):
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imshow('mean',th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



img = cv2.imread('bookpage.jpg')

threshold(img)
thresholdinv(img)
TRUNC(img)
ToZero(img)
ToZeroinv(img)
otsu(img)
gaus(img)
Mean(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
    


