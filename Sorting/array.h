typedef struct int_array {
    int length;
    int* data;
} intArray;

int get(intArray* a, int index);

void set(intArray* a, int index, int value);

int len(intArray* a);

void set_array(intArray* a ,int* data);

intArray* init(int length);

void delete(intArray* a);

void swap(intArray* a, int i, int j);

void printArr(intArray* a);