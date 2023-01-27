#include "array.h"
#include <stdio.h>
#include <stdlib.h>

int get(intArray* a, int index){
    return a->data[index];
}

void set(intArray* a, int index, int value){
    a->data[index] = value;
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
    int tmp = a->data[i];
    a->data[i] = a->data[j];
    a->data[j] = tmp;
}