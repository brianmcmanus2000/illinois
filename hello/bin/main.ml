let x = 12;;
let plus_x y = y + x;;
let () = print_newline (print_int (plus_x 3));;

(*opam exex -- dune init proj hello*)
(*opam exec -- dune build*)
(*opam exec -- dune exec hello*)