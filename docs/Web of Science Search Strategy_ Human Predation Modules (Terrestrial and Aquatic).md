# Web of Science Search Strategy: Human and Natural Predation (Terrestrial and Aquatic)

Version of 16 November 2026. This document replaces the "Human Predation Modules (Terrestrial and Aquatic)" strategy of 9 November 2026 and all earlier drafts. The strings themselves are in `search_strings.md`.

## 1. Purpose and scope

The project compares how often human and natural predators succeed at each stage of the predation sequence, on land and in water. It runs as four Web of Science searches:

- **HT**: human terrestrial (hunting and trapping)
- **HA**: human aquatic (fishing and marine hunting)
- **NT**: natural predators, terrestrial
- **NA**: natural predators, aquatic

Four modules are used because the vocabulary differs by predator type (hunter, harvest, wounding loss against predator, kill rate, attack success) and by realm (rifle and trapper against hook, gear and struck-and-lost). Separate modules can be counted, tested and tuned independently. Records are deduplicated across modules and keep a record of which modules found them, so human-versus-natural and terrestrial-versus-aquatic comparisons come from the tags.

Scope decisions:

- Prey are wild vertebrates. Invertebrate prey and farmed or domestic animals are handled at screening by the eligibility rule, not by search terms, so that the search stays sensitive.
- HT uses no species names. Habitat-group words (whale, seal, seabird, shark and similar) are used only where needed to separate a realm, and kept to the fewest that work.
- Management culling, poaching and falconry are out of scope. Records on them that the search captures are removed at screening.
- Date, language, species, geography and study design are applied at screening.
- Success measures of interest are stage-specific (encounter, pursuit or attack, capture or kill, loss, retrieval) and overall, with a denominator such as per encounter, attempt, shot, hunter day or unit effort.

## 2. Module status

| Module | String version | Status | Evidence |
| :-- | :-- | :-- | :-- |
| HT | v3 | Run in Web of Science: 2,076 records | Sample DOIs from the known studies list were all retrieved. Per-clause counts below. |
| HA | v1 | Candidate, not yet run | Local logic check: 8 of 8 known studies on title and note text |
| NT | v3 | Candidate, not yet run | Local logic check: 8 of 9 |
| NA | v3 | Candidate, not yet run | Local logic check: 9 of 9 |

The local logic check is an approximation made with a small script (`wos_query_check.py`). It has no true Web of Science lemmatization and simplifies the proximity operator, and it used titles and short notes where abstracts were not available. It shows that syntax and logic behave as intended, not that recall is high. Web of Science regression searches are the real test.

## 3. Stage framework

The stages follow the predation sequence of encounter, detection, identification, approach, subjugation and consumption (Endler 1991, as set out in Hamalainen et al. 2022). For fishing, the capture process is encounter, contact and retention (Spence et al.), with vulnerability to capture and catchability as summary properties (Lennox et al. 2017).

| Stage | Human terrestrial (HT) | Human aquatic (HA) | Natural predators (NT, NA) |
| :-- | :-- | :-- | :-- |
| Search, encounter | Animals seen per hunter day, encounter rate, search time | Gear encounter probability | Prey encounter rate |
| Approach, pursuit | Stalking, chasing, pursuit success, flight distance | Bite and strike rate, hooking success, contact probability | Stalk, chase, pursuit, hunting bouts |
| Subjugation, capture | Shot opportunity, hit and kill probability, shot placement | Hooking, capture probability | Attack success, strike success, prey capture success |
| Escape, loss | Wounding and crippling, non-recovery, embedded pellets | Struck and lost, gear injury, bite-off, escape mortality | Prey injured but not eaten, bite scars |
| Overall outcome, effort | Hunter success, harvest success, days per kill, return rates | Angler success, catch rate, catchability | Hunting success, foraging success, kill after chase |

## 4. How the strings were developed

The early strings were written from memory and judged by one number, the final record count, with no test set of known papers and no check of individual terms. A first single-string version returned about 1.4 million records, and a later version added snare terms that retrieved papers on Socrates, economics and giraffe injuries. The strings were rebuilt using the objective approach to search development (Hausner et al. 2012, 2015, 2016), which starts from a test set of known relevant papers, derives terms from those papers, and checks the strategy against them. In a prospective comparison, that approach reached a weighted mean sensitivity of 97 percent with 5 percent precision, against 75 and 4 percent for a conceptual approach. Low precision is therefore expected and is handled by screening.

