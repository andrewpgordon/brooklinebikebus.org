# Route analysis — Corey Hill and the Driscoll approach

All elevations are USGS 3DEP 10-metre ground heights sampled along OpenStreetMap
street centrelines, via OpenTopoData. Distances are Dijkstra street routing over
the OSM network, not straight lines. Good enough to plan with; **not a substitute
for riding it.**

---

## The core geography

Driscoll sits at about **116 ft** on Washington Street, on the **southwest flank
of Corey Hill**. Most Driscoll families live on the **east shoulder** of that
hill — Mason Terrace, York Terrace, Lancaster Terrace, Jordan Road — at roughly
**150–220 ft**.

**The hill sits between the families and the school.** That is the whole problem,
and there is no gentle way over or around it. Every route off the east shoulder
is steep, arterial, or long. The plan solves it by keeping the hill out of the
ride entirely: families walk down, then ride the flat part.

## Key elevations (feet)

| Point | ft |
|---|---|
| Griggs Park, NE corner *(meeting point)* | 36 |
| Griggs Park, centre | 30 |
| Coolidge Corner (Beacon & Harvard) | 54 |
| Summit Ave at Beacon St | 76 |
| Washington Square (Beacon & Washington) | 88 |
| Corey Rd, north end at the Boston line | 86 |
| Corey Rd, south end at Beacon | 94 |
| Lancaster Terrace, SE end | 108 |
| **Driscoll School, Washington St frontage** | **116** |
| Corey Rd × Washington St | 128 |
| Summit Ave × Mason Terrace | 137 |
| Westbourne Terrace, north end | 150 |
| Summit Ave, NW end at Washington St | 151 |
| Corey Rd × Summit Ave | 157 |
| **Summit Ave × Jordan Rd** *(walk starts here)* | **218** |
| Lancaster Terrace, NW end | 218 |
| **Corey Hill Outlook — crest of Summit** | **258** |

## Contour roads — flat, and the reason one meeting point works

These wrap around the hill at near-constant height, so families anywhere along
them can reach a gathering point on level ground.

| Road | Range | Length |
|---|---|---|
| **Mason Terrace** | 122–158 ft | 0.78 mi |
| **York Terrace** | 199–220 ft | 0.30 mi |

## Every way *down* off the east shoulder, measured

| Way down | Grade | Drop | Verdict |
|---|---|---|---|
| **Lancaster Terrace** (SE to Beacon) | **6.4–7.0%, steady** | 149 → 101 ft over 0.14 mi | Gentlest by a wide margin, quiet, no pitchy surprise. **This is what we tell families to use if they ride down.** |
| Mason Terrace, north end → Bellvista | 6.4% | 137 → 119 ft | As gentle, but lands on the wrong side for Griggs Park. |
| **Summit Avenue** | 8.3% avg, **12.1% max** | 258 → 76 ft over 0.42 mi | **No.** Long, steep, finishes at a signalised arterial. It is also the obvious road, which is why the flyer names Lancaster instead. |
| **Jordan Road, west end** | **13.4%** | 209 → 144 ft over 0.09 mi | **No — warn people.** Steepest pitch in the neighbourhood. Jordan is flat and pleasant along its eastern length; the entire drop is in the last block, which is how it catches people out. |

Summit Ave's northwest flank (crest → Washington St) is 5.8% average with a
**13.3%** maximum. Also no.

## The chosen route

**Walking leg — 0.48 mi.** Summit Ave → footpath → Marion St → Griggs Terrace.
Covers the 12% block (Jordan→Mason) and the 7.8% block (Mason→Beacon) on foot.
Crosses Beacon at the Summit Ave signal. 15 minutes at a bike-pushing pace with
kids is comfortable but not generous — **verify on foot.**

**Riding leg — 0.74 mi, max 3%, average ~2.3%.** Griggs Park NE corner →
Griggs Terrace around the park → Griggs Road → Washington Street → Driscoll.
Monotonic climb, 36 → 116 ft, no descents. Crosses Beacon once, at the
Washington Square signal, **on foot**.

## Routes considered and rejected

| Route | Why not |
|---|---|
| Griggs Park → Beacon St west → Washington Sq → Westbourne Terr | Half a mile ridden **on** Beacon Street. |
| Summit & Mason → Lancaster Terr → Beacon St → Washington Sq | A fifth of a mile ridden on Beacon. Only viable with a police escort, which can't be sustained monthly. |
| Coolidge Corner → Beacon St west | Half a mile of arterial. Fine for confident riders, wrong for six-year-olds. |
| Corey Road → Washington St (0.43 mi, max 3.7%, zero Beacon) | Genuinely excellent route — but it serves the hill's **west** side, and our families are on the **east**. Revisit only if the sign-up data says otherwise. |
| Mason Terr north → Bellvista → Corey Rd → Washington St (0.95 mi, max 6.4%) | The only Beacon-free, Summit-free way **around** the hill from the east side. Real and rideable, but a third longer with a 38 ft climb over the north shoulder. Needs six leaders. **This is the leading candidate for route two.** |

## Benchmark — the Lincoln bike bus

Nathan's Route 2 is the model we copied the schedule from. Downes Playground →
Chestnut St → Lincoln School: **0.85 mi, 40 → 97 ft, 1.3% average, done in 15
minutes of riding** with a 15-minute gathering window before it. Our ride is
shorter on a slightly steeper grade, so 15 minutes is realistic.

The thing worth stealing from Lincoln is **the gathering window, not the ride
time.** Standing around from 7:15 to 7:30 doing helmet checks is what absorbs a
late family or a flat tyre.

## Reproducing any of this

```
Overpass API   → street network + park/school polygons for a bbox
Dijkstra       → path, penalising "Beacon Street" ×6 and footways ×50 for riding
OpenTopoData   → /v1/ned10m?locations=lat,lon|lat,lon…  (USGS 3DEP 10 m)
projection     → equirectangular, x scaled by cos(42.34°)
```

Gotchas that cost time the first go:
- Overpass rate-limits; space requests a few seconds apart and check whether the
  response starts with `<` (an HTML error page) before parsing JSON.
- Routing to a park's *centroid* produces silly detours. Route to the **path
  node at the entrance** instead — that is why the meeting point is the NE
  corner, where a footpath actually meets the park.
- Google's geocoder and OSM disagree on Driscoll's address. OSM has the school
  on Lancaster Terrace; the postal address is 725 Washington St.
