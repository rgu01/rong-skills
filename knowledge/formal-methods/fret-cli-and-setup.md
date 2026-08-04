# FRET, part 2: CLI, headless setup, and the two-tier plan

How to drive NASA **FRET** from the command line (no GUI), what was installed on
this machine, and the verified state of the two-tier "AI formalizes + verifies"
workflow. Companion note: [`fret-concepts-and-fretish.md`](fret-concepts-and-fretish.md)
covers concepts and FRETish.

Repo cloned at `~/projects/fret` (FRET v3.1.0). App lives in `fret-electron/`.

---

## FRET is NOT GUI-only — it ships a CLI

Source: `~/projects/fret/fret-electron/app/cli/fretCLI.js` (built binary:
`app/cli/fretCLI.main.js`). Three commands:

| Command | What it does | State needed |
|---|---|---|
| `formalize '<fretish>'` | FRETish sentence → temporal-logic formula | **none — stateless** |
| `realizability <project> <component>` | Runs Kind2/JKind on a stored component | needs the project DB |
| `list [project]` | Lists stored projects / components | needs the project DB |

Invoke (from `fret-electron/`):
```bash
node app/cli/fretCLI.main.js --help
node app/cli/fretCLI.main.js formalize 'sw shall satisfy x'
```

What "verify" means here — **two distinct checks**, only one is stateless:

- **A. Valid FRETish + meaning** (`formalize`): pass → returns LTL; fail → parse
  error. Stateless, always available.
- **B. Realizability** (`realizability`): pass → realizable; fail → unrealizable
  + `--diagnose` prints the conflicting requirement set. Needs a project in the
  DB **and** a solver.

Neither proves *the product satisfies the requirement* — that is Kind2
model-checking a Lustre model against the CoCoSpec export, a separate step
outside `fretcli`.

### `formalize` output logics (options)

| Option | Meaning |
|---|---|
| `-l ft-inf` | future-time, infinite traces (**default**) |
| `-l ft-fin` | future-time, finite traces |
| `-l pt -lang smv` | past-time, SMV LTL |
| `-l pt -lang lustre` | past-time, **CoCoSpec** (Lustre) |

Errors go to **stderr**; the formula goes to **stdout** (a wrapper should read
the first stdout line and check the exit code). It also prints harmless
`Error for modelDB` / LevelDB noise until the DB dir is initialized (see below).

---

## The two-tier plan

- **Tier 1 — fully CLI, stateless (works now).** English → AI drafts FRETish →
  `fretcli formalize` → pass (valid + LTL) / fail (parse error) → render friendly.
  This is the authoring/validation loop.
- **Tier 2 — realizability.** Needs (a) solvers installed [DONE], and (b) a way to
  get requirements into FRET's DB. The CLI has **no `import` command**; the
  shipped path is the GUI (or a custom headless loader we'd write). This is the
  one remaining design gap — architectural, not an install.

---

## What was installed on this machine (2026-07-22)

Environment: WSL2, Ubuntu 22.04, glibc 2.35, x86_64, WSLg present (GUI works),
nvm present, Java 11 present.

1. **Node 20** via nvm (FRET supports 16.16–20.19; the machine default v22 is too
   new for the Electron native build). Use `nvm use 20` in the FRET shell; the
   CLI itself also runs fine under v22.
2. **FRET app**: `git clone … ~/projects/fret && cd fret-electron &&
   npm run fret-install` (heavy: Electron + `tools/LTLSIM/ltlsim-core`). GUI:
   `npm start`.
3. **Solvers for Tier 2 realizability**, installed **without sudo** into
   `~/.local/bin` (already on PATH via `.profile`/`.bashrc`):
   - **kind2 v2.2.0** — single static binary from the kind2-mc GitHub release.
     (Install guide flags **v2.3.0 as unsupported**, so v2.2.0 was chosen.)
   - **z3 4.14.1** — the **glibc-2.35** build (z3 5.x/4.15+ prebuilts target
     glibc 2.39 and will NOT run on Ubuntu 22.04).

FRET's solver detection (`model/realizabilitySupport/realizabilityUtils.js`,
`checkDependenciesExist`) probes `kind2 -h`, `z3 -h`, `jkind -help`,
`jrealizability -help`, `which aeval`. A **valid configuration** is
`[kind2, z3]` **or** `[jkind, z3]` (`aeval` is optional). We satisfy `[kind2, z3]`
— the default engine. JKind was skipped (its v4.6.1 release ships no prebuilt
binary; kind2+z3 is already complete).

