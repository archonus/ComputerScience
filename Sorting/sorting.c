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

static intArray* merge(intArray* a1, intArray* a2){
    int n = len(a1) + len(a2);
    intArray* arr = init(n);
    int i =0;
    int j = 0;
    int n1 = len(a1);
    int n2 = len(a2);
    while(i < n1 && j < n2){
        int v1 = get(a1, i);
        int v2 = get(a2, j);
        if(v1 <= v2){
            set(arr, i + j, v1);
            i++;
        }
        else{
            set(arr, i + j, v2);
            j++;
        }
    }
    while(i < n1){
        set(arr, i + j, get(a1,i));
        i++;
    }
    while(j < n2){
        set(arr, i + j, get(a2, j));
        j ++;
    }
    return arr;
}
intArray* mergeSort(intArray* arr){
    int n = len(arr);
    if(n == 1){
        return arr;
    }

    int split = n >> 1;
    intArray* left = mergeSort(subarray(arr, 0, split));
    intArray* right = mergeSort(subarray(arr,split, n));
    return merge(left, right);
    
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
    intArray* arr = init(8);
    int data[10] = {5,1,3,8,9,32,5,7};
    set_array(arr,data);
    printArr(arr);
    intArray* sorted_arr = mergeSort(arr);
    printArr(arr);
    printArr(sorted_arr);
    delete(arr);

    printf("%d",3 >> 1);
    
    return 0;
}