What has been done:

1. A known studies list was assembled (about nine usable human terrestrial papers, plus human aquatic and natural predator papers).
2. Vocabulary was checked against the literature behind those papers and against fisheries, anthropology and wounding-rate sources (see section 9).
3. Each outcome term was tied to a hunting, fishing or predation context by proximity, and every term was traced to a known study or marked as domain knowledge.
4. Strings were checked locally against known studies and against noise records built from reported false positives.
5. HT v3 was run in Web of Science and checked against sample DOIs.

What remains: running HA, NT and NA, estimating recall on a larger and independent test set, and sampling precision.

### Design rules in force

- **Anchor on the actor or the predation context.** Each outcome term sits near a hunter, fishing, prey or predator word. There is no record-level AND between a broad actor block and a broad outcome block. The earlier two-block design let a hunting term in one sentence satisfy the outcome in an unrelated sentence.
- **No phrase does both jobs.** If "hunting success" were in both blocks, any paper using it, including natural predator papers, would pass on that phrase alone.
- **Generic words need a context word nearby.** `detect*`, `encounter*`, wound, shot, success, catchability and "attack success" count only within three to fifteen words of an actor, gear, prey or predator word. Attack success also means adversarial machine-learning attacks, and "threat hunting" is a cybersecurity term.
- **Context words must name a human role.** People, human and dog are not accepted as hunting context, because natural predators hunt near people.
- **Measurement language.** Effort terms such as hunter days count only beside a harvest, kill or success term.
- **Unquoted hyphenated terms are avoided.** Hyphenated phrases are quoted.
- **Loose gear words stay out.** Snare terms were removed from HT because they matched unrelated papers.
- **Exclusions are last, narrow and tested.** A title-only exclusion removes aquatic words from terrestrial modules and invertebrate group words from natural modules. A category exclusion (X2) is optional and not applied by default.

## 5. Module HT: results of the pilot run

Full string and clause list are in `search_strings.md`. The pilot run returned 2,076 records for the full string.

| Clause | Records |
| --: | --: |
| 1 hunter near success, effort, performance | 718 |
| 2 harvest or hunting success phrases | 54 |
| 3 hunter near observation or encounter | 28 |
| 4 hunter near stalking, chasing, hunting mode | 121 |
| 5 hunter near wounding, non-recovery | 109 |
| 6 crippling and wounding phrases | 41 |
| 7 embedded pellets | 41 |
| 8 human role phrases near outcome words | 939 |
| 9 hunter-specific standalone phrases | 166 |
| 10 days afield and hunter days with yield | 16 |
| 11 harvest per unit effort, days per kill | 2 (none relevant) |
| 12 trapping near success or capture | 76 |
| 13 hunter near return rate, pursuit success | 45 |
| 14 encounter hunting, human foragers | 9 |
| **Union** | **2,076** |

Observations:

- The result is a screenable set, in contrast with the 1.4 million of the earliest version.
- Clause counts sum to 2,365, so about 12 percent of records come from more than one clause.
- Clauses 8 and 1 supply about 70 percent of the summed count. They are the first to sample if precision needs work.
- Clause 11 returned two records and none were relevant. It can be dropped in a future version without affecting recall on the known studies.
- The exclusions applied were the title-only terms in the string. The category exclusion X2 was not applied.

Limits of the validation: the sample DOIs tested were all retrieved, but the known studies list holds too few human terrestrial papers to split into development, validation and unseen sets (the protocol aims for 45 to 60), so no unbiased recall figure exists yet. Several known papers may not be indexed in Web of Science at all (for example agency conference proceedings), and no string can retrieve those.

## 6. Modules HA, NT and NA: candidates

HA covers fishing success and capture-process terms (angler success, catch rate, catchability, hooking, struck-and-lost, escape, gear injury) and marine mammal hunt outcomes. NT and NA share one core of predation-stage phrases (hunting success, predation success, prey capture, chase then kill, attack outcomes, animal-borne video and accelerometer studies, injury of prey by predators) tied to prey or predator words. NT removes aquatic and invertebrate titles. NA requires aquatic context and removes invertebrate titles.

