VarExp x-> let v = lookup_mem m x in (match v with ->
Exn_ -> v
RecVarVal(g,y,e,m') -> Closure (y,e,(ins_mem m' g (RecVarVal(g,y,e,m')))))

VarExp x-> let v = lookup_mem mem x in (match v with 
| RecVarVal(g,y,e,m')->Cclosure(ins_mem ml g (RecVarVal(g,y,e,m')))
|_-> v
)

VarExp x -> let v = lookup_mem m x in (match v with 
|RecVarVal(g,y,e,m') -> Cosure(ins_mem m' g (RecVarVal(g,y,e,m')))
|_->v)

VarExp x-> let v = lookup_mem m x in (match v with
|RecVarVal(g,y,e,m')->Closure(ins_mem m' g (RecVarVal(g,y,e,m')))
|_->v)

VarExp x -> let v = lookup_mem m x in (match v with 
|RecVarVal(g,y,e,m')->Closure(ins_mem m' g (RecVarVal(g,y,e,m')))
|_->V)

IfExp (e1,e2,e3) = let v1 = eval_exp(e1,m) in (match v1 with
|Exn _ -> v1
|BoolVar true -> eval_exp(e2,m)
|BoolVar fale -> eval_exp(e3,m))

IfExp(e1,e2,e3) = let v1 = eval_exp(e1,m) in (match v1 with 
|Exn _ -> v
|BoolVar true -> eval_exp(e2,m)
|BoolVar false -> eval_exp(e3,m))

IfExp(e1,e2,e3) = let v1 = eval_exp(e1,m) in (match v1 with)...

VarExp x = let v = lookup_mem m x in (match v with 
|RecVarVal(g,y,e,m')->Closure(ins_mem m' g (RecVarVal(g,y,e,m')))
|_ -> v) 

LetInExp(x,e1,e2)->let v1 = eval_exp(e1,m) (in match v1 with 
|Exn _ -> v1
|_->eval_exp(e2,(ins_mem m x v1)))

LetInExp(x,e1,e2) = let v1 = eval_exp(e1,m) in (match v1 with
|Exn _ -> v1
|_ -> eval_exp(e2, (ins_mem m x v1)))

LetInExp(x,e1,e2) = let v1 = eval_exp(e1,m) in (match v1 with
|Exn _ -> v1
|_ ->eval_exp(e2, (ins_mem m x v1)))

VarExp x = let v = lookup_mem m x in (match v with 
|RecVarVal(g,y,e,m')-> Closure(ins_mem m' g (RecVarVal(g,y,e',n)))
|_ -> v)

RaiseExp e -> let v = eval_exp(e,m) in (match v with
|Exn _ -> v
|IntVal(n) -> Exn n)

RaiseExp e -> let v = eval_exp(e,m) in (match v with
|Exn _ -> v
|IntVal(n) -> Exn n)

RaiseExp e -> let v =  eval_exp(e,m) in (match v with 
|Exn _ -> v
|IntVal(n) -> Exn n)

VarExp x = let v = lookup_mem m x in (match v with
|RecVarVal(g,y,e,m') = Closure(ins_mem m' g (RecVarVal(g,y,e,m')) )
|_ -> v)

LetInExp(x,e1,e2) = let v1 = eval_exp(e1,m) in( match v1 with 
|Exn _ -> V
|_ -> eval_exp(e2, (ins_mem m x v1)))

VarExp x = let v = lookup_mem m x in (match v with
|RecVarVal(g,y,e,m')->Closure(y,e (ins_mem y e (RecVarVal(g,y,e,m'))))
|_ -> v)

VarExp x = let v = lookup_mem m x in (match v with 
|RecVarVal(g,y,e,m')->Closure(y, e, (ins_mem m' g (RecVarVal(g,y,e,m'))))
|_ -> v)


