Itic3 <-list("Aylin Martinez", "Zuleyma de jesus Manzano", "Emanuel Ezparza");
> Edades <- list(20,18,21);
> View(Edades)
> Carreras <- list("Tic´s", "Gestion empresarial","Mecatronica","Industrial","Logistica");
> EdadesAlumnos <- list(Itic3, Edades);
> view(EdadesAlumnos)
Error in view(EdadesAlumnos) : could not find function "view"
> Itic3[1];
[[1]]
[1] "Aylin Martinez"

> Itic3[3];
[[1]]
[1] "Emanuel Ezparza"

> Itic3[2];
[[1]]
[1] "Zuleyma de jesus Manzano"

> EdadesAlumnos[[1]][[1]];
[1] "Aylin Martinez"
> Edades <- list(20,18,21,19);
> Edades[5] <-(30);
> Edades <- list(20,18,21,19);
> Edades[4] <-(30);
> Edades[4] <- NULL;
> Carreras [2] <- NULL;
> Itic3[1] <- list("Juan Prieto");
> setdiff(Edades, Edades);
list()
> Edades1 <- list(19,18,15);
> intersect(Edades, Edades1);
[[1]]
[1] 18

> setdiff(Edades, Edades1);
[[1]]
[1] 20

[[2]]
[1] 21
