### Buff Predicates

Added a system to simplify the code when searching for buffs. You can generate a function that takes a template buff
(nominally of `EQ_Affect`, `CachedBuff`, or `EQ_Spell*` types) that can be passed into a function to count or get buffs.
Four useful classes that inherit from `SpellAttribute<T>` were created:

- `SpellAffect(eEQSPA, (optional) isIncrease = true)`
- `SpellCategory(eEQSPELLCAT)`
- `SpellSubCat(eEQSPELLCAT)`
- `SpellClassMask(PlayerClass...)`

These objects can be chained together with normal boolean operators (&&, ||, and the unary ! for `SpellClassMask`) to create a predicate function. Use of this is something like:

```cpp title="Example (C++)"
auto buffslot = GetSelfBuff(SpellAffect(SPA_AC, true)
    && SpellCategory(SPELLCAT_HP_BUFFS)
    && (SpellSubCat(SPELLCAT_AEGOLISM) || SpellSubCat(SPELLCAT_SYMBOL))
    && SpellClassMask(Cleric));
```

As part of this change, the following functions have been deprecated, as their functionality has been replaced by this new system:

- GetTargetBuffByCategory()
- GetTargetBuffBySubCat()
- GetTargetBuffBySPA()
- HasCachedTargetBuffSubCat()
- HasCachedTargetBuffSPA()
- GetSelfBuffByCategory()
- GetSelfBuffBySubCat()
- GetSelfBuffBySPA()
- GetSelfShortBuffBySPA()