Before these are treated as final:

1. Run every clause of each module alone and record the count. A clause with tens of thousands of records is the one to tighten.
2. Run the DOI regression searches in `search_strings.md` for each module.
3. Collect real negative records for each module and confirm they are not retrieved.
4. If a module is too large, tighten in this order: restrict HA clause 3 (catchability) to angling words; require a prey or predator word near feeding, foraging and capture success in the natural core (clause 4); drop the generic attack-near-predation clause (clause 13); reduce NEAR distances.

## 7. Decisions

| Decision | Outcome |
| :-- | :-- |
| Aebischer et al. 2014 (wounding rate in deer stalkers, routine culling) | The search may capture it. Screening removes it if judged out of scope. |
| Embedded shotgun pellet counts in live birds | Count as a wounding metric (Clausen et al. 2017 crippling ratio). |
| Bycatch and discard titles in HA | Excluded. Non-target capture is not predation success. |
| Taxon-group words | Used only where needed to separate a realm, and kept to the fewest that work. |
| Invertebrate gear and invertebrate prey | Handled at screening by the wild vertebrate prey rule. |
| Category exclusion X2 | Pending. Run the search with and without it, skim about 100 records that only X2 removes, and apply it only if none are relevant. |
| Hooking and release mortality alone | Not searched; it describes survival after capture. Injury from gear is searched. |
| Giraffe and other wildlife snare wounding | Open: poaching is out of scope, but the known studies list tags two such records as natural terrestrial. |
| Natural predator injury clauses (bite scars, tooth rakes, injure without eating) | Included in the core. Confirm they match the intended scope. |

## 8. Problems found in the known studies list

- Wrong bibliographic details: "Hunter movement and habitat use affect observation rate of white-tailed deer" is by Meier et al., Wildlife Research 52 (2025). "Hunting mode and habitat selection mediate the success of human hunters" is by Gaynor et al., Movement Ecology 12 (2024), DOI 10.1186/s40462-024-00471-z. Several other rows carry the author list of a 1998 Ditchkoff paper, which looks like a copy error.
- Two different Rowland papers are mixed: Rowland et al. 2021 (J Wildl Manage 85, DOI 10.1002/jwmg.22107) and Rowland et al. 2023 (Wildl Soc Bull, DOI 10.1002/wsb.1414).
- Clausen et al. 2017 is "Crippling ratio: a novel approach to assess hunting-induced wounding of wild animals", Ecological Indicators 80: 242-246.
- Many local file rows are only a label and a rate, with no title or DOI, so they cannot be searched.
- Module labels are inconsistent: some natural predator records sit in HA, and some human hunting records sit in NT.
- Authors for "Linking angling catch rates and fish learning under catch-and-release regulations" are listed as Meka and should be checked against DOI 10.1577/M06-035.1.

## 9. Term provenance

"Checked" means the term or concept was found in the literature behind the known studies or in sources read during development. "Domain knowledge" means standard terminology not re-checked, to be confirmed with the test set.

| Terms | Evidence | Status |
| :-- | :-- | :-- |
| animals seen per hunter day, hunter observation, observation rate | Ericsson and Wallin (1999); Meier et al. (2025) | Checked |
| harvest success, successful and unsuccessful hunters, hunting mode, hunter effort | Gaynor et al. (2024); Ontario moose harvest success and hunter effort (2023); Rowland et al. (2021, 2023) | Checked |
| wounding rate and loss, crippling rate and loss, crippling ratio, embedded pellets, non-recovery, hunter inflicted wounding | Wounding-rate studies of archery and firearm hunting; Clausen et al. (2017); Madsen and Riget (2007) | Checked |
| post-encounter return rate, pursuit success, probability of kill upon encounter, hunting ability | Anthropological papers on the Ache, Hadza and Martu | Checked |
| struck-and-lost, struck-but-lost | Fay et al. (1994); Greenland walrus hunt studies | Checked |
| encounter, contact, retention, catchability, vulnerability to capture, bite-off | Spence et al.; Lennox et al. (2017) | Checked |
| hunting success, prey capture success, foraging success, strike and attack success, animal-borne video | Natural predator papers in the known studies list (cheetah, wild dog, rattlesnake, gannet, fur seal, white shark and others) | Checked against titles and notes |
| days afield, gun-days, party-days, harvest per unit effort, broadhead, blood trail | Wildlife-agency and bowhunting terminology | Domain knowledge |
| hooking success, escape mortality, unaccounted mortality, dropout mortality, landing success | Standard fisheries terminology | Domain knowledge |

