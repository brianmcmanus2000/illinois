let rec list_up_to_n n =
  if n < 2 then []
  else (list_up_to_n (n - 1)) @ [n]
;;

let rec list_multiples n current max =
  if current <= max then current :: (list_multiples n (current + n) max)
  else []
;;

let rec get_all_multiples lst max = match lst with
| [] -> []
| head :: tail -> (list_multiples head (head * 2) max) @ (get_all_multiples tail max)
;;

let rec print_list = function
| [] -> ()
| e :: l -> print_int e; print_string " "; print_list l;;

let get_primes n =
  let limit = int_of_float (sqrt (float_of_int n)) in
  let candidates = get_all_multiples (list_up_to_n limit) n in
  List.filter (fun x -> not (List.mem x candidates)) (list_up_to_n n)
;;




print_endline("Numbers up to 10");;
print_list (list_up_to_n 10);;
print_endline("");;
print_endline("multiples of 2 up to 12");;
print_list(list_multiples 2 2 12);;
print_endline("");;
print_endline("potential factors for 81");;
let max = int_of_float(sqrt(81.));;
print_list (get_all_multiples (list_up_to_n max) max);;
print_endline("");;
print_endline("Primes less than 100");;
print_list (get_primes 100);;
print_endline("");;


let largest list = match list with []->None | list -> let rec helper list max = match list with 
  |[]->Some max
  |head::tail-> if head>max then helper tail head else helper tail max 
in helper list 0 
;;

let print_option n = match n with 
None->print_endline("none")
|Some n -> print_int(n);print_endline("") 
;;
print_endline("largest element is");;
print_option (largest [])