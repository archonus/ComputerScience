#include <stdlib.h>
#include <stdio.h>
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

int main(int argc, char const *argv[])
{
    intArray* arr = init(5);
    int data[10] = {5,1,3,8,9};
    set_array(arr,data);
    insertSort(arr);
    printArr(arr);
    delete(arr);
    
    return 0;
}
