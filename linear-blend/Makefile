COMP = g++
FILENAME = linear-blend.cpp
FLAGS = -lpthread -lX11 -std=c++11 -L/usr/X11/lib -I/usr/X11/include
ADD-FLAGS = 
OUTPUT = linear-blend
INCLUDE = -I ../CImg

linear-blend: linear-blend.cpp
	$(COMP) $(FILENAME) $(FLAGS) $(ADD-FLAGS) $(INCLUDE) -o $(OUTPUT)

.PHONY: clean

clean:
	@rm -f $(OUTPUT)
	-@find . -maxdepth 1 -type f -executable -delete
