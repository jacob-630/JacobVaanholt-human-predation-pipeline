# Web of Science Search Strings

Search strings for the human and natural predation review. Platform: Web of Science Core Collection, Advanced Search, field tag TS (title, abstract, author keywords, Keywords Plus). No date or language limits at search. Last updated 16 November 2026.

For the method, rationale and validation status, see `search_strategy.md`.

## Status

| Module | Version | Status |
| :-- | :-- | :-- |
| HT: human terrestrial | v3 | Run in Web of Science: 2,076 records. Sample DOIs tested were all retrieved. |
| HA: human aquatic | v1 | Candidate. Not yet run in Web of Science. |
| NT: natural terrestrial | v3 (core plus wrapper) | Candidate. Not yet run. |
| NA: natural aquatic | v3 (core plus wrapper) | Candidate. Not yet run. |

## How to use these strings

- Paste each string with its line breaks. Quotation marks must be straight (`"`), not typographic.
- Run each clause (each block between `OR` lines) as its own search first and record its count. A clause that returns tens of thousands of records is the one to fix. Then run the full string.
- For NT and NA, run the natural predator core once, note its search number in the history, and replace `#CORE` in the wrapper with that number.
- Record the date, platform, field codes, counts and the full string for PRISMA-S.
- Hyphenated terms are quoted on purpose. Do not remove the quotes.

## HT v3: human terrestrial (final)

```
TS=(
(hunter* NEAR/5 (success OR successful OR unsuccessful OR failure OR failed OR efficiency OR efficient OR effort OR performance OR "kill rate*" OR "kills per" OR "harvest per" OR "empty-handed" OR bagged))
OR
(("harvest success" OR "hunt success" OR "hunting success") NEAR/10 (hunter* OR firearm* OR rifle* OR archery OR bowhunt* OR licen* OR "tag holder*" OR "game animal*" OR "wild game"))
OR
(hunter* NEAR/10 ("observation rate*" OR "observation success" OR "observation* per" OR "seen per" OR "sightings per" OR "encounter rate*" OR "sighting rate*" OR "search time"))
OR
(hunter* NEAR/10 (stalking OR stalked OR chase OR chasing OR "approach distance*" OR "flight initiation distance*" OR "flushing distance*" OR "hunting mode*" OR "hunting strateg*" OR "hunting technique*"))
OR
(hunter* NEAR/10 (wound OR wounded OR wounding OR crippled OR crippling OR unrecovered OR "not recovered" OR "not retrieved" OR nonretriev* OR "non-retriev*" OR nonrecover* OR "non-recover*" OR "blood trail*" OR "tracking dog*" OR "recovery dog*" OR "shot placement" OR "missed shot*" OR "shot opportunit*" OR "shooting distance*" OR "shooting performance"))
OR
(("crippling ratio*" OR "crippling rate*" OR "crippling loss*" OR "wounding rate*" OR "wounding loss*" OR "wounded and lost" OR "wounded-and-lost" OR "hunting-induced wounding" OR "hunting induced wounding") NEAR/15 (hunt OR hunts OR hunted OR hunting OR hunter* OR shooting OR shotgun* OR gunshot OR rifle* OR firearm* OR archery OR arrow* OR crossbow* OR bowhunt* OR "game animal*" OR wildlife))
OR
(("embedded pellet*" OR "embedded shot*" OR "shotgun pellet*" OR "gunshot pellet*") NEAR/15 (crippl* OR wound* OR hunter* OR hunting))
OR
(("recreational hunt*" OR "sport hunt*" OR "subsistence hunt*" OR "traditional hunt*" OR "customary hunt*" OR "trophy hunt*" OR "commercial hunt*" OR "regulated hunt*" OR "legal hunt*" OR bowhunt* OR "bow hunt*" OR "archery hunt*" OR "persistence hunt*" OR "hound hunt*" OR "drive hunt*" OR "hunting with dogs" OR "hunting season*" OR "hunting licen*" OR "hunting permit*" OR "hunting quota*" OR "hunting regulation*" OR bushmeat OR "wild meat") NEAR/10 (success OR successful OR unsuccessful OR failure OR efficiency OR wound OR wounded OR wounding OR crippling OR kill OR kills OR "kill rate*" OR harvest OR harvested OR "per unit effort" OR "days afield" OR encounter* OR sighting* OR stalk* OR shot OR shots))
OR
("hunter inflicted" OR "seen per hunter" OR "observations per hunter" OR "hunter observation*" OR "hunter sighting*" OR "crippling ratio*" OR broadhead*)
OR
(("days afield" OR "hunter-days" OR "hunter days" OR "gun-days" OR "gun days" OR "party-days" OR "hunter-hours") NEAR/10 (harvest* OR kill OR kills OR killed OR success OR successful OR unsuccessful OR bag OR bagged OR "per unit effort"))
OR
(("harvest per unit effort" OR HPUE OR "kill per unit effort" OR "days per kill" OR "days per harvest" OR "hours per kill" OR "effort per kill") NEAR/15 (hunter* OR hunting OR hunted OR "game animal*" OR "wild game" OR wildlife))
OR
((trapper* OR "fur trap*" OR furbearer* OR "fur-bearer*" OR leghold* OR "leg-hold*" OR conibear* OR "body-grip*") NEAR/10 (success OR successful OR efficiency OR "capture rate*" OR "capture success" OR "capture probabilit*" OR "time to death" OR wounded OR escape OR escaped))
OR
(hunter* NEAR/10 ("return rate*" OR "foraging return*" OR "pursuit success" OR "pursuit time" OR "post-encounter" OR "prey choice" OR "diet breadth" OR "hunting ability" OR "hunting skill*" OR "probability of kill*" OR "failure rate*" OR "zero returns"))
OR
("encounter hunting" OR "intercept hunting" OR ("human forager*" NEAR/10 ("return rate*" OR "pursuit success" OR "post-encounter" OR "encounter rate*")))
)
NOT TI=(whaling OR "whale hunt*" OR sealing OR "seal hunt*" OR "marine mammal*" OR "sea turtle*" OR "marine turtle*" OR seabird* OR fishing OR fishery OR fisheries OR angling OR angler* OR spearfishing OR bycatch OR aquaculture OR poach* OR cull* OR falconry)
```

