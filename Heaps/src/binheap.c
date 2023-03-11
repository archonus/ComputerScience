#include<stdlib.h>
#include<stdbool.h>
#include "binheap.h"

bin_heap* init(comparator_t cmp){
    bin_heap* heap = malloc(sizeof(*heap));
    heap->ls = init_list();
    heap->cmp = cmp;
}

void enqueue(bin_heap* heap, void* v){

}