# Final prior-art audit — 12 August 2026

## Scope

The final audit targeted four claims that could affect originality: (i) the standard seed-2 block structure; (ii) prime-platform/appearance-index formulas; (iii) perfect-power classification; and (iv) eventual coalescence for arbitrary positive integer seeds.

Searches covered the directly related OEIS family, exact-recurrence web searches, the cited greatest-prime-factor recurrence literature, the 2026 HMMT official solution, and the April 2026 Mathematics Stack Exchange discussion on composite squares. This is a good-faith targeted audit, not a logically exhaustive search of all unpublished or non-indexed mathematics.

## Findings

### 1. Standard orbit and block structure are prior art

- OEIS A036441 records the exact seed-2 recurrence, a closed block formula, quadratic bounds, and a general-seed notation `a(m,n)` with several shift identities.
- OEIS A076271 records the same recurrence with a one-index shift, the consecutive-prime multiple blocks, transition products of consecutive primes, and the presence/positions of prime squares.
- A076272 records the greatest-prime-factor plateau sequence; A076273 the increase positions; A075527 the plateau widths; A076274 the square positions.
- HMMT February 2026 Guts Round, Problem 8, gives an induction proving consecutive prime products appear and describes the transition through multiples of the next prime.

**Consequence for the manuscript:** none of these items is claimed as a new main theorem. They are used as prior structure and are reproved only for self-containment.

### 2. The no-composite-square special case is already publicly proved

The Mathematics Stack Exchange question “Are there any squares of composite numbers in the sequence …?” (22 Apr 2026) received an answer by Thomas Andrews proving that a composite square cannot occur, using the block bound and Bertrand's postulate.

**Consequence:** the manuscript now explicitly treats “no composite squares” as prior public reasoning. Its perfect-power theorem is presented as an extension from squares to all perfect powers, but **no absolute priority claim is made** for that extension.

### 3. Greatest-prime-factor recurrence literature is related but not the same global-seed statement

The identified Caragiu / Back–Caragiu works study greatest-prime-factor driven recurrences, including ultimate periodicity in other recurrence families. The exact seed-addition map studied here is already catalogued in OEIS; the literature located in this audit did not supply a proof of universal eventual coalescence of all positive integer seeds for `x -> x + P^+(x)`.

### 4. Universal coalescence for all seeds: no proof found in the targeted audit

OEIS A036441 explicitly defines general seeds and gives important shift identities, including eventual shifts among prime seeds, but its current entry does not state that **every** integer seed eventually joins the seed-2 orbit. Exact-phrase and recurrence searches performed on 12 Aug 2026 did not reveal such a theorem.

**Consequence:** the manuscript keeps universal coalescence as an open conjecture, supported by a proved sufficient attraction criterion and an exhaustive finite scan through 10,000,000. The text says “no proof was found in the sources searched,” not “this has never been studied/proved anywhere.”

## Principal sources checked

- https://oeis.org/A036441
- https://oeis.org/A076271
- https://oeis.org/A076272
- https://oeis.org/A076273
- https://oeis.org/A075527
- https://oeis.org/A076274
- https://math.stackexchange.com/questions/5134042/
- https://hmmt-archive.s3.amazonaws.com/tournaments/2026/feb/guts/solutions.pdf
- Back, G. & Caragiu, M. (2010), *The Greatest Prime Factor and Recurrent Sequences*, Fibonacci Quarterly 48(4), 358–362.
- Caragiu, M. (2010), *Recurrences based on the greatest prime factor function*, JP Journal of Algebra, Number Theory and Applications 19(2), 155–163.