### HT v3 clause counts (pilot run)

Counts are by clause position in the string above.

| Clause | What it captures | Records |
| --: | :-- | --: |
| 1 | `hunter*` within 5 words of success, failure, efficiency, effort or performance words | 718 |
| 2 | "harvest success", "hunt success", "hunting success" within 10 words of a hunter, weapon, licence or game word | 54 |
| 3 | `hunter*` within 10 words of observation, encounter, sighting or search-time words | 28 |
| 4 | `hunter*` within 10 words of stalking, chasing, flight distance or hunting mode words | 121 |
| 5 | `hunter*` within 10 words of wounding, crippling, non-recovery, blood trail or shot-placement words | 109 |
| 6 | Crippling ratio, crippling and wounding rate or loss phrases within 15 words of hunting, shooting or weapon words | 41 |
| 7 | Embedded or shotgun pellet phrases within 15 words of crippling, wounding or hunting words | 41 |
| 8 | Human hunting role phrases (recreational, subsistence, bowhunting, hunting season and similar) within 10 words of success, wounding, kill, harvest or effort words | 939 |
| 9 | Hunter-specific standalone phrases (hunter inflicted, seen per hunter, hunter observation, crippling ratio, broadhead) | 166 |
| 10 | Days afield and hunter-day effort terms within 10 words of a yield term | 16 |
| 11 | Harvest per unit effort and days per kill within 15 words of hunting words | 2 (none relevant) |
| 12 | Trapper and fur-trapping terms within 10 words of success or capture words | 76 |
| 13 | `hunter*` within 10 words of return rate, pursuit success, post-encounter or hunting ability | 45 |
| 14 | "encounter hunting", "intercept hunting", human forager phrases | 9 |
| | **Union (full string)** | **2,076** |

