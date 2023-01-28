#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
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

void mergeSort(intArray* arr){
    //To do
}

int main(int argc, char const *argv[])
{
    intArray* arr = init(5);
    int data[10] = {5,1,3,8,9};
    set_array(arr,data);
    printArr(arr);
    printf("%d\n", get(arr,5));
    bubbleSort(arr);
    printArr(arr);
    delete(arr);
    
    return 0;
}
