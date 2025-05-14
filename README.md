# DANK
## Navigation
- [Directory contents](#directory-contents)
- [VSCode syntax highlight extension](#vscode-syntax-highlight-extension)
- [Make](#make)
- [Testing & Debugging](#testing--debugging)
  - [Modes of testing](#modes-of-testing)
  - [Testfile structure](#testfile-structure)
- [DANK Language](#dank-language)
  - [Navigation](#navigation-1)
  - [Comments](#comments)
  - [Repetition](#repetition)
  - [Conditional branching](#conditional-branching)
  - [Reusable code](#reusable-code)
  - [Stopping code execution](#stopping-code-execution)
  - [Variables? in this economy?](#variables-in-this-economy)
  - [Data visualization](#data-visualization)
  - [DA RULEZ](#da-rulez)
    - [Delegate](#delegate)
    - [Logical expression](#logical-expression)
    - [Expression](#expression)
    - [Expression operators](#expression-operators)
    - [Logical Operators](#logical-operators)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Brackets](#brackets)


## Directory contents
+ [antlr](/antlr/) - antlr.jar
+ [dank-shl](/dank-shl/) - VS Code extension
+ [grammar](/grammar/) - Grammar definition
+ [modules](/modules/) - Python files - Lexer, Parser, Visitor
    + [deprecated](/modules/deprecated/) - Python files - Listener (not up to date)
+ [test_files](/test_files/) - .dank files meant for testing
    + [valid.dank](/test_files/valid.dank) - 35 tests, that should give valid outputs
    + [invalid.dank](/test_files/invalid.dank) - 16 tests that should end in error
+ [DANK.py](/DANK.py) - Used for testing/debugging code

## VSCode syntax highlight extension
To enable syntax highlighting for the **DANK** language in Visual Studio Code:

1) Copy the [dank-shl](/dank-shl/) directory into your VS Code extensions folder:
    + Windows - `%USERPROFILE%\.vscode\extensions\`
    + macOS/Linux - `~/.vscode/extensions/`

2) Restart VS Code

If done correctly *.dank files should now use syntax highlighting (check in [test_files](/test_files/))

## Make
Make generates files [DANKLexer.py](/modules/DANKLexer.py) and [DANKParser.py](/modules/DANKParser.py) utilizing files [DANKLexer.g4](/grammar/DANKLexer.g4) and [DANKParser.g4](/grammar/DANKParser.g4).

## Testing & Debugging
There are three modes for testing.

For this help use --help or -h arguments when running the script.

### Modes of testing
1) python .\DANK.py
    + debug/interactive mode - Takes code to be validated as input. Prints parser tree.
2) python .\DANK.py (--test|-t) - Takes and tests all the files in [test_files](/test_files/) directory. Prints tested codes, outputs and number of tests, that did not result in error.
3) python .\DANK.py (--test|-t) filename - Tests the code in the given file. Prints tested codes, outputs and number of tests, that did not result in error.

### Testfile structure
+ Functional code - multiple lines
+ Comment - expected outcome of the functional code
+ Empty line

## DANK Language
### Navigation

  - [Comments](#comments)
  - [Repetition](#repetition)
  - [Conditional branching](#conditional-branching)
  - [Reusable code](#reusable-code)
  - [Stopping code execution](#stopping-code-execution)
  - [Variables? in this economy?](#variables-in-this-economy)
  - [DA RULEZ](#da-rulez)
    - [Delegate](#delegate)
    - [Logical expression](#logical-expression)
    - [Expression](#expression)
    - [Expression operators](#expression-operators)
    - [Logical Operators](#logical-operators)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Brackets](#brackets)

### Comments

**\<comment>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COMMENT  
**\</comment>**

Part of code which will not be executed.

### Repetition
**\<cycle>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODE  
**\</cycle>**

Block of code, which will be continuously executed.

### Conditional branching
**\<branch condition**=*["logical expression"](#logical-expression)***>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODE  
**\</branch>**

Block of code which is only executed if condition is true.

### Reusable code

**\<delegate name**=*"function name"***>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<params>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IDENTIFIERS  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\</params>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODE  
**\</delegate>**

Defines a block of code that can be called to be executed at different parts of code. The **CODE** part may contain variable definition of [ret variable](#variables-in-this-economy). The [ret variable](#variables-in-this-economy) will be transferred outside of the delegate into [function_name variable](#variables-in-this-economy) once finished.

**function_name**([VALUES](#expression))

Delegate call of **function name** in the code.

### Stopping code execution

**\<leave>**

Stops the execution of the future code. Execution resumes after the next matching [**\</cycle>**](#repetition) or [**\</delegate>**](#reusable-code) block.

### Variables? in this economy?

**variable name** = [VALUE](#expression)

Assigning a value to the variable with **variable name**.

### Data visualization

**\<present>**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VALUE](#expression)  
**\</present>**

Function to visualize data in the terminal.

### DA RULEZ

#### Delegate
When calling a delegate the parameters may be:
+ [variable name](#variables-in-this-economy)
+ [expression](#expression) in [brackets](#brackets)
+ [string](#strings)
+ [number](#numbers)

#### Logical expression

May contain:
+ [variable name](#variables-in-this-economy)
+ [expression](#expression) in [brackets](#brackets)
+ [number](#numbers)
+ [logical operator](#logical-operators)

#### expression

May contain: 
+ [variable names](#variables-in-this-economy)
+ expressions in [brackets](#brackets)
+ [strings](#strings)
+ [numbers](#numbers)
+ [expression operators](#expression-operators)

#### Expression operators

+ \+ - numeric addition, string concatenation
+ \- - numeric subtraction, string concatenation with reversed string
+ \* - numeric multiplication
+ / - numeric division


#### Logical Operators

+ \< - less than
+ \> - greater than
+ = - equal
+ <= - less than or equal
+ \>= - greater than or equal
+ ~ - not equal

#### Numbers

Are always float.

#### Strings 

Are always surrounded by pair of \".

#### Brackets

Only \( \) are utilized in DANK Language