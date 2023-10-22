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
    Node *head;
} XORList;

XORList *createEmptyList()
{
    XORList *ls = malloc(sizeof(XORList));
    ls->head = NULL;
    return ls;
}

bool isEmpty(XORList *ls)
{
    return ls->head == NULL;
}

int main(int argc, char const *argv[])
{
    Node n = {.value = 1, .xor_pointer = NULL};
    printf("Hello\n");
    printf("%d %p\n", n.value, n.xor_pointer);
    return 0;
}
