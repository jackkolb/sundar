CC=gcc
CFLAGS=-c
VALGRIND_FLAGS=

ifdef DEBUG
	CFLAGS += -DDEBUG=1
	VALGRIND_FLAGS += -g -O0
endif

OBJECTS_FOLDER=objects
SOURCE_FOLDER=adxl_src

SOURCES=adxl355.c
OBJECTS=$(foreach obj, $(SOURCES:.c=.o), $(OBJECTS_FOLDER)/$(obj))

LIB=rpiadxl355.a

all: $(OBJECTS_FOLDER) $(LIB) control

$(LIB): $(OBJECTS)
	ar rcs $@ $(OBJECTS)

$(OBJECTS_FOLDER)/%.o: $(SOURCE_FOLDER)/%.c
	$(CC) $(CFLAGS) -o $@ $<

control: $(BUILD_FOLDER)
	$(CC) $(VALGRIND_FLAGS) -I$(SOURCE_FOLDER) ./main.c -l:$(LIB) -lwiringPi -L./ -o ./collect.o

$(OBJECTS_FOLDER):
	mkdir $(OBJECTS_FOLDER)

clean_examples:
	rm -rf $(BUILD_FOLDER)

clean:
	rm -rf *.o
	rm -rf $(OBJECTS_FOLDER)
