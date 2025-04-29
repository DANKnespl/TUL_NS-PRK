ANTLR_JAR=./antlr/antlr-4.13.2-complete.jar
GRAMMAR_DIR=./grammar
MODULE_DIR=./modules

GRAMMARS=$(GRAMMAR_DIR)/DANKLexer.g4 $(GRAMMAR_DIR)/DANKParser.g4

all: generate clean move

generate:
	@which java || echo "Java not found in PATH"
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor $(GRAMMARS)

clean:
	rm -f $(GRAMMAR_DIR)/*.interp $(GRAMMAR_DIR)/*.tokens
	rm -f $(GRAMMAR_DIR)/*Listener.py $(GRAMMAR_DIR)/*Visitor.py

move:
	mkdir -p $(MODULE_DIR)
	mv $(GRAMMAR_DIR)/*.py $(MODULE_DIR)