## 10. Gaps considered and left out

- Vulnerability to harvest and selectivity: describe which animals are taken, not how often a hunt succeeds.
- Hunter satisfaction and motivation: a large literature mostly outside the research question.
- Harvest and exploitation rates: population-level fractions, not stage success. Darimont et al. (2015) is a context record, not a test record for the stage clauses.
- Hunting papers with no hunter word: partly caught by the role phrases; the test set is the check for the rest.
- Archaeological hunting and natural predator comparisons that reach HT: handled at screening, and natural predator records are duplicated by NT and removed when modules are pooled.
- Commercial fishing catchability: included in HA clause 3, flagged as the likeliest source of volume.

## 11. Downstream workflow

1. **Run and record.** Run each clause and the full string for each module. Record counts, dates and strings.
2. **Export.** In Web of Science, Export, Tab delimited file, Record Content: Full Record, in batches of up to 1,000 records. Do not use Fast 5K for screening because it lacks abstracts. Put each module in its own folder (`data/HT`, `data/HA`, `data/NT`, `data/NA`).
3. **Merge and deduplicate.** `merge_wos_exports.py` removes duplicates across modules by accession number, then DOI, then title and year, keeps a `modules` column (for example `HT|NT`), assigns each record to one screening project, and writes one CSV per module for ASReview.
4. **Screen in ASReview, one project per module.** Per-module projects give each search its own stopping rule and recall check. Records found by both a human and a natural module are likely direct comparisons and are tagged for attention.
5. **Prior knowledge and stopping.** Use relevant records from the known studies list and the reported false positives as priors. Hold back part of the list as a key-paper check. Fix the stopping rule before screening; the SAFE procedure combines a minimum share screened, a run of consecutive irrelevant records, a recall plot check and a key-paper check (Boetje and van de Schoot 2024).
6. **Eligibility (proposal).** Relevant: reports or likely reports a quantitative success or failure measure at one or more stages, with a denominator, by a human or non-human vertebrate predator on wild vertebrate prey. Irrelevant: domestic, farmed or invertebrate prey; no success measure (attitudes, economics, disease, regulation); only population-level exploitation rates; simulation without empirical data. When unsure at title and abstract, label relevant.
7. **Tags at screening.** Realm, predator (human, natural, both), stage reported, measure type, and flags (review, no abstract, needs full text).

Helper scripts: `merge_wos_exports.py`, `harvest_terms.py` (term mining from a development set), `wos_query_check.py` (local approximate checker).

## 12. Validation protocol going forward

1. Extend the test list to 45 to 60 papers per module by pearl growing (cited references, citing articles and Related Records of the strongest known studies).
2. Split into development, validation and unseen sets. Choose terms from the development set only, tune on the validation set, and open the unseen set once.
3. Audit each new term on its own: run it alone, run it AND the test set, scan the first 20 to 30 results, then keep, anchor or drop.
4. After every change, record total records, positives retrieved and negatives retrieved in a version log. Change one group of terms per version.
5. Sample 100 to 200 random records per module, label them, and attribute each false positive to the clause that retrieved it.
6. Report per PRISMA-S and consider a PRESS review by a librarian.

## 13. Version history

| Date | Version | Change |
| :-- | :-- | :-- |
| 26 Oct 2026 | Draft | Two broad blocks joined by AND; terrestrial and aquatic together |
| 9 Nov 2026 | Module draft | Four-module structure; context lists limited to human roles; unsupported terms removed |
| 13 Nov 2026 | HT v2 (interim) | Snare and forager terms removed; generic phrases anchored |
| 14 Nov 2026 | HT v3, HA v1, natural core v3 | Rebuilt from known studies list; inline-anchored clauses |
| Nov 2026 | HT v3 pilot | 2,076 records; sample DOIs retrieved |

