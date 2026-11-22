# tiny-chess-01 — entry report

## Status: READY TO SUBMIT (parent: bundle + submit top-level only)

- **Engine**: alpha-beta + quiescence, house PSTs, TT, killers, MVV-LVA,
  iterative deepening, fixed **50,000 nodes/move** (no clock, no randomness).
  Game-history repetition via accumulated hashes.
- **Packed `main.py`**: **4,079 bytes** (≤ 4,096). lzma + base85 payload

## Practice results (packed entry, local kit env, 50k nodes/move)

| Trial | W-D-L | Elo | Avg/max think |
|---|---|---|---|
| 0 | 3-0-3 | 1,279 | 1.42 s / 2.38 s |
| 1 | 4-0-2 | 1,451 | 1.39 s / 2.51 s |
| 2 | 4-0-2 | 1,451 | 1.33 s / 1.89 s |
| **Mean** | | **≈ 1,394** | |

Floor 1,154 cleared. Baseline (sunfish 4K) mean ≈ 1,365. Our mean ≈ 1,394 is
**above the baseline**. Think times well under 10 s. Deterministic.
## Bugs fixed

1. Driver var `g` shadowed move-gen `g()` → TypeError, first-legal-move
   fallback (Elo 0). Renamed driver var to `W`.
2. TT-move ordering in `od()`: TT capture lost top priority. Restored
   `if m==tt:return 1000000`.
3. En passant capture square reversed in `mk()`/`uk()`. Fixed; verified by
   perft + EP tests.
4. No game-history repetition (`HI` reset each move). Fixed by accumulating
   hashes. Gain: trial-0 Elo 876 → 1,279.

## Build / sources

`minify.py` + `pack.py` on `work/dev/compact2.py` → `main.py`.
Logs: `work/runs/t0-packed12b/`, `t1-packed12/`, `t2-packed12/`.

## Risks

- TT mate scores stored without ply adjustment (size cut)
- Mean beats baseline by only +29; final uses different openings; prizes need
  beating the baseline (90% paired t-interval above 0)
