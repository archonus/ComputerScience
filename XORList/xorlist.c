#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
typedef struct xlistNode
{
    int value;
    struct xlistNode *xor_pointer;
} Node;

typedef struct xlist
{
    Node *start;
    Node *end;
} XORList;

XORList *createEmptyList()
{
    XORList *ls = malloc(sizeof(XORList));
    ls->start = NULL;
    ls->end = NULL;
    return ls;
}

Node *createNode(int x)
{

    Node *node = malloc(sizeof(Node));
    node->value = x;
    return node;
}

static Node *ptr_xor(Node *a, Node *b)
{
    return (Node *)((uintptr_t)a ^ (uintptr_t)b);
}

void append(XORList *ls, int x)
{
    Node *node = createNode(x);
    if (ls->start == NULL)
    {
        // Was empty, so now a 1 element list, so prev = next = 0 => xor = 0
        node->xor_pointer = NULL;
        ls->start = node;
        ls->end = node;
    }
    else
    {
        Node *prev = ls->end;
        ls->end = node;
        prev->xor_pointer = ptr_xor(prev->xor_pointer, node);
        node->xor_pointer = prev; // next = 0, so xor_pointer = prev
    }
}

int insertAt(XORList *ls, int index, int x)
{
    if (ls->start == NULL)
    { // Empty list
        if (index != 0)
        {
            printf("Index %d is out of bounds\n", index);
            return -1;
        }
        ls->start = createNode(x);
        ls->start->xor_pointer = NULL;
        ls->end = ls->start;
    }
    else if (index == 0)
    { // Insert at start
        Node *node = createNode(x);
        node->xor_pointer = ls->start;
        ls->start->xor_pointer = ptr_xor(node, ls->start->xor_pointer);
        ls->start = node;
    }
    else
    { // Inserting into non-empty list where prev != NULL
        int i = 0;
        Node *prev = NULL;
        Node *current = ls->start;
        Node *next = ls->start->xor_pointer;
        while (current != ls->end && i < index)
        {
            prev = current;
            current = next;
            next = ptr_xor(prev, current->xor_pointer);
            i++;
        }

        if (index > i)
        { // Put at end
            append(ls, x);
        }
        else
        { // Put x where current is
            Node *node = createNode(x);

            Node *prev_prev = ptr_xor(prev->xor_pointer, current);
            prev->xor_pointer = ptr_xor(prev_prev, node);

            current->xor_pointer = ptr_xor(node, next);

            node->xor_pointer = ptr_xor(prev, current);
        }
    }
    return 0;
}

int deleteAt(XORList *ls, int index)
{
    if (ls->start == NULL)
    {
        printf("Deleting from empty list");
        return -1;
    }
    if (index == 0)
    {
        Node *new_head = ls->start->xor_pointer;
        if (new_head != NULL)
        { // Need to change its xor pointer
            new_head->xor_pointer = ptr_xor(ls->start, new_head->xor_pointer);
        }
        ls->start = new_head;
    }
    else
    {
        Node* prev = NULL;
        Node* current = ls->start;
        Node* next = ls->start->xor_pointer;
        int i = 0;
        while(current != ls->end && i < index)
        {
            prev = current;
            current = next;
            next = ptr_xor(prev, current->xor_pointer);
            i++;            
        }
        if(index > i)
        {
            printf("%d is invalid index\n", index);
            return -1;
        }
        Node* prev_prev = ptr_xor(prev->xor_pointer, current);
        prev->xor_pointer = ptr_xor(prev_prev, next);

        if(current == ls->end)
        {
            ls->end = prev;
        }
        else
        { // next exists
            Node* next_next = ptr_xor(next->xor_pointer, current);
            next->xor_pointer = ptr_xor(prev, next_next);
        }
        free(current);
    }
}

void foreach (XORList *ls, void (*f)(int))
{
    if (ls->start == NULL)
        return;
    Node *prev = NULL;
    Node *current = ls->start;
    while (current != ls->end)
    {
        f(current->value);
        Node *next = ptr_xor(prev, current->xor_pointer);
        prev = current;
        current = next;
    }
    f(current->value); // Final function call
}

void map(XORList *ls, int (*f)(int))
{
    if (ls->start == NULL)
        return;
    Node *prev = NULL;
    Node *current = ls->start;
    while (current != ls->end)
    {
        current->value = f(current->value);
        Node *next = ptr_xor(prev, current->xor_pointer);
        prev = current;
        current = next;
    }
    current->value = f(current->value); // Final function call
}

void print_int(int x)
{
    printf("%d\n", x);
}

int add_one(int x) { return x + 1; }

int main(int argc, char const *argv[])
{
    XORList *ls = createEmptyList();
#define N 5
    for (int i = 0; i < N; i++)
    {
        append(ls, i);
    }

    map(ls, add_one);
    insertAt(ls, 0, 0);
    printf("Inserted 0 at start\n");
    foreach (ls, print_int)
        ;

    insertAt(ls, 200, 200);
    printf("Inserted 200 at end\n");
    foreach (ls, print_int)
        ;

    insertAt(ls, 1, 500);
    printf("500 inserted at index 1\n");
    foreach (ls, print_int)
        ;

    insertAt(ls, 4, 300);
    printf("300 inserted at index 4\n");
    foreach (ls, print_int)
        ;

    deleteAt(ls, 4);
    printf("Deleted 300 from index 4\n");
    foreach(ls, print_int);

    deleteAt(ls, 0);
    printf("Deleted 0 at start\n");
    foreach (ls, print_int)
        ;

    return 0;
}
