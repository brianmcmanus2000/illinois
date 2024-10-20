let geq (a, b) k = k (a >= b);;
let mulk (a, b) k = k (a * b);;


let greatestabsk (a, b, c) k = 
  mulk (a,a) (fun a_squared -> 
  mulk (b,b) (fun b_squared -> 
  mulk (c,c) (fun c_squared ->
    geq (b_squared,c_squared) (fun b_ge_c ->
      if b_ge_c then
        geq (a_squared,b_squared) (fun a_ge_b ->
          if a_ge_b then k a else k b)
      else
        geq (a_squared,c_squared) (fun a_ge_c ->
          if a_ge_c then k a else k c)))));;



let greatestabsk2 (a, b, c) k = mulk(a,a) (fun a_squared ->
  mulk(b,b) (fun b_squared ->
    mulk(c,c) (fun c_squared ->
      geq(b_squared,c_squared) (fun passes_check1 ->
        if passes_check1 then geq(a_squared,b_squared) (fun passes_check_2 ->
          if passes_check_2 then k a else k b)
        else geq(a_squared,c_squared)(fun passes_check_3 ->
          if passes_check_3 then k a else k c)))));;


let test1 = greatestabsk2 (-2, 2, 1) string_of_int;;
let test2 = greatestabsk (-2, 2, 1) string_of_int;;
print_endline(test1);;
print_endline(test2);;
(*
[0 / 0] greatestabsk (-2, 2, 5) (fun s -> ()) (correct)
[1 / 1] greatestabsk (-3, 2, 1) string_of_int (correct)
[1 / 1] greatestabsk (-1, -10, -3) string_of_int (correct)
[1 / 1] greatestabsk (-1, -2, 5) string_of_int (correct)
[1 / 1] greatestabsk (-2, 4, -9) string_of_int (correct)
[0 / 1] greatestabsk (-2, 2, 1) string_of_int (student solution returns an incorrect value)
[0 / 1] greatestabsk (3, 4, -4) string_of_int (student solution returns an incorrect value)
[0 / 1] greatestabsk (1, -1, -1) string_of_int (student solution returns an incorrect value)
[0 / 1] greatestabsk (1, -2, 2) string_of_int (student solution returns an incorrect value)
[1 / 1] greatestabsk (4, 5, -6) string_of_int (correct)
[1 / 1] greatestabsk (7, 5, -6) string_of_int (correct)
[1 / 1] greatestabsk (-5, -2, 3) string_of_int (correct)
[1 / 1] greatestabsk (-9, 0, -4) string_of_int (correct)
[2 / 2] is_nontrivial_cps_check file "greatestabsk" (correct)
*)