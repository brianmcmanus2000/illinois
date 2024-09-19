

let p n = print_int(n);print_endline"";n

let d =
  let f = fun _ ->
    let rec g c =
      ( print_int(100); print_endline"";
        if c > 10 then g (c-1)
        else ( fun b -> ( p c ) + ( p b ) ) )
    in g ( p 3 ) ( g ( p 11 )  ( p 6) )
  in f 50;;

print_int(d);;
print_endline"";;
print_endline"";;


let p (s, (n:int)) = print_endline(s);n
let f n =
  (print_endline("a");
   fun m ->
     if (p ("b", n) >= p ("c", 4)) ||
       ((p ("d", n * 3) > 7) &&
           (let k = (p ("e", n) - (p("f",3)))
            in (p ("g", k) <= 5)))
     then p ("h", (n * m))
     else (p ("i", (n + m))))

let d = f 2 3;;
d;;

(*opam exex -- dune init proj hello*)
(*opam exec -- dune build*)
(*opam exec -- dune exec hello*)
