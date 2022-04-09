

install:
	make clean
	pyinstaller ./main/dotman.py

clean :
	rm -rf build
	rm -rf dist
	rm -rf ~/.config/dotman/
