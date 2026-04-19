def qaytarish(ro'yxat):
    saqlangan = []
    natija = []
    for i in ro'yxat:
        if i not in saqlangan:
            saqlangan.append(i)
            natija.append(i)
    return natija

ro'yxat = [1, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9]
print(qaytarish(ro'yxat))
```

```python
def qaytarish(ro'yxat):
    return list(dict.fromkeys(ro'yxat))

ro'yxat = [1, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9]
print(qaytarish(ro'yxat))