### Verified results

Tier 1 — `formalize 'when overheatDetected the controller shall within 3 ticks satisfy warningLight'`:

```
# ft-inf (default):
((G (((! overheatDetected) & (X overheatDetected)) -> (X (F[0,3] warningLight)))) & (overheatDetected -> (F[0,3] warningLight)))
# ft-fin:
((LAST V (((! overheatDetected) & ((! LAST) & (X overheatDetected))) -> (X ((F[0,3] warningLight) | (F[0,2] LAST))))) & (overheatDetected -> ((F[0,3] warningLight) | (F[0,2] LAST))))
# pt -lang smv:
(H ((O[3,3] ((overheatDetected & (Z (! overheatDetected))) & (! warningLight))) -> (O[0,2] ((Z FALSE) | warningLight))))
# pt -lang lustre (CoCoSpec):
H((OT(3, 3, ((overheatDetected and ZtoPre(not (overheatDetected))) and not (warningLight))) => OT(2, 0, (ZtoPre(false) or warningLight))))
```

Tier 2 — solver detection: `kind2 -h` OK, `z3 -h` OK. Running
`fretcli realizability <dummy> <dummy>` gets **past** the solver gate (no
"No valid solver configuration" error) and fails only on the missing project DB
— confirming solvers are wired; the DB is the only remaining blocker.

---

## Manual steps left (both need sudo — could not be automated this session)

**1. Install the missing Electron GUI libraries.** The FRET GUI has never been
launched here, and 4 of 6 runtime libs are absent (`ldconfig -p` check, 2026-07-22):
present = `libgtk-3`, `libnss3`; **missing = `libgbm1`, `libdrm2`, `libasound2`,
`libx11-xcb1`**. The CLI does not need them, but `npm start` will not display
until they are installed:

```bash
sudo apt-get install -y libgbm1 libdrm2 libasound2 libx11-xcb1
```

**2. Initialize the database via one GUI launch.** FRET's DB
(`~/Documents/fret-db`, `~/Documents/model-db`) is created on the **first GUI
launch**. Until then `formalize` still works but prints LevelDB noise to stdout,
and `realizability`/`list` cannot run:

```bash
cd ~/projects/fret/fret-electron && nvm use 20 && npm start   # opens the FRET window once
```

After that, requirements authored (or imported) in a project become available to
`fretcli realizability` and `fretcli list`.

> **Compatibility caveat:** the kind2 v2.2.0 + z3 4.14.1 pairing is *inferred*
> (guide only says "v2.3.0 unsupported") and detected by FRET's probe, but has
> **not** been exercised end-to-end against FRET 3.1.0 — no realizability run has
> happened yet (needs a project). Confirm on the first real project.

---

## Next design item (Tier 2 headless)

To make realizability fully agent-driven we need a **headless path to load a
project into FRET's LevelDB** (the GUI's Import reads a project JSON). Options:
reuse FRET's internal DB-support modules from a small Node script, or drive an
import. This is where the future **FRET skill + MCP server** lives:

- **MCP tool** `fret_formalize(fretish, logic)` → wraps `fretcli formalize`
  (deterministic grounding, stateless — ready today).
- **MCP tool** `fret_realizability(project, component)` → wraps
  `fretcli realizability --diagnose --json` (after the headless-import gap is solved).
- **Skill** orchestrates: extract from Word → draft FRETish → formalize/validate
  → render pass/fail + diagnosis in a user-friendly way.
