#include <stdlib.h>
#include <stdio.h>
#include "heapsort.h"

static int getLeftChild(int i, int heapSize){
    int l = 2*i + 1;
    if(l < heapSize){
        return l;
    }
    else{
        return -1;
    }
}

static int getRightChild(int i, int heapSize){
    int r = 2*i + 2;
    if(r < heapSize){
        return r;
    }
    else{
        return -1;
    }
}

static int getParent(int i){
    return i >> 1;
}

static void maxHeapOrderSink(intArray* a, int i, int heapSize){
    //Assertion that heapSize <= len(a)
    int l = getLeftChild(i, heapSize);
    int r = getRightChild(i, heapSize);
    int largest = i;
    if(l != -1 && get(a, l) > get(a, i)){
        largest = l;
    }
    if(r != -1 && get(a, r) > get(a, largest)){
        largest = r;
    }
    if(largest != i){
        swap(a, i, largest);
        maxHeapOrderSink(a, largest, heapSize);
    }
}

void heapify(intArray* a){
    int n = len(a);
    int start = ((len(a) + 1) >> 1) - 1;
    for(int i = start; i >= 0; i--){
        maxHeapOrderSink(a, i, n);
    }
    
}

void heapsort(intArray* a){
    heapify(a);
    for(int i = len(a) - 1; i >= 1; i --){
        swap(a, i, 0); //Move the max element to the end
        maxHeapOrderSink(a, 0, i); //Sink the top element to its rightful place
    }
}
