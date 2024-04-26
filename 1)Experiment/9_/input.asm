; Define a macro to increment two values
INCR MACRO X, Y
    MOVER X, Y
MEND

; Define a macro to decrement two values
DECR MACRO X, Y
    MOVEM Y, X
MEND

; Define a macro to print three values
PRN MACRO X, Y, Z
    MOVER X, Y
    MOVEM Y, Z
    PRINT X, Y
    PRINT Z
MEND

START 100
READ N1
INCR N1, N2
DECR N1, N2
READ N2
INCR N1, N2
INCR N3, N4
DECR N3, N4
PRN A1, A2, Z9
STOP
END
