# `dffs` and Category Theory

## `Data.Function.on`

The core pattern in `dffs` is Haskell's [`on`][Data.Function.on]:

```haskell
on :: (b -> b -> c) -> (a -> b) -> a -> a -> c
(cmp `on` f) x y = cmp (f x) (f y)
```

Each `dffs` CLI instantiates `on` with a specific comparator:

| CLI | `cmp` | `f` | `x`, `y` |
|-----|-------|-----|----------|
| `diff-x` | `diff` | shell pipeline | two files |
| `git-diff-x` | `diff` | shell pipeline | file at two commits |
| `comm-x` | `comm` | shell pipeline | two files |

## Arrow notation

In the category of functions (or, more generally, any [monoidal category] with a [product bifunctor][bifunctor] `(***)` and composition `(>>>)`), the pattern is:

```
(f *** f) >>> cmp
```

where `(***)` applies `f` to both components of a pair independently, then `(>>>)` feeds the results into `cmp`:

```
           ┌─── f ───┐
(a, b) ─── *** ──────┼─── (f(a), f(b)) ─── cmp ─── result
           └─── f ───┘
```

In Haskell's `Control.Arrow`:

```haskell
import Control.Arrow (Arrow, (***), (>>>))

dffs :: Arrow arr => arr a b -> arr (b, b) c -> arr (a, a) c
dffs f cmp = (f *** f) >>> cmp
```

## Why this matters

Shell pipelines are morphisms in a category where objects are "streams of bytes" and composition is `|`. `dffs` lifts a unary pipeline `f` into a binary comparison via the product bifunctor — applying `f` independently to both inputs, then comparing the results.

This is why the transform `f` need not know anything about the comparison, and vice versa. They compose orthogonally, which is what makes `dffs` commands useful: any pipeline (sort, jq, wc, head, awk, …) can be paired with any comparator (diff, comm) without either needing to be aware of the other.

[Data.Function.on]: https://hackage.haskell.org/package/base/docs/Data-Function.html#v:on
[monoidal category]: https://en.wikipedia.org/wiki/Monoidal_category
[bifunctor]: https://hackage.haskell.org/package/base/docs/Data-Bifunctor.html
