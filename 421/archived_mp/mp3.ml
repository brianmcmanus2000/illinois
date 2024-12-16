
let rec even_count_fr l = match l with
[] -> 0
| l::ls -> let result = even_count_fr ls in if (l mod 2 = 0) then 1+result else result
let even_count_fr_base = 0;;
let even_count_fr_rec r x = 1-abs(r mod 2) + x

let rec remove_even list = 
  match list with [] -> []
    | (n::rest) -> let r = remove_even rest in if n mod 2 = 0 then r else n :: r
let remove_even_base = [] (* You may need to change this *)
let remove_even_rec n r = match (n mod 2) with
|0 -> r
|_ -> n::r


let rec sift p l = match l with 
|[]   -> ([],[])
|(h::t) -> let (tl,fl) = sift p t in if p h then (h::tl,fl) else (tl,h::fl) 

let rec apply_even_odd l f g = 
  match l with
  [] -> []
  | (first::rest) ->
    match rest with
      [] -> [f first]
      | (second::remaining) -> let result = apply_even_odd remaining f g in (f first)::g(second)::result

let split_sum l f = 
  let rec helper l f t_accumulator f_accumulator = 
    match l with 
    | [] -> (t_accumulator, f_accumulator)
    | (head::tail) -> match f head with
        |true-> helper tail f (t_accumulator + head) f_accumulator
        |false-> helper tail f t_accumulator (f_accumulator + head)
  in (helper l f 0 0);;
let split_sum_start = (0, 0) 

let split_sum_step f r x = let (t_accumulator,f_accumulator) = r in match f x with 
  |true -> (t_accumulator + x, f_accumulator)
  |false -> (t_accumulator, f_accumulator + x)

let rec all_nonneg l = match l with
|[]->true
|head::tail-> (head >= 0) && (all_nonneg tail)
let all_nonneg_start = true;; (* You may need to change this *)
let all_nonneg_step r x = r && (x >= 0)

let rec count_element l m = 
  let rec helper accumulator l m = match l with
    |[] -> accumulator
    |head::tail -> match head = m with
      |true -> helper (accumulator+1) tail m
      |false ->helper accumulator tail m
  in helper 0 l m

let count_element_start = 0
let count_element_step m acc_value x = match x = m with
  |true -> acc_value+1
  |false -> acc_value

let rec max_index l = 
  let rec helper l max_value max_list index = 
    match l with
    |[] -> max_list
    | (head::tail) ->
        if head > max_value then (helper tail head [index] (index + 1))
        else if head = max_value then (helper tail max_value (index::max_list) (index+1))
        else (helper tail max_value max_list (index + 1))
  in match l with
  |[] -> []
  | (head::tail) -> (helper tail head [0] 1);;



  