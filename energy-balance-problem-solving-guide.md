# A General Approach to Energy Balance Problems

*Working draft — methodology extracted from the E1–E4 problem set. Fill in / reorder as the course develops.*

The aim of this guide is a single, repeatable procedure that works whether the
system is steady or unsteady, flow or batch, and with or without a reaction,
phase change, or mixing effect. Every problem in this course should be
solvable by walking through the same sequence of steps — the differences
between problems are just *which terms survive* after step 3.

---

## 0. The one equation everything comes from

Every energy balance in this course starts from the same general,
unsteady-state balance on the system:

$$\frac{d(m_{sys}H_{sys})}{dt} = \sum \dot{m}_{in}H_{in} - \sum \dot{m}_{out}H_{out} + \dot{Q} + \dot{W}$$

Don't skip to a simplified/steady-state form from memory — write this down
first, every time. The simplifications in step 3 should be visible,
justified deletions from this equation, not a different equation pulled from
nowhere.

> **Sign convention:** $\dot{Q}$ and $\dot{W}$ are energy *added to* the
> system. A negative result means energy actually leaves the system (heat
> rejected, or work done *by* the system on the surroundings, e.g. a
> turbine). Keep the sign the maths gives you — don't flip it to make a
> number "look right." State what the sign means in words instead.

---

## 1. Define the system

- Draw the boundary. What's inside, what's crossing it?
- If there's more than one obvious system (e.g. a cell *and* a heat
  exchanger — see E1), treat each as its own system with its own balance,
  and be explicit about which streams connect them.

## 2. Classify the process

Two questions decide almost everything about how the balance simplifies:

| Question | If yes | If no |
|---|---|---|
| Is anything flowing in/out? | **Flow (open) system** — keep the $\dot{m}H$ terms | **Batch (closed) system** — $\dot{m}_{in}=\dot{m}_{out}=0$ |
| Is the system at steady state? | $\dfrac{d(m_{sys}H_{sys})}{dt}=0$ — solve directly, no integration needed | **Unsteady** — you must integrate over time (step 4) |

This gives four combinations. All four show up in the E-series:

| Scenario | Example | What survives |
|---|---|---|
| Steady, flow | E1(a)/(b) — electrowinning cell & heat exchanger; E2 — turbine | $\sum\dot{m}_{in}H_{in} - \sum\dot{m}_{out}H_{out} + \dot{Q} + \dot{W} = 0$, solved directly |
| Unsteady, flow | E1(c) — cell temperature rising over time with circulation off | $m$ still roughly constant, but $T(t)$ (and hence $H_{sys}$) changes — integrate |
| Unsteady, batch | E3 — mixing NaOH and water; E4 — bomb calorimeter | $\dot{m}_{in}=\dot{m}_{out}=0$, and you integrate from an initial to a final *state*, not over a flow |
| Steady, batch | — | Trivial/rare: nothing changes, nothing flows |

## 3. Apply assumptions to kill terms

State each assumption **in words**, then show the term it removes. Common
ones:

- Insulated / adiabatic $\Rightarrow \dot{Q} = 0$
- No shaft work $\Rightarrow \dot{W} = 0$
- No flow (closed vessel) $\Rightarrow \dot{m}_{in} = \dot{m}_{out} = 0$
- Steady state $\Rightarrow \dfrac{d(m_{sys}H_{sys})}{dt} = 0$
- Well-mixed system $\Rightarrow$ a single uniform $T$ (or composition)
  describes the whole system at any instant — needed before you can even
  write $m\,C_P\,dT/dt$

## 4. If unsteady: separate variables and integrate

This is the step that's easiest to shortcut — don't. For a batch system with
$\dot{Q}=\dot{W}=0$ and no flow, step 3 leaves:

$$\frac{d(m_{sys}H_{sys})}{dt} = 0$$

Separate and integrate between the initial state ($i$) and final state ($f$):

$$\int_i^f d(m_{sys}H_{sys}) = 0 \quad\Rightarrow\quad m_{sys,f}H_{sys,f} - m_{sys,i}H_{sys,i} = 0$$

**If the total system mass doesn't change** over the process (nothing added,
removed, or separated out — true for both E3 and E4, where the vessel is
sealed), $m_{sys}$ can be pulled outside the integral as a constant, which is
a cleaner route to the same place:

$$m_{sys}\int_i^f dH_{sys} = 0 \quad\Rightarrow\quad m_{sys}\,\Delta H_{sys} = 0 \quad\Rightarrow\quad \Delta H_{sys} = 0$$

This is the derivation both E3(b) and E4(c) now use. It only holds because
$m_{sys}$ is genuinely constant — if mass were entering or leaving, you'd
have to keep $m_{sys}H_{sys}$ together and go back to the flow-balance form
in step 0 instead.

If instead a source term survives (e.g. E1(c), where $\dot{W}_{excess}$ keeps
heating the electrolyte with the cooling circuit off):

$$m\,C_P\,\frac{dT}{dt} = \dot{W}_{excess} \quad\Rightarrow\quad t = \frac{m\,C_P\,(T_f-T_0)}{\dot{W}_{excess}}$$

The pattern is always: isolate the derivative, separate variables, integrate
both sides between defined limits.

## 5. Pick an explicit reference state

$H$ has no absolute zero — only *differences* in enthalpy matter. Before
you can write down $H_{sys,i}$ or $H_{sys,f}$ as numbers, you must choose a
reference state where $H \equiv 0$, and hold every term in the balance to
that same reference.

- Pick a reference that's *convenient for the data you have* — e.g. E3 uses
  0 °C (and the *unmixed* species) because the water starts there. E4 uses
  298.15 K with the standard $\Delta H^\circ_f$ table, because that's what
  the formation-enthalpy data is defined against.
