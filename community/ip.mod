# valtozok, parameterek
param N; # csucsok szama
param m; # elek szama

set V := 1..N; # csucsok
set VV dimen 2;

param a {V,V} default 0; # szomszedsagi matrix, ai,j 1, ha van el i es j kozott, kulonben  0
param d {V} ; # di: i fokszama

param qij{i in V, j in V: i<j} = (a[i,j] - (d[i]*d[j]) / (2*m)); # modularitas matrix

# 0, ha i �s j csucsok ugyanabban a kozossegben vannak, 1 kulonben
var x {i in V, j in V: i<j} binary;

# celfuggveny 
maximize modularitas: 1/(2*m) * sum{i in V, j in V: i<j} qij[i,j]*(1 - x[i,j]);

# feltetelek, ha i �s j egy kozossegben van, �s j �s k is egy kozossegben van, akkor i �s k is
subject to elek1 {i in V, j in V, k in V: i<j<k}: x[i,k] + x[i,j] - x[j,k] >= 0;
subject to elek2 {i in V, j in V, k in V: i<j<k}: x[i,k] - x[i,j] + x[j,k] >= 0;
subject to elek3 {i in V, j in V, k in V: i<j<k}: - x[i,k] + x[i,j] + x[j,k] >= 0;