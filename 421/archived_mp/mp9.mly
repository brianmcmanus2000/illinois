/* Use the expression datatype defined in expressions.ml: */
%{
  open Common

(* You may want to add extra code here *)

%}


/* Define the tokens of the language: */
%token <int> INT
%token <float> FLOAT
%token <string> STRING IDENT
%token TRUE FALSE NEG PLUS MINUS TIMES DIV DPLUS DMINUS DTIMES DDIV EXP CARAT
       LT GT LEQ GEQ EQUALS NEQ PIPE ARROW SEMI DSEMI DCOLON NIL
       LET REC AND IN IF THEN ELSE FUN MOD RAISE TRY WITH NOT LOGICALAND
       LOGICALOR LBRAC RBRAC LPAREN RPAREN COMMA UNDERSCORE UNIT
       HEAD TAIL PRINT FST SND EOF

/* Define the "goal" nonterminal of the grammar: */
%start main expression
%type <Common.dec> main
%type <Common.exp> expression

%%

main:
    expression DSEMI      			   { (Anon ( $1)) }
  | LET IDENT EQUALS expression	DSEMI 	           { (Let ($2,$4)) }
  | LET REC IDENT IDENT EQUALS expression DSEMI    { (LetRec ($3, $4, $6)) }

expression:
  | LET IDENT EQUALS expression IN expression { LetInExp($2, $4, $6) }
  | LET REC IDENT IDENT EQUALS expression IN expression { LetRecInExp($3, $4, $6, $8) }  
  | fn_exp                                             { $1 }
  | neg_expression {$1}
  | TRY expression WITH handler_list
        { 
          match $4 with
          | None -> TryWithExp($2, None, ConstExp(UnitConst), $4) 
          | Some (tag, exp) -> TryWithExp($2, tag, exp, $4)      
        }
;

handler_list:
    handler                                { [$1] }
  | handler PIPE handler_list              { $1 :: $3 }
;

handler:
    exception_tag ARROW expression         { ($1, $3) }
;


exception_tag:
    INT                                    { Some $1 }
  | UNDERSCORE                             { None }
;

neg_expression:
  | MINUS monop_exp                                         { MonOpAppExp(IntNegOp, $2)}   
  | DMINUS monop_exp                                       { MonOpAppExp(FloatNegOp, $2) } 
  
fn_exp:
    FUN IDENT ARROW expression                       { FunExp($2, $4) }
  | raise_exp                                       { $1 }

raise_exp:
  | RAISE rest_op                                { RaiseExp($2) }
  | if_exp                                          { $1 }

if_exp:
    IF expression THEN expression ELSE expression   { IfExp($2, $4, $6) }
  | or_else_exp                                     { $1 }

or_else_exp:
    or_else_exp LOGICALOR and_also_exp                 { IfExp($1, ConstExp(BoolConst(true)), $3) }
  | and_also_exp                                    { $1 }

and_also_exp:
    and_also_exp LOGICALAND rel_op_exp             { IfExp($1, $3, ConstExp(BoolConst(false))) }
  | rel_op_exp                                  { $1 }

rel_op_exp:
    rel_op_exp rel_op cons_exp                  { $2 $1 $3 }
  | cons_exp                                    { $1 }

cons_exp:
    lo_bin_op_exp DCOLON cons_exp               { BinOpAppExp(ConsOp, $1, $3) }
  | lo_bin_op_exp                               { $1 }      

lo_bin_op_exp:
    lo_bin_op_exp lo_bin_op hi_bin_op_exp       { $2 $1 $3 }
  | hi_bin_op_exp                               { $1 }

hi_bin_op_exp:
    hi_bin_op_exp hi_bin_op monop_exp             { $2 $1 $3 }
  | monop_exp                                     { $1 }

hi_bin_op:
    TIMES                                      { fun x y -> BinOpAppExp(IntTimesOp, x, y) }
  | DIV                                        { fun x y -> BinOpAppExp(IntDivOp, x, y) }
  | DTIMES                                     { fun x y -> BinOpAppExp(FloatTimesOp, x, y) }
  | DDIV                                       { fun x y -> BinOpAppExp(FloatDivOp, x, y) } 
  | MOD                                        { fun x y -> BinOpAppExp(ModOp, x, y) } 
lo_bin_op:
    PLUS                                       { fun x y -> BinOpAppExp(IntPlusOp, x, y) }
  | MINUS                                      { fun x y -> BinOpAppExp(IntMinusOp, x, y) }
  | DPLUS                                      { fun x y -> BinOpAppExp(FloatPlusOp, x, y) }
  | DMINUS                                     { fun x y -> BinOpAppExp(FloatMinusOp, x, y) }
  | CARAT                                      { fun x y -> BinOpAppExp(ConcatOp, x, y) }
  | EXP                                      { fun x y -> BinOpAppExp(ExpoOp, x, y) }
rel_op:
    EQUALS                                      { fun x y -> BinOpAppExp(EqOp, x, y) }
  | LT                                          { fun x y -> BinOpAppExp(GreaterOp, y, x) }
  | GT                                          { fun x y -> BinOpAppExp(GreaterOp, x, y) }
  | LEQ                                         { fun x y -> IfExp(BinOpAppExp(GreaterOp, y, x), ConstExp(BoolConst(true)), BinOpAppExp(EqOp, x, y)) }
  | GEQ                                         { fun x y -> IfExp(BinOpAppExp(GreaterOp, x, y), ConstExp(BoolConst(true)), BinOpAppExp(EqOp, x, y)) }
  | NEQ                                         { fun x y -> IfExp(BinOpAppExp(EqOp, x, y), ConstExp(BoolConst(false)), ConstExp(BoolConst(true))) }

monop_exp:
  | mon_op                                      { FunExp("x",MonOpAppExp($1, VarExp("x"))) }
  | mon_op monop_exp                            { MonOpAppExp($1, $2) }
  | app_exp                                     { $1 }


app_exp:
    app_exp rest_op                              { AppExp($1, $2) }
  | rest_op {$1}

rest_op:
    LPAREN paren_exp RPAREN                     { $2 }
  | LBRAC list_exp RBRAC                        { $2 }
  | constant_exp                                { $1 }
  | IDENT                                       { VarExp($1) }

list_exp:
    expression                                     { BinOpAppExp(ConsOp, $1, ConstExp(NilConst)) }
  | expression COMMA list_exp                      { BinOpAppExp(ConsOp, $1, $3) }
  | expression SEMI list_exp                       { BinOpAppExp(ConsOp, $1, $3) }

paren_exp:
    expression                                     { $1 }
 |  expression COMMA paren_exp                     { BinOpAppExp(CommaOp, $1, $3) }

mon_op:
  | HEAD                                          { HdOp }
  | TAIL                                          { TlOp }
  | FST                                         { FstOp }
  | SND                                         { SndOp }
  | PRINT                                       { PrintOp }

constant_exp:
    INT                                         { ConstExp(IntConst($1)) }
  | FLOAT                                        { ConstExp(FloatConst($1)) }
  | TRUE                                        { ConstExp(BoolConst(true)) }
  | FALSE                                        { ConstExp(BoolConst(false)) }
  | STRING                                      { ConstExp(StringConst($1)) }
  | UNIT                                        { ConstExp(UnitConst) }
  | NIL                                         { ConstExp(NilConst) }
  | LBRAC RBRAC                                 { ConstExp(NilConst) }