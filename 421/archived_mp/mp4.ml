let quadk (a, b, c) k = mulk (4,b) (fun four_b -> mulk(a,a) (fun a_squared -> mulk (2,a_squared) (fun double_a_squared -> addk(double_a_squared,four_b) (fun inner_sum -> addk(inner_sum,c) k))))

let rec list_prod l = match l with
[] -> 1
|x::xs -> let result = (list_prod xs) in x * result

(***** Problem 6b: Recursion & CPS ******)
let rec list_prodk l k = match l with 
[]-> k 1
|x::xs -> list_prodk xs (fun times_element -> mulk (x, times_element) k)

let rec even_count  l   = match l with 
[] -> 0
|x::xs -> let result = even_count xs in if (x mod 2) = 0 then result + 1 else result
let rec even_countk l k =
  match l with [] -> k 0
  | x::xs ->
      even_countk xs (fun recur ->
        modk (x, 2) (fun mod_2 ->
        eqk (mod_2, 0) (fun is_even ->
        if is_even then addk (recur,1) k
        else k recur)));;
let rec sum_all (p,l) = match l with
[] -> 0.0
|x::xs -> let result = sum_all (p,xs) in if p x then result +. x else result

let rec sum_allk (p,l) k = match l with 
[]-> k 0.0
|x::xs -> 
  sum_allk (p, xs) (fun result -> 
    p x (fun passes_check -> 
      if passes_check then float_addk(result,x) k 
      else k result))

let rec list_compose fs = match fs with
[] -> 0
|x::xs -> let result = list_compose xs in x result

let rec list_composek fsk k = match fsk with
[] -> k 0
|f::fs -> list_composek fs (fun result -> (f result) k)