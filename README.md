# System Programming and Complier Construction 

This repository contains the source code and documentation for ten labs exploring various aspects of compiler design. The labs cover topics from lexical analysis to code generation and linking/loading.

## Experiments

**1. Lexical Analyzer for Programming Languages**

* Implements a lexical analyzer using the lex tool for a specific programming language (e.g., C, Python, Java).
* Identifies and classifies tokens (keywords, identifiers, operators, literals).
* Provides a foundation for further compiler stages.

**2. Optimization of DFA-Based Pattern Matchers**

* Explores techniques for optimizing Deterministic Finite Automata (DFA) used for pattern matching in regular expressions.
* Improves efficiency of the lexical analyzer.

**3. LL(1) and SLR Parser Generation**

* Implements programs to generate parsers for context-free grammars using LL(1) and SLR parsing techniques.
* Verifies the syntax of programs.

**4. SDT Implementation using Lex/Yacc**

* Demonstrates the use of lex and yacc tools to implement a Semantic Directed Translator (SDT) for a specific programming language.
* Performs semantic analysis and code generation during parsing.

**5. Three-Address Code Generation**

* Develops programs to generate three-address code for various programming language constructs (e.g., expressions, statements, control flow).
* Serves as an intermediate representation for optimization and code generation.

**6. Basic Block Identification and Flow Graph Generation**

* Implements algorithms to find basic blocks (sequences of instructions without jumps) in three-address code.
* Constructs a control flow graph to represent program flow.

**7. Code Generation Algorithm**

* Investigates code generation techniques to translate three-address code into machine code for a specific target architecture.
* Optimizes the generated code for efficiency.

**8. Two-Pass Assembler**

* Designs and implements a two-pass assembler that translates assembly language instructions into machine code.
* Resolves symbolic references in the second pass.

**9. Two-Pass Macro Processor**

* Creates a two-pass macro processor that expands macro definitions during assembly.
* Provides modularity and code reuse.

**10. Linker/Loader Design**

* Explores the design principles of a linker/loader.
* Links object files together and loads the combined program into memory for execution.

## Getting Started

1. **Clone the Repository:** Use `git clone https://github.com/Code-forlife/SPCC-Practicals` to clone this repository.
2. **Set Up Environment:** Install any necessary tools (e.g., lex, yacc) based on lab requirements.
3. **Explore Labs:** Each lab folder contains source code, makefiles, and documentation (if available).
4. **Run Labs:** Follow instructions in individual lab folders to compile and execute programs.


## Learning Resources

* [https://www.geeksforgeeks.org/compiler-design-tutorials/](https://www.geeksforgeeks.org/compiler-design-tutorials/)
* [https://www.amazon.com/Compilers-Principles-Techniques-Alfred-Aho/dp/0201100886](https://www.amazon.com/Compilers-Principles-Techniques-Alfred-Aho/dp/0201100886)
* [https://www.amazon.com/lex-yacc-Doug-Brown/dp/1565920007](https://www.amazon.com/lex-yacc-Doug-Brown/dp/1565920007)
