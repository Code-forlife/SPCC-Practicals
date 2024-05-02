%{
#include "y.tab.h"
%}

%%
n { return N; }
e { return E; }
s { return S; }
w { return W; }
B { return B; }
\n { return '\n'; }
. { return yytext[0]; }
%%

int yywrap(void) {
    return 1;
}
