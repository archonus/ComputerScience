#include "array.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool checkIndex(intArray* a,int i){ //Check if index is within bounds
    return (i >= 0 && i < a->length);
}

int get(intArray* a, int index){
    if(checkIndex(a,index)){
        return a->data[index];
    }
    exit(EXIT_FAILURE);
    
}

void set(intArray* a, int index, int value){
    if(checkIndex(a,index)){
        a->data[index] = value;
    }
    else {
        exit(EXIT_FAILURE);
    }
}

int len(intArray* a){
    return a->length;
}

void set_array(intArray* a ,int* data){
    for(int i = 0; i < a->length; i++){
        a->data[i] = data[i];
    }
}

intArray* init(int length){
    intArray* array = malloc(sizeof(*array));
    int* data = malloc(length * sizeof(*data));
    array->data = data;
    array->length = length;
    return array;
}

void delete(intArray* a){
    free(a->data);
    free(a);
    a = NULL;
}

void swap(intArray* a, int i, int j){
    if(checkIndex(a,i) && checkIndex(a,j)){
        int tmp = a->data[i];
        a->data[i] = a->data[j];
        a->data[j] = tmp;
    }
    else{
        exit(EXIT_FAILURE);
    }
}

void printArr(intArray* a){
    for(int i = 0; i < a->length - 1; i++){
        printf("%d, " ,a->data[i]);
    }
    printf("%d\n", a->data[a->length - 1]);
}