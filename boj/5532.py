# https://www.acmicpc.net/problem/5532

days, math_total, lang_total, math, lang = [int(input()) for _ in range(5)]

days = days - max(
  math_total // math + (1 if math_total % math else 0),
  lang_total // lang + (1 if lang_total % lang else 0)
)

print(days)