The clause counts sum to 2,365, so about 12 percent of records are retrieved by more than one clause. Clause 8 is the largest single contributor (939) and clause 1 the second (718); these are the two to sample first if precision needs improving. Clause 11 returned two records, none relevant.

The optional category exclusion was not applied in this run:

```
WC=(Economics OR "Agricultural Economics & Policy" OR Business OR Management OR "Hospitality, Leisure, Sport & Tourism" OR "Infectious Diseases" OR Virology OR Microbiology OR Parasitology OR Immunology)
```

Run the final search with and without it, skim about 100 records that only this filter would remove, and apply it only if none are relevant.

## HA v1: human aquatic (candidate)

```
TS=(
((angler* OR angling) NEAR/5 (success OR successful OR unsuccessful OR failure OR efficiency OR "catch rate*" OR "catch per" OR "capture success" OR "hooking success" OR "landing success"))
OR
(("catch rate*" OR "catch per unit effort" OR "catch per angler" OR "fish per hour" OR "angler-hour*" OR "angler hour*" OR CPUE) NEAR/5 (angler* OR angling OR "hook and line" OR "hook-and-line"))
OR
((catchability OR "gear efficiency" OR "capture efficiency" OR "capture probabilit*" OR "probability of capture" OR "capture success" OR "catch success" OR "vulnerability to capture" OR "vulnerability to angling" OR "angling vulnerability") NEAR/10 (angler* OR angling OR fishing OR hook OR hooks OR hooked OR hooking OR bait* OR lure* OR "fishing gear*" OR gear OR longline* OR gillnet* OR "gill net*" OR trawl* OR trap OR traps))
OR
(("hooking success" OR "hooking probabilit*" OR "hooking rate*" OR "hooking efficiency" OR "bite rate*" OR "bite probabilit*" OR "strike rate*" OR "strike probabilit*" OR "contact probabilit*") NEAR/10 (angler* OR angling OR fishing OR hook OR hooks OR hooking OR bait* OR lure* OR gear OR net OR nets OR longline*))
OR
("struck and lost" OR "struck-and-lost" OR "struck but lost" OR "struck-but-lost" OR "hooked and lost" OR "hooked-and-lost")
OR
(("bite-off*" OR "bite off*" OR "escape mortality" OR "unaccounted mortality" OR "unaccounted fishing mortality" OR "dropout mortality" OR "drop-out mortality" OR "escape probabilit*" OR "escape rate*" OR "retention probabilit*" OR "gear escape*" OR "net escape*" OR "landing rate*" OR "landing efficiency") NEAR/10 (angler* OR angling OR fishing OR hook OR hooks OR hooked OR hooking OR gear OR longline* OR gillnet* OR "gill net*" OR trawl* OR net OR nets OR trap OR traps OR pot OR pots))
OR
(landed NEAR/5 (struck OR hooked))
OR
((injur* OR wound* OR scar*) NEAR/5 (hook OR hooks OR hooking OR hooked OR "circle hook*" OR "gill net*" OR gillnet* OR "fishing gear*" OR "fishing line*" OR "net mark*"))
OR
(("injury rate*" OR "injury prevalence" OR "injury frequenc*" OR "wounding rate*" OR "proportion wounded" OR "proportion injured") NEAR/15 (angler* OR angling OR hook OR hooks OR hooking OR hooked OR "catch and release" OR "catch-and-release" OR gillnet* OR "gill net*" OR "fishing gear*" OR "fishing line*"))
OR
((whaling OR "whale hunt*" OR "seal hunt*" OR "walrus hunt*" OR "marine mammal hunt*" OR "marine mammal harvest*") NEAR/15 (struck OR landed OR lost OR efficiency OR success OR successful OR wounded OR retrieved OR retrieval OR recovered))
)
NOT TI=(aquaculture OR poach* OR cull* OR falconry OR bycatch OR discard*)
```

