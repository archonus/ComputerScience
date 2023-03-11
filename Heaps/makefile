# bin/main : obj/main.o obj/list.o
# 	gcc -o bin/main obj/main.o obj/list.o

obj/main.o : src/main.c src/list.h
	gcc -c src/main.c -o obj/main.o


obj/list.o : src/list.c src/list.h
	gcc -c src/list.c -o obj/list.o


clean:
	rm bin/*
	rm obj/*

hello:
	@echo $(EXEC_FILES)
	@echo $(EXECS)

.PHONY : hello clean build