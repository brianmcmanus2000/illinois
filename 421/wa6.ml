Unify {('b = F(N,S)), (P('a,'c) = P('c,'b))}


= Unify {(P('a,'c) = P('c,F(N,S)))} o {'b -> F(N,S)} by Eliminate on ('b = F(N,S))
= Unify { ('a = 'c) , ('c = F(N,S)) } o {'b -> F(N,S)} by Decompose on (P('a,'c) = P('c,F(N,S)))
= Unify { ('c = F(N,S)) } o {'a -> 'c} o {'b -> F(N,S)} by Eliminate on ('a = 'c)
= Unify {} o {'c -> F(N,S)} o {'a -> 'c} o {'b -> F(N,S)} by Eliminate on ('c = F(N,S))
= {'c -> F(N,S), 'a -> F(N,S), 'b -> F(N,S)} 


Unify {(F('a,F(G('b,'c,H('d)),'e)) = F(G('c,'b,'c),F('a,'d))), (H(G('d,F('a,'e),'f)) = H(G('e,'f,F(G('c,H('e),H('d)),'e))))}


= Unify{ ('a = G('c,'b,'c)), (F(G('b,'c,H('d)),'e) = F('a,'d)), (H(G('d,F('a,'e),'f)) = H(G('e,'f,F(G('c,H('e),H('d)),'e))))} by Decompose on (F('a,F(G('b,'c,H('d)),'e)) = F(G('c,'b,'c),F('a,'d)))

= Unify{ ('a = G('c,'b,'c)), (F(G('b,'c,H('d)),'e) = F('a,'d)), (G('d,F('a,'e),'f) = G('e,'f,F(G('c,H('e),H('d)),'e)))} by Decompose on (H(G('d,F('a,'e),'f)) = H(G('e,'f,F(G('c,H('e),H('d)),'e))))

= Unify{ ('a = G('c,'b,'c)), (F(G('b,'c,H('d)),'e) = F('a,'d)), ('d = 'e), (F('a,'e) = 'f), ('f = F(G('c,H('e),H('d)),'e))} by Decompose on (G('d,F('a,'e),'f) = G('e,'f,F(G('c,H('e),H('d)),'e)))

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('d)) = 'a), ('e = 'd) , ('d = 'e), (F('a,'e) = 'f), ('f = F(G('c,H('e),H('d)),'e))} by Decompose on (F(G('b,'c,H('d)),'e) = F('a,'d))

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), ('e = 'e) , (F('a,'e) = 'f), ('f = F(G('c,H('e),H('e)),'e))} o {'d -> 'e} by Eliminate on ('d = 'e)

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), (F('a,'e) = 'f), ('f = F(G('c,H('e),H('e)),'e))} o {'d -> 'e} by Delete on ('e = 'e)

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), ('f = F('a,'e)), ('f = F(G('c,H('e),H('e)),'e))} o {'d -> 'e} by Orient on (F('a,'e) = 'f)

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), (F('a,'e) = F(G('c,H('e),H('e)),'e))} o {'d -> 'e} o {'f -> F('a,'e)} by Eliminate on ('f = F('a,'e))

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), ('a = G('c,H('e),H('e))), ('e = 'e)} o {'d -> 'e} o {'f -> F('a,'e)} by Decompose on (F('a,'e) = F(G('c,H('e),H('e)),'e))

= Unify{ ('a = G('c,'b,'c)), (G('b,'c,H('e)) = 'a), ('a = G('c,H('e),H('e)))} o {'d -> 'e} o {'f -> F('a,'e)} by Delete on ('e = 'e)

= Unify{(G('b,'c,H('e)) = G('c,'b,'c)), (G('c,'b,'c) = G('c,H('e),H('e)))} o {'d -> 'e} o {'f -> F(G('c,'b,'c),'e)} o {'a -> G('c,'b,'c)} by Eliminate on  ('a = G('c,'b,'c))

= Unify{('b = 'c), ('c = 'b), (H('e) = 'c), (G('c,'b,'c) = G('c,H('e),H('e)))} o {'d -> 'e} o {'f -> F(G('c,'b,'c),'e)} o {'a -> G('c,'b,'c)} by Decompose on (G('b,'c,H('e)) = G('c,'b,'c))

= Unify{('c = 'c), (H('e) = 'c), (G('c,'c,'c) = G('c,H('e),H('e)))} o {'d -> 'e} o {'f -> F(G('c,'c,'c),'e)} o {'a -> G('c,'c,'c)} o {'b->'c} by Eliminate on ('b = 'c)

= Unify{(H('e) = 'c), (G('c,'c,'c) = G('c,H('e),H('e)))} o {'d -> 'e} o {'f -> F(G('c,'c,'c),'e)} o {'a -> G('c,'c,'c)} o {'b->'c} by Delete on ('c='c)

= Unify{(H('e) = 'c), ('c = 'c), ('c = H('e)), ('c = H('e))} o {'d -> 'e} o {'f -> F(G('c,'c,'c),'e)} o {'a -> G('c,'c,'c)} o {'b->'c} by Decompose on (G('c,'c,'c) = G('c,H('e),H('e)))

= Unify{(H('e) = 'c), ('c = H('e)), ('c = H('e))} o {'d -> 'e} o {'f -> F(G('c,'c,'c),'e)} o {'a -> G('c,'c,'c)} o {'b->'c} by Delete on ('c='c)

= Unify{(H('e) = H('e)), (H('e) = H('e)), (H('e) = H('e))} o {'d -> 'e} o {'f -> F(G(H('e),H('e),H('e)),'e)} o {'a -> G(H('e),H('e),H('e))} o {'b->H('e)} o {'c -> H('e)} by Eliminate on ('c = H('e))

= Unify{} o {'d -> 'e} o {'f -> F(G(H('e),H('e),H('e)),'e)} o {'a -> G(H('e),H('e),H('e))} o {'b->H('e)} o {'c -> H('e)} by Delete on (H('e) = H('e))

 = {'d -> 'e , 'f -> F(G(H('e),H('e),H('e)),'e) , 'a -> G(H('e),H('e),H('e)) , 'b->H('e) , 'c -> H('e)}



(* = Unify {('a=S),(P(N, 'b) = P('c,'a))} by Decompose on (F('a, P(N, 'b)) = F(S, P('c, 'a))) *)
(* = Unify {('a=S), (N='c), ('b='a)} by Decompose on (P(N, 'b) = P('c,'a)) *)
(* = Unify {('a=S),(N='c)} o {'b->'a} by Eliminate on ('b='a) *)
(* = Unify {('a=S),('c=N)} o {'b->'a} by Orient on (N='c) *)
(* = Unify {('a=S)} o {'c->N} o {'b->'a} by Eliminate on ('c=N) *)
(* = Unify {} o {'a->S} o {'c->N} o {'b->'a} by Eliminate on ('a=S) *)
(*= {'a -> S, 'b -> S, 'c -> N}*)