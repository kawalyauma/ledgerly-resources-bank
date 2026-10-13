# Coded figures

Ledgerly draws these from a small spec, so the result is exact and the same whichever agent wrote it.
Put the spec in `figures/<key>.json` as `"method": "coded"` with `"coded": { … }`.

| type | fields | example |
|---|---|---|
| `shape` | `shape`: circle, square, rectangle, triangle, right-triangle, equilateral-triangle, isosceles-triangle, parallelogram, rhombus, trapezium, kite, pentagon, hexagon, octagon | `{"type":"shape","shape":"trapezium"}` |
| `fraction` | `shape`: circle or bar; `numerator` 0–24; `denominator` 1–24 | `{"type":"fraction","shape":"bar","numerator":3,"denominator":5}` |
| `number-line` | `from`, `to` (−1000…1000), `step` > 0, `marks` (≤ 12 numbers to highlight) | `{"type":"number-line","from":0,"to":10,"step":1,"marks":[3,7]}` |
| `clock` | `hour` 0–23, `minute` 0–59 | `{"type":"clock","hour":3,"minute":45}` |
| `map` | `region`: uganda; `layers` from regions, lakes, rivers, neighbours, towns, mountains, equator; `highlight` (≤ 10 names) | `{"type":"map","layers":["lakes","rivers"],"highlight":["Lake Kyoga"]}` |
| `bar-chart` | `title`, `yLabel`, `bars`: 1–12 × `{label, value}` | `{"type":"bar-chart","title":"Pupils present","bars":[{"label":"Mon","value":40}]}` |
| `column-sum` | `operation`: add, subtract or multiply; `numbers` (2–4 whole numbers); `showAnswer` | `{"type":"column-sum","operation":"add","numbers":[345,278],"showAnswer":true}` |
| `long-division` | `dividend`, `divisor` (whole numbers); `showWorking` | `{"type":"long-division","dividend":756,"divisor":6,"showWorking":true}` |
| `angle` | `degrees` 1–359; `label` | `{"type":"angle","degrees":60,"label":"x"}` |
| `venn` | `sets`: 2–3 × `{label, items}`; `both` (items in every set) | `{"type":"venn","sets":[{"label":"Even","items":["2","4"]},{"label":"Prime","items":["3","5"]}],"both":["2"]}` |

The numbers in a coded figure must come from the source (for example, the numbers of the
sourced question it illustrates).
