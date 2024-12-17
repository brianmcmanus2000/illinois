/*

In this problem you are asked to complete an ocamlyacc file to implement a parser for the following fragment of PicoML:

  <main> ::= <exp> ;;
      | let IDENT = <exp> ;;
  <exp> ::= IDENT | FLOAT | TRUE | FALSE
      | ( <exp> )
      | <exp> <binop> <exp>
  <binop> ::= *. | /. | ** | = | > | <

The symbols <main>, <exp> and <binop> are non-terminals, while let, IDENT, FLOAT, TRUE, FALSE, and remaining characters and character sequences are terminals. 
The start symbol is <main>. In the file {\skeleton} we have given you the general directives and tokens at the top, followed by the clauses for main, and we 
assume you will fill in the clauses that will define exp. For this problem you are not allowed to the shortcut directives %left and %right. You will lose points 
for shift/reduce and reduce/reduce conflicts in your grammar.

You are required to disambiguate this grammar in accordance with the following associativity and precedence table:

  right **
  left *. left /.
  left = left > left <

Higher in the precedence table means higher precedence, i.e. binds more tightly.

When producing the attributes for each successful production, you will need to use the types for abstract syntax trees for PicoML: const, binop, exp and dec. 
These types are found in common.ml found in the downloaded files. Some of the productions you may have been given may be syntactic sugar for more basic forms.
 */


/* Use the expression datatype defined in expressions.ml: */
%{
    open Common

(* You may want to add extra code here *)

%}

/* Define the tokens of the language: */
%token <int> INT
%token <float> FLOAT
%token <string> STRING IDENT
%token 
%token TRUE FALSE NEG PLUS MINUS TIMES DIV DPLUS DMINUS DTIMES 
       DDIV MOD EXP CARAT LT GT LEQ GEQ EQUALS NEQ PIPE ARROW 
       SEMI DSEMI DCOLON NIL LET REC AND IN IF THEN ELSE FUN 
       MOD RAISE TRY WITH NOT LOGICALAND LOGICALOR LBRAC RBRAC 
       LPAREN RPAREN COMMA UNDERSCORE UNIT HEAD TAIL PRINT FST
       SND EOF

/* Define the "goal" nonterminal of the grammar: */
%start main
%type <Common.dec> main

%%

/* Main Parsing Rules */
main:
    expression DSEMI
        { Anon ($1) }
  | LET IDENT EQUALS expression DSEMI
        { Let ($2, $4) }
  | LET REC IDENT IDENT EQUALS expression DSEMI
        { LetRec ($3, $4, $6) }

/* Expression Parsing with Precedence and Associativity */
expression:
    expr_cmp
        { $1 }

/* Lowest Precedence: =, >, < (Left-Associative) */
expr_cmp:
    expr_cmp EQUALS expr_mul_div
        { BinOpAppExp(EqOp, $1, $3) }
  | expr_cmp GT expr_mul_div
        { BinOpAppExp(GreaterOp, $1, $3) }
  | expr_cmp LT expr_mul_div
        { BinOpAppExp(LessOp, $1, $3) }
  | expr_mul_div
        { $1 }

/* Middle Precedence: *., /. (Left-Associative) */
expr_mul_div:
    expr_mul_div DTIMES expr_exp
        { BinOpAppExp(FloatTimesOp, $1, $3) }
  | expr_mul_div DDIV expr_exp
        { BinOpAppExp(FloatDivOp, $1, $3) }
  | expr_exp
        { $1 }

/* Highest Precedence: ** (Right-Associative) */
expr_exp:
    expr_atom EXP expr_exp
        { BinOpAppExp(ExpoOp, $1, $3) }
  | expr_atom
        { $1 }

/* Atomic Expressions: Identifiers, Floats, Booleans, Parentheses */
expr_atom:
    IDENT
        { VarExp $1 }
  | FLOAT
        { ConstExp (FloatConst $1) }
  | TRUE
        { ConstExp (BoolConst true) }
  | FALSE
        { ConstExp (BoolConst false) }
  | UNIT
        { ConstExp UnitConst }
  | LPAREN expression RPAREN
        { $2 }

%%

(* Additional OCaml code (e.g., helper functions, lexer) goes here *)