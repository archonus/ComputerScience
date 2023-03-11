OBJ = obj
BIN = bin
SRC = src

SOURCE_FILES = array.c heapsort.c sorting.c
EXEC_FILES = sorting

OBJECTS = $(addprefix $(OBJ)/, $(SOURCE_FILES:.c=.o))
EXECS = $(addprefix $(BIN)/,$(EXEC_FILES))

build : $(EXECS)

$(EXECS): $(OBJECTS)
	gcc -o $@ $^

$(OBJECTS): $(OBJ)/%.o : $(SRC)/%.c $(SRC)/%.h
	gcc -c $< -o $@


clean:
	rm $(BIN)/*
	rm $(OBJ)/*

hello:
	@echo $(EXEC_FILES)
	@echo $(EXECS)

.PHONY : hello clean build
