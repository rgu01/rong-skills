# Flight query — Xi'an (China) → Stockholm (Sweden)

**Created:** 2026-08-10 · **Last updated:** 2026-08-10 · **Status:** resolved,
pending manual price verification

---

## 1. Trip

| Field | Value |
|---|---|
| Origin | Xi'an, China — **XIY** (Xi'an Xianyang International) |
| Destination | Stockholm, Sweden — **ARN** (Stockholm Arlanda) |
| Trip type | Round trip |
| Passengers | 1 adult *(assumed — unconfirmed)* |
| Cabin | Economy *(assumed — unconfirmed)* |
| Currency searched | SEK |

## 2. Date window

- **Swedish visa validity:** 2026-10-01 → 2027-01-13
- **Stay in Sweden:** 85–90 days *(relaxed from exactly 90 on 2026-08-10)*
- Both flights must fall wholly inside the visa window; the return must be on or
  before 2027-01-13.
- Dates are flexible inside the visa window if that lowers the fare.

## 3. Restrictions

1. **Carriers:** Air China (CA) or China Eastern (MU) only. No other marketing
   or operating carrier, including codeshares on a third airline.
2. **Routing:** exactly **one stop, and that stop must be inside China**.
   No stop outside China. No second stop.
3. **Transfer airport:** the transfer must be **within the same airport**.
   An itinerary arriving at Shanghai Hongqiao (SHA) and departing from Shanghai
   Pudong (PVG), or the reverse, is **disqualified**. *(Added 2026-08-10.)*
4. **Price:** select the **lowest** qualifying fare.

## 4. Day-count rule

Schengen days count **inclusive of both the arrival and the departure day**.

| Outbound | Return | Days | In 85–90 range |
|---|---|---|---|
| 2026-10-01 | 2026-12-29 | 90 | yes |
| 2026-10-01 | 2026-12-31 | 92 | **no — over** |
| 2026-10-02 | 2026-12-29 | 89 | yes |
| 2026-10-03 | 2026-12-31 | 90 | yes |
| **2026-10-04** | **2026-12-29** | **87** | **yes** |
| 2026-10-06 | 2026-12-29 | 85 | yes |
| 2026-10-08 | 2026-12-31 | 85 | yes |

---

## 5. RESULT

**Air China · 2026-10-04 → 2026-12-29 · 87 days · 6 137 kr**

| | |
|---|---|
| Outbound | XIY **09:35** → PEK → ARN **17:20** same day |
| Beijing connection | **2h00** |
| Total outbound | 13h45 |
| Return | 2026-12-29 from ARN, PEK connection, arrives XIY next day |
| Transfer airport | **PEK both directions** — single airport, satisfies restriction 3 |
| Fare | **6 137 kr** (1 adult, economy, SEK) |

Identical 6 137 kr fare also available **2026-10-06 → 2026-12-29** for an
85-day stay.

This beats the 6 559 kr the traveller found on the same dates by **422 kr**,
and it is the *best-connection* itinerary as well as the cheapest — most
low-priced CA fares carry a 15-hour Beijing layover.

### Runner-up (same-airport compliant)

| Airline | Outbound | Return | Days | Fare |
|---|---|---|---|---|
| Air China | 2026-10-05 | 2026-12-30 | 87 | 6 712 kr |

---

## 6. Search evidence

All searches: momondo.se, filtered `airlines=CA,MU; stops=1`, sorted by price,
1 adult, economy, SEK. Retrieved 2026-08-10.

### 6.1 Sweep before restriction 3 (airport change still allowed)

| Outbound | Return | Days | Best MU | Best CA |
|---|---|---|---|---|
| 2026-10-03 | 2026-12-31 | 90 | 5 390 kr | 8 971 kr |
| 2026-10-08 | 2026-12-31 | 85 | 5 390 kr | 8 972 kr |
| 2026-10-04 | 2026-12-29 | 87 | none | 6 137 kr |
| 2026-10-06 | 2026-12-29 | 85 | none | 6 137 kr |
| 2026-10-05 | 2027-01-02 | 90 | 5 772 kr | 6 183 kr |
| 2026-10-10 | 2027-01-07 | 90 | 5 436 kr | 6 183 kr |
| 2026-10-12 | 2027-01-09 | 90 | 5 436 kr | 6 759 kr |
| 2026-10-01 | 2026-12-29 | 90 | none | 7 876 kr |
| 2026-10-01 | 2026-12-28 | 89 | 11 700 kr | 9 450 kr |

### 6.2 Air China sweep under restriction 3

