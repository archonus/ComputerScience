#pragma once
#include "list.h"
typedef int (*comparator_t)(void*,void*);
typedef struct heap{
    list* ls;
    comparator_t cmp;

} bin_heap;