## References

- Boetje J, van de Schoot R (2024). The SAFE procedure: a practical stopping heuristic for active learning-based screening in systematic reviews and meta-analyses. Systematic Reviews 13: 81. doi:10.1186/s13643-024-02502-7
- Clausen KK, Holm TE, Haugaard L, Madsen J (2017). Crippling ratio: a novel approach to assess hunting-induced wounding of wild animals. Ecological Indicators 80: 242-246. doi:10.1016/j.ecolind.2017.05.044
- Darimont CT, Fox CH, Bryan HM, Reimchen TE (2015). The unique ecology of human predators. Science 349(6250): 858-860. doi:10.1126/science.aac4249
- Endler JA (1991). Interactions between predators and prey. In: Behavioural Ecology: An Evolutionary Approach, 3rd edition.
- Ericsson G, Wallin K (1999). Hunter observations as an index of moose Alces alces population parameters. Wildlife Biology 5(3): 177-185. doi:10.2981/wlb.1999.022
- Fay FH, Burns JJ, Stoker SW, Grundy JS (1994). The struck-and-lost factor in Alaskan walrus harvests, 1952-1972. Arctic 47(4): 368-373. doi:10.14430/arctic1310
- Gaynor KM, McInturff A, Abrahms BL, Smith AM, Brashares JS (2024). Hunting mode and habitat selection mediate the success of human hunters. Movement Ecology 12: 29. doi:10.1186/s40462-024-00471-z
- Grames EM, Stillman AN, Tingley MW, Elphick CS (2019). An automated approach to identifying search terms for systematic reviews using keyword co-occurrence networks. Methods in Ecology and Evolution. doi:10.1111/2041-210X.13268
- Hamalainen L, Rowland HM, Mappes J, Thorogood R (2022). Social information use by predators: expanding the information ecology of prey defences. Oikos 2022(10): e08743. doi:10.1111/oik.08743
- Hausner E, Waffenschmidt S, Kaiser T, Simon M (2012). Routine development of objectively derived search strategies. Systematic Reviews 1: 19.
- Hausner E, Guddat C, Hermanns T, Lampert U, Waffenschmidt S (2015). Development of search strategies for systematic reviews: validation showed the noninferiority of the objective approach. Journal of Clinical Epidemiology 68(2): 191-199.
- Hausner E, Guddat C, Hermanns T, Lampert U, Waffenschmidt S (2016). Prospective comparison of search strategies for systematic reviews: an objective approach yielded higher sensitivity than a conceptual one. Journal of Clinical Epidemiology 77: 118-124.
- Lennox RJ, Alos J, Arlinghaus R, Horodysky A, Klefoth T, Monk CT, Cooke SJ (2017). What makes fish vulnerable to capture by hooks? A conceptual framework and a review of key determinants. Fish and Fisheries. doi:10.1111/faf.12219
- Livoreil B, Glanville J, Haddaway NR, et al. (2017). Systematic searching for environmental evidence using multiple tools and sources. Environmental Evidence 6: 23. doi:10.1186/s13750-017-0099-6
- Madsen J, Riget F (2007). Do embedded shotgun pellets have a chronic effect on body condition of pink-footed geese? Journal of Wildlife Management. doi:10.2193/2006-108
- Meier AN, Little AR, Gee KL, Demarais S, Webb SL, Ranglack DH (2025). Hunter movement and habitat use affect observation rate of white-tailed deer (Odocoileus virginianus). Wildlife Research 52: WR24114. doi:10.1071/WR24114
- Rowland MM, et al. (2021). Influence of landscape characteristics on hunter space use and success. Journal of Wildlife Management 85: 1394-1409. doi:10.1002/jwmg.22107
- Spence MA, Pace MC, Minto C, Bartos TIJ, Dolder PJ. A process-based theory of fishing. Natural Resource Modeling. doi:10.1111/nrm.70040
- van de Schoot R, de Bruin J, Schram R, et al. (2021). An open source machine learning framework for efficient and transparent systematic reviews. Nature Machine Intelligence 3: 125-133. doi:10.1038/s42256-020-00287-7
