#pragma once 

typedef struct list_t{
    int n;
    int capacity;
    void** arr; // Array of pointers 
} list;

void *get(list *ls, int i);

void set(list *ls, int i, void *v);

void append(list *ls, void *v);

void *pop(list *ls);

void delete(list* ls);

void free_all(list* ls);

list *init_list();

