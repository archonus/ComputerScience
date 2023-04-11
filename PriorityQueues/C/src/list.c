#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "list.h"
#define INITIAL_CAPACITY 5

bool checkIndex(list *ls, int i)
{
    if (i < 0)
    {
        return false;
    }
    else if (i >= ls->n)
    {
        return false;
    }
    return true;
}

void *get(list *ls, int i)
{ // Returns a void pointer
    if (checkIndex(ls, i))
    {
        return ls->arr[i];
    }
    else
    {
        printf("Index error %d\n", i);
        exit(EXIT_FAILURE);
    }
}

void set(list *ls, int i, void *v)
{
    if (checkIndex(ls, i))
    {
        ls->arr[i] = v;
    }
    else
    {
        printf("Index error %d\n", i);
        exit(EXIT_FAILURE);
    }
}

static void resize(list *ls, int new_capacity)
{
    if (new_capacity <= ls->n)
    { // Can't shrink to less than necessary space
        new_capacity = ls->n + 1; // If both n and capacity are zero, will still increase size
    }
    void **new_arr = realloc(ls->arr, new_capacity * sizeof(void *));
    if (new_arr)
    { // realloc successful
        ls->arr = new_arr;
        ls->capacity = new_capacity;
    }
    else
    { // realloc failed
        printf("Could not resize array");
        exit(EXIT_FAILURE);
    }
}

void append(list *ls, void *v)
{
    if (ls->n == ls->capacity)
    { // Full
        resize(ls, 2 * ls->capacity);
    }
    ls->n++; // Increment num items
    set(ls, ls->n - 1, v);
}

void *pop(list *ls)
{ // Return last element and reduce n
    return get(ls, --ls->n);
}

void delete(list *ls)
{
    free(ls->arr);
    free(ls);
    ls = NULL;
}

void free_all(list *ls)
{
    for (int i = 0; i < ls->n; i++)
    {
        free(ls->arr[i]);
    }
    delete (ls);
}

list *init_list()
{
    list *ls = malloc(sizeof(*ls));
    void **arr = malloc(INITIAL_CAPACITY * sizeof(void *));
    if (ls == NULL || arr == NULL)
    {
        printf("Could not initialise");
        exit(EXIT_FAILURE);
    }
    else
    {
        ls->arr = arr;
        ls->capacity = INITIAL_CAPACITY;
        ls->n = 0;
        return ls;
    }
}
