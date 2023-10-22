#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
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

bool isEmpty(XORList *ls)
{
    return ls->start == NULL;
}

void insert(int x, XORList *ls)
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
        Node* prev = ls->end;
        ls->end = node;
        prev->xor_pointer = (int)prev->xor_pointer ^ (int)node;
        node->xor_pointer = prev; // next = 0, so xor_pointer = prev
    }
}

void map(int (*f)(int), XORList* ls){
    // TODO
}

int main(int argc, char const *argv[])
{
    Node n = {.value = 1, .xor_pointer = NULL};
    printf("Hello\n");
    printf("%d %p\n", n.value, n.xor_pointer);
    return 0;
}
