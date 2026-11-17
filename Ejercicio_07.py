## Ejercicio 7 — Búsqueda (10 pts)

#Las funciones reciben una `list` de `Cancion`. Se implementan a mano.

#```python
#def busqueda_lineal(canciones, campo, valor) -> list: ...
#def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion: ...
#```

#- `busqueda_lineal`: `campo` es `"titulo"`, `"artista"` o `"genero"`. Devuelve todas las canciones cuyo campo es igual a `valor`, en el orden original. Si no hay ninguna, lista vacía. `"Rock"` y `"Soda Stereo"` tienen que poder buscarse por este camino.
#- Binaria por `titulo`, sobre una lista ya ordenada alfabéticamente por `titulo`. Si el título no está, `CancionNoEncontradaError`. Si hubiera dos canciones con el mismo título, devuelve la primera que encuentre la búsqueda.

#**Teoría.** ¿Por qué `busqueda_binaria_por_titulo` pide la lista ordenada por título? ¿Qué complejidad tiene sobre `n` canciones, y qué complejidad tiene la búsqueda lineal por artista?

#---