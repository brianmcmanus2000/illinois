let rec import_list lst = match lst with 
  | [] -> ConstExp(NilConst)
  | ((a, b) :: tail) -> 
    let tail_result = import_list tail in
      let current = BinOpAppExp(CommaOp, ConstExp(IntConst a), ConstExp(IntConst b)) in
        BinOpAppExp(ConsOp, current, tail_result);;
let pair_sums : exp = 
  let fun_var = VarExp("pair_sums") in
  let lst_var = VarExp("lst") in
  let condition_exp = BinOpAppExp(EqOp, lst_var, ConstExp(NilConst)) in
  let x_var = VarExp("x") in
  let let_exp1 = MonOpAppExp(HdOp, lst_var) in
  let in_exp1 = BinOpAppExp(ConsOp, BinOpAppExp(IntPlusOp, MonOpAppExp(FstOp, x_var), MonOpAppExp(SndOp, x_var)), AppExp(fun_var, MonOpAppExp(TlOp, lst_var))) in
  let true_exp = ConstExp(NilConst) in
  let false_exp = LetInExp("x", let_exp1, in_exp1) in
  let if_exp = IfExp(condition_exp, true_exp, false_exp) in
  let in_exp2 = AppExp(fun_var, BinOpAppExp (ConsOp,
      BinOpAppExp (CommaOp, ConstExp (IntConst 7), ConstExp (IntConst 1)),
      BinOpAppExp (ConsOp,
      BinOpAppExp (CommaOp, ConstExp (IntConst 4), ConstExp (IntConst 2)),
      BinOpAppExp (ConsOp,
      BinOpAppExp (CommaOp, ConstExp (IntConst 6), ConstExp (IntConst 3)),
      ConstExp NilConst)))) in
  LetRecInExp("pair_sums", "lst", if_exp, in_exp2);;

let rec count_const_in_exp exp = 
  match exp with ConstExp(exp1) -> 1
  | VarExp(exp1) -> 0
  | MonOpAppExp(op, exp1) -> (count_const_in_exp exp1)
  | BinOpAppExp(op, exp1, exp2) -> (count_const_in_exp exp1) + (count_const_in_exp exp2)
  | IfExp(exp1, exp2, exp3) -> (count_const_in_exp exp1) + (count_const_in_exp exp2) + (count_const_in_exp exp3)
  | AppExp(exp1, exp2) -> (count_const_in_exp exp1) + (count_const_in_exp exp2)
  | FunExp(var, exp1) -> (count_const_in_exp exp1)
  | LetInExp(var, exp1, exp2) -> (count_const_in_exp exp1) + (count_const_in_exp exp2)
  | LetRecInExp(var1, var2, exp1, exp2) -> (count_const_in_exp exp1) + (count_const_in_exp exp2);;

let rec freeVarsInExp exp = 
  match exp with ConstExp(e1) -> []
  | VarExp(e1) -> [e1]
  | MonOpAppExp(op, e1) -> (freeVarsInExp e1)
  | BinOpAppExp(op, e1, e2) -> (freeVarsInExp e1) @ (freeVarsInExp e2)
  | IfExp(e1, e2, e3) -> (freeVarsInExp e1) @ (freeVarsInExp e2) @ (freeVarsInExp e3)
  | AppExp(e1, e2) -> (freeVarsInExp e1) @ (freeVarsInExp e2)
  | FunExp(var, e1) -> List.filter (fun a -> if a = var then false else true) (freeVarsInExp e1)
  | LetInExp(var, e1, e2) ->
    freeVarsInExp(e1) @ (List.filter (fun a -> if a = var then false else true) (freeVarsInExp(e2)))
  | LetRecInExp(var1, var2, e1, e2) -> 
    let result1 = freeVarsInExp(e1) in
      let result2 = freeVarsInExp(e2) in
        let result2_filtered = List.filter (fun a -> if a = var1 then false else true) result2 in
          let result1_filtered = List.filter (fun a -> if a = var1 then false else true) result1 in
            (List.filter (fun a -> if a = var2 then false else true) result1_filtered) @ result2_filtered;;

let rec cps_exp e k = 
  match e with VarExp(exp) -> VarCPS(k, exp)
  | ConstExp(exp) -> ConstCPS(k, exp)
  | IfExp(e1, e2, e3) -> 
      let e2_cps_exp = cps_exp e2 k in
        let e3_cps_exp = cps_exp e3 k in
          let free_list = freeVarsInExpCPS(e2_cps_exp) @ freeVarsInExpCPS(e3_cps_exp) @ freeVarsInContCPS(k) in
            let fresh_var = freshFor(free_list) in  
              cps_exp e1 (FnContCPS (fresh_var, IfCPS(fresh_var, e2_cps_exp, e3_cps_exp)))
  | AppExp(e1, e2) -> 
    let free_list1 = freeVarsInExp(e1) @ freeVarsInContCPS(k) in
      let fresh_var1 = freshFor(free_list1) in 
        let free_list2 = fresh_var1 :: freeVarsInContCPS(k) in 
          let fresh_var2 = freshFor(free_list2) in
            cps_exp e2 (FnContCPS(fresh_var1, cps_exp e1 (FnContCPS(fresh_var2, AppCPS(k, fresh_var2, fresh_var1)))))
  | BinOpAppExp(op, e1, e2) -> 
    let free_list1 = freeVarsInExp(e1) @ freeVarsInContCPS(k) in
      let fresh_var1 = freshFor(free_list1) in
        let free_list2 = fresh_var1 :: freeVarsInContCPS(k) in
          let fresh_var2 = freshFor(free_list2) in
            cps_exp e2 (FnContCPS(fresh_var1, cps_exp e1 (FnContCPS(fresh_var2, BinOpAppCPS(k, op, fresh_var2, fresh_var1)))))
  | MonOpAppExp(op, exp) -> 
    let v = freshFor(freeVarsInContCPS(k)) in 
      cps_exp exp (FnContCPS(v, MonOpAppCPS(k, op, v)))
  | FunExp(x, exp) -> FunCPS(k, x, Kvar, (cps_exp exp (ContVarCPS Kvar)))
  | LetInExp(x, e1, e2) -> 
      let e2_cps_exp = cps_exp e2 k in
            cps_exp e1 (FnContCPS(x, e2_cps_exp))
  | LetRecInExp(f, x, e1, e2) -> FixCPS(FnContCPS(f, cps_exp e2 k), f, x, Kvar, cps_exp e1 (ContVarCPS Kvar));;