- Say the reference state out loud in the write-up: "relative to the
  unmixed components at 0 °C" (E3) / "relative to the elements at 298.15 K"
  (E4, implicitly, via $\Delta H_f$). If you don't state it, a marker (or
  future-you) can't check whether every term is consistent with it.

## 6. Build up $H_{sys}$ term by term

Every enthalpy term is some combination of:

- **Sensible heat**: $n\,C_P\,(T-T_{ref})$ or $m\,C_P\,(T-T_{ref})$ — moving
  something's temperature away from the reference, with no change of phase
  or composition.
- **Latent heat**: $x\,\Delta H_{vap}$, $(1-x)\,\Delta H_{vap-liq}$, etc. —
  a phase change at constant $T$ (E2).
- **Reaction/mixing enthalpy**: $\Delta H_{rxn}$, $\Delta H_{dissolution}$,
  etc. — a change of chemical identity, evaluated at some reference
  temperature and then corrected with sensible heat if the reaction doesn't
  happen at the reference temperature (E3, E4).

**Watch intensive vs. extensive.** Table values for $\Delta H_{rxn}$ and
$\Delta H_{dissolution}$ are *intensive* — per mole or per kg reacted/mixed
— but the system balance is written in *extensive* enthalpy ($\Delta H_{sys}$,
units of kJ). Every intensive term must be multiplied by the amount actually
present before it can be added into the balance: moles reacted for
$\Delta H_{rxn}$ (E4 uses $n_{sucrose}\,\Delta H_{rxn}$, not bare
$\Delta H_{rxn}$), mass of solution for $\Delta H_{dissolution}$ (E3 uses
$m_{solution}\,\Delta H_{dissolution}$). Missing this multiplier is a very
easy, very silent unit error — it won't fail dimensionally in a units-free
scribble, only when you actually track the units through.

**The key move — and the fix made to E3(b):** when a process is adiabatic
and something reacts/dissolves/mixes, the reaction or mixing enthalpy is not
a separate "heat leaving the system" term. It is *part of the final state's
enthalpy*, because the energy released by dissolution/reaction stays inside
an insulated system and shows up as a higher final temperature instead.
General template (for a mass basis; swap $m_k \to n_j$ for a molar/reaction
basis as in E4):

$$\Delta H_{sys} = \underbrace{\xi\,\Delta H_{rxn\ /\ dissolution}}_{\text{reaction/mixing, at }T_{ref}} + \underbrace{\sum_k m_k\,C_{P,k}\,(T_f - T_{ref})}_{\text{sensible heat, everything present at }T_f} = 0$$

where $\xi$ is the extent of reaction/mixing (moles reacted, or mass
dissolved) — the multiplier from the paragraph above. This is the general
template for any adiabatic reaction/mixing/dissolution problem: react or mix
at the reference temperature, then carry every product and every inert
(bomb, water bath, excess reagent, …) up to $T_f$ with sensible heat. Set
the sum to zero (from step 4) and solve for $T_f$.

## 7. Solve, then sanity-check

- Rearrange for the unknown **symbolically first** — get a clean formula in
  terms of the given quantities before substituting a single number (E3(a)
  and E4(d) both do this: solve for $T_f$ algebraically, *then* plug in).
  It's much easier to spot a units/sign mistake in a formula than buried in
  arithmetic, and it makes the final numeric substitution a one-line check.
- Solve the resulting algebraic equation for the unknown.
- Check the **sign** makes physical sense (exothermic $\Rightarrow$
  negative $\Delta H$; work done *by* a turbine $\Rightarrow$ negative
  $\dot{W}$ under the convention in step 0) and say what the sign means in
  words rather than silently flipping it.
- Check **magnitude** — does $T_f$ move in the direction you'd expect?
  Is the answer a plausible temperature/duty/flow rate for the physical
  situation?

---

## Worked examples by scenario (cross-reference)

| Step | E1 (electrowinning) | E2 (turbine) | E3 (NaOH mixing) | E4 (bomb calorimeter) |
|---|---|---|---|---|
| Flow vs batch | Flow | Flow | Batch | Batch |
| Steady vs unsteady | Both (a/b steady, c unsteady) | Steady | Unsteady | Unsteady |
| Reference state needed? | No (uses $\Delta T$ directly) | No (steam tables have their own reference) | Yes — 0 °C, unmixed species | Yes — 298.15 K, elements (via $\Delta H_f$) |
| Extra enthalpy term | — | Latent heat ($\Delta H_{vap}$) | Mixing enthalpy ($\Delta H_{dissolution}$) | Reaction enthalpy ($\Delta H_{rxn}$) |
| Intensive → extensive multiplier ($\xi$) | — | — | $m_{solution}$ (mass basis) | $n_{sucrose}$ (molar/extent-of-reaction basis) |
| $m_{sys}$ pulled out of $\int dH_{sys}$? | — | — | Yes (E3(b)) | Yes (E4(c)) |

---

## To do

- [ ] Add a short "how to spot which scenario you're in" flowchart (maybe a
      diagram) at the top, before step 1.
- [ ] Add a fully worked template problem showing all 7 steps end-to-end,
      annotated.
- [ ] Decide where this lives: standalone chapter (e.g.
      `02b-ebal-problem-solving.qmd`) vs. a section inside the intro
      chapter — probably wants to come *before* the worked examples/problems
      chapters in the `chapters:` list.
- [ ] Cross-link from each `problems/problem-eN.qmd` solution back to the
      relevant step(s) here, once this has a stable heading structure.
