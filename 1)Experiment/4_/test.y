%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *s);

int posX = 0;
int posY = 0;

%}

%union {
    int num;
}

%token N E S W B

%%
stmt: B direction_list '\n' { printf("Final position is (%d, %d)\n", posX, posY); }
    | B direction_list { printf("Final position is (%d, %d)\n", posX, posY); }
    ;

direction_list: direction { }
              | direction_list direction { }
              ;

direction: N { posY++; printf("Current position is (%d, %d)\n", posX, posY); }
         | E { posX++; printf("Current position is (%d, %d)\n", posX, posY); }
         | S { posY--; printf("Current position is (%d, %d)\n", posX, posY); }
         | W { posX--; printf("Current position is (%d, %d)\n", posX, posY); }
         ;

%%

void yyerror(const char *s) {
    printf("Invalid string\n");
}

int main() {
    printf("Enter the input string: ");
    yyparse();
    return 0;
}
