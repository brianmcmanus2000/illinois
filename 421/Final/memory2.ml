VarExp x = let v = lookup_mem m x in (match m with 
|RecVarVal(g,y,e,m')->Closure(y,e,(ins_mem m' g (RecVarVal(g,y,e,m'))))
|_->v)

LetInExp(x,e1,e2) = let v = eval_exp(m,e1) in (match v with
|Exn _ -> v
|_ -> eval_exp(e2,(ins_mem m x v)))

RaiseExp e -> let v = eval_exp(e,m) in (match v with
|Exn _ -> v
|IntVal(n) -> Exn n
)

IfExp(e1,e2,e3) = let v1 = eval_exp(e1,m) in (match v1 with
|Exn _ -> v
|BoolVar true -> eval_exp(e2,m)
|BoolVar false -> eval_exp(e3,m))