| Outbound | Return | Days | Cheapest compliant CA |
|---|---|---|---|
| **2026-10-04** | **2026-12-29** | **87** | **6 137 kr** |
| 2026-10-06 | 2026-12-29 | 85 | 6 137 kr |
| 2026-10-05 | 2026-12-30 | 87 | 6 712 kr |
| 2026-10-02 | 2026-12-29 | 89 | 7 876 kr |
| 2026-10-03 | 2026-12-28 | 87 | 8 081 kr |
| 2026-10-03 | 2026-12-31 | 90 | 8 971 kr |
| 2026-10-08 | 2026-12-31 | 85 | 8 972 kr |

---

## 7. Why China Eastern is eliminated

MU offered the outright cheapest fare in the whole search — **5 390 kr** — but
**every MU itinerary found routes the return `PVG → SHA`**: the long-haul MU290
lands at Pudong, while the Shanghai→Xi'an domestic leg departs from Hongqiao.
That is an airport change, so restriction 3 disqualifies all of them.

Checked across the 2026-10-03, 2026-10-08 and 2026-12-31 pairings; no
same-airport MU option appeared at any price in the top 20 results. The one MU
option with a clean *return* (9 614 kr) changes airports on the **outbound**
instead, and is more expensive than the winning CA fare regardless.

Two structural reasons MU fits this trip badly:

- **MU289/MU290 fly only 3×/week (Mon/Thu/Sat)**, so the return is pinned to
  those days. 2026-12-29 is a Tuesday — which is why MU never appears on the
  original dates at all.
- **Its Stockholm service is Pudong-only**, while its Xi'an domestic feeder
  favours Hongqiao, forcing the cross-city transfer.

Air China is unaffected: **every CA itinerary is PEK → PEK**.

## 8. Route reference

| Airline | Routing | Long-haul leg | Frequency |
|---|---|---|---|
| Air China (CA) | XIY → **PEK** → ARN | CA911 / CA731, dep 13:55–17:00, ~9h20 | 7×/week |
| | ARN → PEK → XIY | CA912, dep 18:10–22:20, ~8h20 | 12×/week |
| China Eastern (MU) | XIY → **PVG** → ARN | MU289, PVG 15:00 → ARN 20:10 | 3×/week Mon/Thu/Sat |
| | ARN → PVG → XIY | MU290, ARN 22:40 → PVG 14:40+1 | 3×/week |

Air China is the only nonstop operator on PEK–ARN. China Eastern's
Shanghai–Stockholm route resumed 2026-06-22 after a six-year gap, on an A330-200.

### Routings disqualified by restriction 2 (stop outside China)

MU sells XIY → ARN via **Vienna (VIE)**, **Istanbul (IST)** and **Milan (MXP)**.
All are excluded.

### Unverified

FlightConnections lists a CA option via PVG (~11h40). Possibly a codeshare on MU
metal, which would breach restriction 1. Not selected; not verified.

## 9. Source access log

Tested 2026-08-10 from client IP 155.4.16.2.

| Source | Status | Notes |
|---|---|---|
| **momondo.se** | **Works** | No bot wall. Source of every price in this document. Driven with Playwright headed Chromium. |
| airchina.se | Blocked | Plain fetch: form visible, no fares. Headless: hCaptcha wall. Headed: one clean load, then behavioural block — "Your current behavior is detected as abnormal" (event-id `7ecf8ee25917863493290feca1b8`). Not pursued; circumventing it would mean disguising the automation. |
| ceair.com | Blocked | Plain fetch: empty JS shell. Headless: hard block, no challenge offered (event-id `8592cac4d41786348916de9ecaf9`). Headed: homepage loaded; fare search not attempted. |
| Open web search | Partial | Yielded schedules and route structure. Fare figures were undated aggregates for other routes — discarded, superseded by momondo data. |

## 10. Caveats before booking

- Prices are **metasearch quotes from onward booking sites**, not confirmed
  airline fares, and they move. The 422 kr gap against the traveller's own
  6 559 kr find on identical dates suggests checking **which** booking site
  momondo is quoting.
- **Final price must be verified manually** on airchina.se — automated access is
  blocked, so this step cannot be done here.
- **Checked-baggage allowance is unverified** for this fare bucket.
- Assumes **1 adult, economy**. Both unconfirmed.

## 11. Open questions

- Passenger count and cabin.
- Checked-baggage requirement.
- Minimum or maximum acceptable layover duration in China.
- Preferred billing currency (all figures here are SEK).
