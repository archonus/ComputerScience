#include <stdlib.h>
#include <stdio.h>
#include "array.h"

int main(int argc, char const *argv[])
{
    intArray* arr = init(5);
    int data[10] = {1,2,3,4,5};
    set_array(arr,data);
    printf("%d", get(arr, 0));
    delete(arr);
    
    return 0;
}
