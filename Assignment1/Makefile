all: src

	cd src && 	zip -r ../bin/lexer.zip *
	echo '#!/usr/bin/env python3.4' | cat - bin/lexer.zip > bin/lexer
	chmod +x bin/lexer

clean:
	rm bin/*
