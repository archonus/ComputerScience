#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#define DEBUG
#include "array.h"

void insertSort(intArray* arr){
    for(int i = 1; i < len(arr); i++){
        for(int j = i; j > 0; j --){
            if(get(arr, j) < get(arr,j-1)){
                swap(arr,j, j-1);
            }
        }
    }

}

void bubbleSort(intArray* arr){
    for(int i = 0; i < len(arr) - 1; i++ ){
        bool swapped = false;
        for(int j = 0; j < len(arr) - i - 1; j ++){
            if(get(arr,j) > get(arr, j+1)){
                swap(arr,j, j+1);
                swapped = true;
            }
        }
        if(!swapped){ //Didn't need to swap on a pass => array sorted
            break;
        }
    }
}


static void merge(intArray* arr, int start, int mid, int end){
    intArray* left = subarray(arr, start, mid);
    intArray* right = subarray(arr, mid, end);
    int i = 0;
    int j = 0;
    while(i < mid - start && j < end - mid){
        int v1 = get(left, i);
        int v2 = get(right, j);
        if(v1 <= v2){
            set(arr, start + i + j, v1);
            i++;
        }
        else{
            set(arr, start + i + j, v2);
            j++;
        }
    }
    while(i < mid - start){
        set(arr, start + i + j, get(left, i));
        i++;
    }
    while (j < end - mid){
        set(arr, start + i + j, get(right, j));
        j++;
    }
    delete(left);
    delete(right);
}

static void mergeSortSubArray(intArray* arr, int start, int end){
    if(end - start < 2){
        return;
    }
    int mid = (end + start) >> 1;
    mergeSortSubArray(arr, start, mid);
    mergeSortSubArray(arr, mid, end);
    merge(arr, start, mid, end);
}

void mergeSort(intArray* arr){
    mergeSortSubArray(arr, 0, len(arr));
}

static int partition(intArray* arr, int begin, int end){
    int pivot = get(arr, end - 1);
    int low = begin;
    int high = end - 1;
    while(low < high){
        while(low < high && get(arr,low) <= pivot){
            low++;
        }
        while(low < high && get(arr,high) >= pivot){
            high --;
        }
        if(low < high){
            swap(arr, low, high);
            low++;
            high--;
        }
    }
    swap(arr,end - 1,high);
    return high;
}

static void quickSortPartition(intArray* arr, int begin, int end){
    if(end - begin < 2){
        return;
    }
    else{
        int p_i = partition(arr, begin, end);
        quickSortPartition(arr, begin, p_i);
        quickSortPartition(arr, p_i, end);
    }
}

void quickSort(intArray* arr){
    quickSortPartition(arr, 0, len(arr));
}


int main(int argc, char const *argv[])
{
    int data[] = {5,1,3,8,9,32,5,7, 2, 22};
    intArray* arr = init((sizeof data) / (sizeof data[0]));
    set_array(arr,data);
    printArr(arr);
    mergeSort(arr);
    printArr(arr);
    delete(arr);
    
    return 0;
}
