let rec subst_fun sigma ty = 
  match sigma with [] -> TyVar(ty)
  | ((a, b)::tl) -> 
    if a = ty then b
    else subst_fun tl ty

let rec monoTy_lift_subst sigma ty = 
  match ty with TyVar(m) -> subst_fun sigma m
  | TyConst(s, args) ->
    let rec helper l =
      match l with [] -> []
      | (hd::tl) -> monoTy_lift_subst sigma hd :: helper tl
    in TyConst(s, helper args)

let rec occurs v ty = 
  match ty with TyVar(x) ->
    if x = v then true
    else false
  | TyConst(s, args) ->
    let rec helper l =
      match l with [] -> false
      | (hd :: tl) -> 
        if occurs v hd then true
        else helper tl
    in helper args

let rec contains n ty =
  match ty with
  |  TyVar m -> n=m
  | TyConst(st, typelst) -> List.fold_left (fun xl x -> if xl then xl else contains n x) false typelst;;

let rec substitute ie ty = 
  let n,sub = ie in match ty with
    | TyVar m -> if n=m then sub else ty
    | TyConst(st, typelist) -> TyConst(st, List.map (fun t -> substitute ie t) typelist);;

let rec unify eqlst : substitution option =
  let rec addNewEqs lst1 lst2 acc =
    match lst1,lst2 with
    | [],[] -> Some acc
    | t::tl, t'::tl' -> addNewEqs tl tl' ((t,t')::acc)
    | _ -> None
  in
  match eqlst with
  |  [] -> Some([])
    (* Delete *)
  | (s,t)::eqs when s=t -> unify eqs
    (* Eliminate *)
  | (TyVar(n),t)::eqs when not(contains n t)-> 
      let eqs' = List.map (fun (t1,t2) -> (substitute (n,t) t1 , substitute (n,t) t2)) eqs
      in (match unify eqs' with
           None -> None
         | Some(phi) -> Some((n, monoTy_lift_subst phi t):: phi))
    (* Orient *)
  | (TyConst(str, tl), TyVar(m))::eqs -> unify ((TyVar(m), TyConst(str, tl))::eqs)
    (* Decompose *)
  | (TyConst(str, tl), TyConst(str', tl'))::eqs when str=str' -> 
      (match (addNewEqs tl tl' eqs) with
        None -> None
      | Some l -> unify l)
    (* Other *)
  | _ -> None
;;