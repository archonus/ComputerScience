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

static Node* ptr_xor(Node* a, Node * b){
    return (Node*) ((uintptr_t) a ^ (uintptr_t) b);
}

bool isEmpty(XORList *ls)
{
    return ls->start == NULL;
}

void insert(XORList *ls, int x)
{
    Node *node = malloc(sizeof(Node));
    node->value = x;
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

void foreach (XORList * ls, void (*f)(int))
{
    Node *next = ls->start;
    if (ls->start == NULL)
        return;
    f(ls->start->value);
    next = ptr_xor(next, next->xor_pointer);
    while (next != ls->end)
    {
        f(next->value);
        next = ptr_xor(next, next->xor_pointer);
    }
}

void map(XORList *ls, int (*f)(int))
{
    // TODO
}

void print_int(int x){
    printf("%d\n",x);
}

int main(int argc, char const *argv[])
{
    XORList* ls = createEmptyList();
    insert(ls, 1);
    printf("Inserted 1\n");
    insert(ls, 2);
    printf("Inserted 2\n");
    insert(ls,3);
    printf("Inserted 3\n");
    foreach(ls, print_int);
    printf("Hello\n");
    return 0;
}
