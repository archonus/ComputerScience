OBJ = obj
BIN = bin
SRC = src

SOURCE_FILES = array.c heapsort.c sorting.c
EXEC_FILES = sorting

OBJECTS = $(addprefix $(OBJ)/, $(SOURCE_FILES:.c=.o))
EXECS = $(addprefix $(BIN)/,$(EXEC_FILES))



bin/sorting : $(OBJECTS)
	gcc -o bin/sorting $(OBJECTS)

sorting.o : sorting.c array.h
	gcc -c sorting.c

array.o : array.c array.h
	gcc -c array.c

heapsort.o : heapsort.c heapsort.h
	gcc -c heapsort.c


.PHONY : hello clean

clean:
	rm sorting.out $(OBJECTS)

hello:
	@echo $(EXEC_FILES)
	@echo $(EXECS)
