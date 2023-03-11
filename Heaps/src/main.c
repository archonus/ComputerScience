#include <stdio.h>
#include "list.h"

int main(int argc, char const *argv[]){
    list* ls = init_list();
    append(ls, 0);
    append(ls, 0);
    printf("Capacity: %d, n: %d\n",ls->capacity, ls->n);
    delete(ls);
}