| Clause | What it captures |
| --: | :-- |
| 1 | Angler success, catch rate, hooking and landing success |
| 2 | Catch per unit effort and angling catch rates, tied to angling words |
| 3 | Catchability, gear efficiency, capture probability, vulnerability to capture (most likely source of volume; restrict to angling words if the count is too large) |
| 4 | Hooking success, bite and strike rates, contact probability |
| 5 | Struck-and-lost and hooked-and-lost phrases |
| 6 | Escape, retention, landing and dropout phrases near fishing or gear words |
| 7 | Landed near struck or hooked |
| 8 | Injury, wound or scar near hook, gill net or fishing line words |
| 9 | Injury rate, injury prevalence, proportion wounded near angling or gear words |
| 10 | Whaling and marine mammal hunt outcomes |

## Natural predator core v3 (shared by NT and NA, candidate)

```
TS=(
(("hunting success" OR "hunt success" OR "predation success" OR "predatory success" OR "attack success" OR "strike success" OR "kill success" OR "pursuit success" OR "chase success" OR "successful hunt*" OR "unsuccessful hunt*" OR "failed hunt*" OR "hunting attempt*" OR "hunting bout*" OR "kill attempt*" OR "attack attempt*") NEAR/15 (prey OR predator* OR predation OR predatory OR carnivor* OR raptor*))
OR
("prey capture success" OR "prey capture rate*" OR "prey capture probabilit*" OR "prey capture efficiency" OR "predation attempt*" OR "attempted predation" OR "predatory strike*" OR "prey pursuit*")
OR
(("observed hunt*" OR "observed daytime hunt*" OR "observed kill*" OR "observed predation event*") NEAR/15 (prey OR predator* OR carnivor* OR raptor*))
OR
(("capture success" OR "foraging success" OR "feeding success" OR "foraging performance" OR "capture probabilit*" OR "capture rate*") NEAR/10 (attack* OR pursuit* OR strike* OR chase* OR dive OR dives OR diving OR plunge* OR stalk* OR hunt OR hunts OR hunted OR hunting))
OR
(("prey capture" OR "prey capture attempt*") NEAR/10 (attack* OR success OR successful OR unsuccessful OR attempt* OR failure OR kill* OR pursuit*))
OR
(("predatory attack*" OR "predatory strike*" OR "prey attack*" OR "predator attack*" OR "attacks on prey") NEAR/5 (success OR successful OR unsuccessful OR outcome* OR failure OR failed))
OR
(("attack strateg*" OR "attack tactic*") NEAR/10 (prey OR predator* OR raptor* OR carnivor*))
OR
(("hunting strateg*" OR "hunting tactic*" OR "hunting mode*") NEAR/15 (prey OR predator* OR carnivor* OR raptor*))
OR
((stalk OR stalks OR stalked OR stalking) NEAR/3 (chase OR chases OR chased OR chasing))
OR
((chase OR chases OR chased OR chasing OR pursuit OR pursuits) NEAR/15 (kill OR kills OR killed OR killing OR "kill rate*" OR hunt OR hunts OR hunting))
OR
(("hunting behavio*" OR "predatory behavio*") NEAR/15 (attack* OR success OR successful OR strike* OR kill* OR capture* OR pursuit* OR "prey encounter*" OR "hunting effort"))
OR
(("prey encounter*" OR "encounter rate*") NEAR/10 (strike* OR attack* OR pursuit* OR hunt OR hunts OR hunting OR capture*))
OR
((attack OR attacks) NEAR/10 (predation OR predations OR predatory OR predator*))
OR
(("predator attacks" OR "successive attacks" OR "predator attack*") NEAR/15 (school* OR shoal* OR "bait ball*"))
OR
(("animal borne" OR "animal-borne" OR accelerometer* OR biologg*) NEAR/15 (predation OR "prey capture" OR hunt OR hunts OR hunting OR attack* OR chase* OR kill OR kills OR "foraging attempt*" OR "capture attempt*"))
OR
((injur* OR wound* OR scar*) NEAR/5 (predator* OR predation OR "predatory attack*" OR "shark bite*" OR "bite mark*" OR "bite scar*" OR "tooth rake*"))
OR
((injur* OR wound*) NEAR/10 ("without eating" OR "without consuming" OR "without ingesting" OR uneaten))
)
```

### NT: natural terrestrial

```
(#CORE) NOT TI=(marine OR ocean* OR sea OR underwater OR dive OR dives OR diving OR plunge* OR pelagic OR reef* OR seabird* OR shark* OR whale* OR cetacean* OR pinniped* OR piscivor* OR "fish school*" OR insect* OR arthropod* OR spider* OR arachnid* OR beetle* OR wasp* OR mantis OR mantid* OR ladybird* OR parasitoid* OR nematode* OR mite OR mites OR copepod* OR zooplankton OR dragonfl* OR hoverfl* OR lacewing* OR larva* OR ant OR ants)
```

### NA: natural aquatic

```
((#CORE) AND TS=(dive OR dives OR diving OR underwater OR plunge* OR pelagic OR marine OR ocean* OR sea OR reef* OR seabird* OR shark* OR whale* OR cetacean* OR pinniped* OR piscivor* OR "fish school*" OR "schooling fish*" OR "bait ball*" OR "fish prey" OR "prey fish" OR fish)) NOT TI=(insect* OR arthropod* OR spider* OR arachnid* OR beetle* OR wasp* OR mantis OR mantid* OR ladybird* OR parasitoid* OR nematode* OR mite OR mites OR copepod* OR zooplankton OR dragonfl* OR hoverfl* OR lacewing* OR larva* OR ant OR ants)
```

Complete single-line versions with the core written in are provided as `NT_v3_full_query.txt` and `NA_v3_full_query.txt`.

## Regression searches (from the known studies list)

Combine each module's string with its DOI search using AND. All retrieved records should be returned.

```
HT:  DO=(10.1002/jwmg.22638 OR 10.1071/WR24114 OR 10.2981/wlb.1999.022 OR 10.1186/s40462-024-00471-z OR 10.1002/wsb.1414 OR 10.1002/jwmg.22107 OR 10.1016/j.ecolind.2017.05.044 OR 10.2193/2006-108)
HA:  DO=(10.1080/02755947.2015.1120833 OR 10.1577/M06-035.1 OR 10.14430/arctic1310 OR 10.1093/icesjms/fsaa205)
NT:  DO=(10.1111/1365-2435.13318 OR 10.1038/ncomms11034 OR 10.1016/j.anbehav.2012.04.029 OR 10.1016/j.anbehav.2012.06.027 OR 10.3389/fevo.2024.1465094 OR 10.2307/3803048)
NA:  DO=(10.1016/j.beproc.2013.04.012 OR 10.1007/s00227-005-0130-2 OR 10.1111/1365-2656.12455 OR 10.1111/j.1748-7692.2005.tb01254.x OR 10.1017/S002531540501218X)
```

Negative test for HT (must return zero when combined with the HT string using AND):

```
UT=(WOS:000624388100001 OR WOS:000477911000008 OR WOS:001771298500001)
```

## Change log

| Date | Change |
| :-- | :-- |
| 26 Oct 2026 | First draft: two blocks joined by AND, species-agnostic, terrestrial and aquatic together. |
| 9 Nov 2026 | Module structure (HT, HA). Phrases removed from both blocks; context lists limited to human roles. |
| 13 Nov 2026 | Interim v2: snare terms removed, forager anchor removed, generic phrases tied to hunting words. |
| 14 Nov 2026 | HT v3: built from the known studies list. Added harvest success, observation rate, hunting mode, crippling ratio and embedded pellet clauses. HA v1 and natural predator core v3 drafted. |
| Nov 2026 | HT v3 pilot run: 2,076 records, sample DOIs retrieved. |
