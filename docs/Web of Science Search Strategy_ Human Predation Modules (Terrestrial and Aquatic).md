# **Web of Science Search Strategy: Human Predation Modules (Terrestrial and Aquatic)**

Web of Science Core Collection, Advanced Search. Final version of 9 November 2026\. It replaces the terrestrial draft of the same date and the draft of 26 October 2026\.

## **Purpose and scope**

The project compares how often human and natural predators succeed at each stage of the predation sequence, on land and in water. It runs as four Web of Science searches: human-terrestrial (HT), human-aquatic (HA), natural-terrestrial (NT) and natural-aquatic (NA). This document gives the final strings for the two human modules. NT and NA follow, built on the same stage framework.  
Four modules are used because the vocabulary differs by predator type (hunter, harvest, wounding loss against predator, kill rate, attack success) and by realm (rifle, trapper, shot against hook, gear, struck and lost). Separate modules can be counted, sentinel-tested and tuned independently. All four are pooled into ASReview with a module tag, so the human-versus-natural and terrestrial-versus-aquatic comparisons come from the tags.  
Scope decisions: prey are wild vertebrates. HT uses no species names. HA uses habitat-group words (whale, seal, seabird and similar) only inside the marine hunting set, because that is the only way to separate marine hunting from fishing. Management culling, poaching and falconry are out of scope. Date, language, species, geography and study design are applied at screening. The TS field (title, abstract, author keywords, Keywords Plus) is searched. The measure of a good search is the quality of its terms and its tested recall, not the number of records.

## **Stage framework**

The stages follow the predation sequence of encounter, detection, identification, approach, subjugation and consumption (Endler 1991, as set out in Hämäläinen et al. 2022). For fishing, the equivalent is the capture process of encounter, contact and retention (Spence et al.), with vulnerability to capture and catchability as the summary properties (Lennox et al. 2017). Each Block B set targets one or more stages.

| Stage | Human terrestrial measure | Human aquatic measure | Sets |
| :---- | :---- | :---- | :---- |
| Search, encounter, detection | Animals seen per hunter day, encounter rate, search time | Gear encounter probability, search time | HT-B1, HA-B1 |
| Approach and pursuit | Stalking, chasing, pursuit success, flight distance, hunting attempts | Bite and strike rate, contact probability, hooking success | HT-B2, HA-B2 |
| Subjugation | Shot opportunity, hit and kill probability, shot placement | Hooking, capture probability | HT-B3, HA-B2, HA-B4 |
| Escape and loss | Wounding and crippling loss, non-recovery | Struck and lost, bite-off, escape mortality | HT-B4, HA-B3 |
| Overall outcome and effort | Hunter success, days per kill, harvest per unit effort, return rates | Angling success, catch rate, gear efficiency, catchability | HT-B5, HA-B4 |

## **Design rules**

> * **Anchor on the human actor.** Block A names a person hunting or fishing. Block B names a stage or outcome measure.  
> * **No term does both jobs.** A phrase sits in one block only. If "hunting success" sat in both, any paper using it would pass the whole search alone, including papers on natural predators.  
> * **Generic words need a hunting or fishing word nearby.** detect\*, encounter\*, wound, shot, success and catchability count only within three to fifteen words of an actor or gear term.  
> * **Context words must name a human role.** A word such as people or human is not accepted as context, because natural predators also hunt near people.  
> * **Block B uses measurement language.** Effort terms such as hunter days count only beside a harvest, kill or success term.  
> * **Exclusions are last, narrow and tested.** They are applied by title or WoS category and checked against the sentinel set before use.

## **Why the earlier string let these records through**

I cannot see which term matched each record. The routes below are the ones the old string allowed, and each has been closed. To confirm, run each set in Web of Science and combine it with the record, for example \#4 AND UT=WOS:000624388100001, so that each false positive is attributed to a set. The attribution also tells you which set to tighten if a similar record appears later.

| Record | Likely route | Fix |
| :---- | :---- | :---- |
| Barn owl movement ecology, breeding, diet and roosting | A natural predator. The old A2 accepted human or people within five words of hunting, so a sentence about owls hunting near people satisfied Block A. | A2 now needs a human role word (licence, quota, firearm, subsistence and similar). People, human and dog are removed from it. |
| Hunting practices and disease transmission between community dogs and wild dogs | Human hunting, but the outcome is disease. The old B1 counted detect\* within five words of hunting, which matches pathogen detection in hunting dogs. | detect\* is removed. Only detection probability within ten words of a hunting term counts. X2 removes infectious disease categories. |
| Economic impacts of chronic wasting disease from a deer hunter survey | A social science survey. The old B5 counted hunter days and per hunting trip on their own, which appear in expenditure surveys, and "hunting trip" also sat in A1. | Effort terms now need a harvest, kill or success term within ten words. "Hunting trip" left A1. X2 removes economics and business categories. |

## **Module HT: human terrestrial**

### **HT-A1. Phrases that describe people hunting**

TS=(hunter\* OR "human predat\*" OR "human hunt\*" OR "recreational hunt\*" OR "sport hunt\*" OR "subsistence hunt\*" OR "traditional hunt\*" OR "customary hunt\*" OR "trophy hunt\*" OR "commercial hunt\*" OR "legal hunt\*" OR "regulated hunt\*" OR "hunting licen\*" OR "hunting permit\*" OR "hunting regulation\*" OR "hunting quota\*" OR "hunting season\*" OR bowhunt\* OR "bow hunt\*" OR "archery hunt\*" OR "persistence hunt\*" OR "spot and stalk" OR "still hunt\*" OR "stand hunt\*" OR "drive hunt\*" OR "driven hunt\*" OR "hound hunt\*" OR "hunting with dogs" OR bushmeat OR "wild meat")  
**Why.** Every phrase is specific to people hunting, so none needs a proximity condition. hunter\* stays because wildlife-agency and hunter-gatherer papers depend on it, and it also matches hunter-gatherer. Known noise: Hunter syndrome, Hunter Valley, and natural predators described as ambush or pursuit hunters. Hunting pressure, hunting trip and hunting return are not here because they are effort or exposure terms, which belong in Block B or nowhere.

### **HT-A2. Generic hunting words with a human role**

TS=((hunt OR hunts OR hunted OR hunting) NEAR/5 (villager\* OR indigenous OR aboriginal OR "first nations" OR inuit OR "native american\*" OR subsistence OR recreational OR sport OR sports OR traditional OR customary OR trophy OR licen\* OR permit\* OR quota\* OR regulated OR firearm\* OR rifle\* OR shotgun\* OR muzzleloader\* OR archery OR crossbow\* OR arrow\* OR spear\* OR snare\* OR hound\* OR "game animal\*" OR "wild game"))  
**Why.** This catches papers that describe hunting without a phrase from A1. hunt\* is written as four words because it also matches Huntington's disease and huntingtin. The context list contains only roles, weapons and regulatory words that belong to people. Human, people, dog, bow, wildlife, vertebrate\* and quarry are left out because predators hunt near people, hunt wildlife and vertebrates, and the other words have unrelated meanings.

### **HT-A3. Harvest and kill language**

TS=((harvest\* NEAR/3 (hunter\* OR hunting OR "game animal\*" OR "wild game" OR wildlife OR "wild animal\*" OR "wild meat" OR bushmeat OR "game species")) OR "game harvest\*" OR (("harvest survey\*" OR "harvest report\*" OR "harvest record\*" OR "human harvest\*" OR "subsistence harvest\*") NEAR/10 (hunt OR hunts OR hunted OR hunting OR hunter\* OR wildlife OR "game animal\*" OR "wild game" OR bushmeat OR "wild meat")) OR ((kill OR kills OR killed OR killing) NEAR/3 (hunter\* OR hunting OR "game animal\*" OR "wild game" OR bushmeat OR "wild meat")))  
**Why.** Wildlife agencies say harvest where other papers say hunt. A bare harvest\* would pull in crop, energy and tissue harvest. Kill terms are tied to hunting words because killed near wildlife matches roadkill and turbine fatality studies. Subsistence and human harvest need a hunting or wildlife word nearby because both also describe plant and fish harvest.

### **HT-A4. Fur trapping and snaring**

TS=(trapper\* OR "fur trap\*" OR "fur harvest\*" OR furbearer\* OR "fur-bearer\*" OR leghold\* OR "leg-hold\*" OR conibear\* OR "body-grip\*" OR ((snare OR snares OR snaring OR snared) NEAR/5 (wire OR wildlife OR bushmeat OR "wild animal\*" OR "wild meat" OR villager\* OR "game animal\*" OR hunt OR hunts OR hunted OR hunting OR hunter\*)))  
**Why.** Trapping and snaring are human predation with their own success and loss stages. Generic trap\* is excluded because it matches research live-trapping, camera, insect and ion traps. Snare is restricted because SNARE proteins would otherwise dominate.

### **HT-A5. Human foraging anthropology**

TS=(("human forag\*" NEAR/10 (hunt OR hunts OR hunted OR hunting OR hunter\* OR "game animal\*" OR "wild game" OR prey)) OR (("foraging return\*" OR "post-encounter" OR postencounter OR "on-encounter" OR "central place") NEAR/10 (hunter\* OR forager\* OR hunting)) OR (("optimal foraging" OR "prey choice" OR "diet breadth") NEAR/10 (hunter\* OR forager\* OR human OR humans OR people)) OR "encounter hunting" OR "intercept hunting")  
**Why.** Studies of hunter-gatherers report encounter rates, pursuit success and post-encounter return rates by stage. The vocabulary was checked against anthropological papers on the Ache, Hadza and Martu (see Term provenance). human\* is replaced by human and humans because the wildcard matches humane. Human foraging must sit near a hunting word because it also names psychology experiments.

### **HT-B1. Search and encounter**

TS=("seen per hunter" OR "observations per hunter" OR "hunter observation\*" OR "hunter sighting\*" OR "game seen" OR ("prey encounter\*" NEAR/10 (hunter\* OR forager\*)) OR (("observation rate\*" OR "encounter rate\*" OR "encounter probabilit\*" OR "encounter frequenc\*" OR "time to encounter" OR "search time" OR "search effort" OR "sighting rate\*" OR "sightings per" OR "animals seen" OR "detection probabilit\*") NEAR/10 (hunter\* OR hunting OR hunted)))  
**Why.** Hunter observation papers measure animals seen per hunter day, an encounter-stage rate (Ericsson and Wallin 1999). Those phrases are hunter-specific and stand alone. Detection probability, encounter rate and search time are core survey-ecology terms, so they count only within ten words of a hunting term. The generic detect\* is removed.

### **HT-B2. Approach and pursuit**

TS=(((stalk OR stalks OR stalked OR stalking OR chase OR chased OR chasing) NEAR/5 (hunter\* OR hunting OR hunted)) OR (("pursuit success" OR "pursuit failure" OR "pursuit time" OR "successful pursuit\*" OR "failed pursuit\*" OR "initiated pursuit\*") NEAR/15 (hunter\* OR forager\* OR hunting)) OR ("probability of kill\*" NEAR/10 (encounter\* OR pursuit\* OR hunter\*)) OR (("approach distance\*" OR "flight initiation distance\*" OR "flushing distance\*" OR "alert distance\*" OR "escape distance\*") NEAR/10 (hunter\* OR hunting OR hunted)) OR "hunting attempt\*" OR "kill attempt\*" OR "failed hunt\*" OR "unsuccessful hunt\*" OR "successful hunt\*")  
**Why.** Anthropological work decomposes hunting into finding prey, pursuit and probability of kill upon encounter, so pursuit success and its relatives are included when a hunter or forager word is nearby. Ambush\* is removed because it mostly describes natural predators. Stalk and chase forms are spelled out because cyberstalking, plant stalks and chase scenes are common false matches.

### **HT-B3. Shot, hit and miss**

TS=("shot opportunit\*" OR "shooting opportunit\*" OR "shot placement" OR "shot distance\*" OR "shooting distance\*" OR "missed shot\*" OR "lethal shot\*" OR broadhead\* OR (("shots per" OR "shots fired" OR "shots taken" OR "shooting accuracy" OR "shooting success" OR "hit probabilit\*" OR "kill probabilit\*") NEAR/10 (hunter\* OR hunting OR hunted)) OR ((shot OR shots OR shooting OR arrow OR arrows OR bullet\* OR rifle\* OR bow OR firearm\*) NEAR/10 (miss OR missed OR hit OR hits OR accuracy OR placement OR opportunit\*)) OR (ballistic\* NEAR/10 (hunter\* OR hunting)))  
**Why.** Weapon words count only beside hit, miss, accuracy or placement words. Phrases that sports, policing and military papers also use (shots per, shots fired, hit probability) are tied to hunting words. This avoids shotgun sequencing, vaccine shots and one-shot learning.

### **HT-B4. Wounding, loss and retrieval**

TS=("wounding loss\*" OR "wounding rate\*" OR "crippling loss\*" OR "crippling rate\*" OR "wounded and lost" OR "wounded-and-lost" OR "hunter inflicted" OR nonretriev\* OR non-retriev\* OR unretriev\* OR nonrecover\* OR non-recover\* OR "blood trail\*" OR ((unrecovered OR "not recovered" OR "not retrieved" OR "recovery rate\*" OR "lost game" OR "lost animal\*" OR "wounded game" OR "wounded animal\*" OR "tracking dog\*" OR "recovery dog\*" OR "game recovery" OR "carcass recovery" OR "carcass retrieval") NEAR/10 (hunter\* OR hunting OR hunted)) OR ((wound OR wounds OR wounded OR wounding OR crippl\*) NEAR/5 (hunter\* OR hunting OR hunted OR "game animal\*" OR wildlife OR "wild animal\*")) OR (("time to death" OR "time to insensibility" OR "instantaneous death" OR "instantaneous kill\*" OR "clean kill\*" OR "killing efficiency") NEAR/10 (hunter\* OR hunting OR shooting OR arrow\* OR bullet\*)))  
**Why.** Wounding and retrieval loss is where a hit stops being a harvest. Wounding rate, wounding loss, crippling rate and crippling loss are used interchangeably in the literature, so all four are searched. Non-recovery and hunter-inflicted wounding were added after the literature check. Generic recovery phrases count only near a hunting term, because wind turbine and pet studies use them.

### **HT-B5. Overall success and effort**

TS=(((hunt OR hunts OR hunted OR hunting OR hunter\* OR harvest\* OR shooting) NEAR/5 (success OR successes OR successful OR successfully OR unsuccessful OR fail\* OR efficien\* OR "kill rate\*" OR "capture rate\*" OR "kills per")) OR (("harvest probabilit\*" OR "probability of harvest\*" OR "probability of being harvested" OR "probability of being killed") NEAR/10 (hunter\* OR hunting OR hunted)) OR (("hunting return\*" OR "return rate\*" OR "foraging return\*") NEAR/10 (hunter\* OR hunting OR forager\*)) OR (("hunting ability" OR "hunting skill\*" OR "hunting prowess" OR "hunting reputation") NEAR/10 (hunter\* OR forager\*)) OR (("trapping success" OR "trap success" OR "trapping efficiency" OR "capture efficiency" OR "capture success") NEAR/10 (trapper\* OR "fur trap\*" OR furbearer\* OR leghold\* OR "leg-hold\*" OR conibear\* OR snare\* OR snaring OR hunter\* OR hunting)) OR "days per kill" OR "days per harvest" OR "days per animal" OR "hours per kill" OR "effort per kill" OR "effort per animal" OR "kill per unit effort" OR "harvest per unit effort" OR HPUE OR (("days afield" OR "hunter-days" OR "hunter days" OR "hunter day" OR "gun-days" OR "gun days" OR "party-days" OR "hunter-hours" OR "man-days" OR "man days" OR "hunting trip\*") NEAR/10 (harvest\* OR kill OR kills OR killed OR success OR successful OR unsuccessful OR bag OR bagged OR "per unit effort")) OR (("empty-handed" OR "returned empty") NEAR/10 (hunter\* OR hunting)))  
**Why.** Older agency literature expresses effort as gun-days and party-days, so those stay beside hunter-days, but every effort-only term now needs a yield term within ten words. Success is spelled out because success\* matches succession and successor. Return rates and hunting ability are included because hunter-gatherer studies measure success that way. Trapping success counts only beside trapping gear or a hunting word. Productivity, yield per and hunting intensity are removed because they match crop, fisheries and exposure papers.

### **HT exclusions**

**HT-X (title only).**  
TI=(whaling OR "whale hunt\*" OR sealing OR "seal hunt\*" OR "marine mammal\*" OR "sea turtle\*" OR "marine turtle\*" OR seabird\* OR fishing OR fishery OR fisheries OR angling OR angler\* OR spearfishing OR bycatch OR aquaculture OR poach\* OR cull\* OR falconry)  
**HT-X2 (WoS category).**  
WC=(Economics OR "Agricultural Economics & Policy" OR Business OR Management OR "Hospitality, Leisure, Sport & Tourism" OR "Infectious Diseases" OR Virology OR Microbiology OR Parasitology OR Immunology)  
**Why.** X keeps marine and fishing titles out of the terrestrial module and removes poaching, culling and falconry titles. It uses the title field only, because abstracts of legitimate hunting papers mention fishing in passing. X2 removes the economics and disease-transmission records of the kind in your examples. Neither is applied until the sentinel set confirms that no sentinel record is removed. If one is, delete the category or term responsible.  
Block A: HT-A1 OR HT-A2 OR HT-A3 OR HT-A4 OR HT-A5  
Block B: HT-B1 OR HT-B2 OR HT-B3 OR HT-B4 OR HT-B5  
Final: (Block A) AND (Block B) NOT (HT-X OR HT-X2)

## **Module HA: human aquatic**

Status: the design follows the same rules, but its vocabulary has less direct support in this review of the literature than HT does. Terms marked as domain knowledge in the provenance table need sentinel validation before the module is final.

### **HA-A1. Fishing actors, practices and gear**

TS=(angler\* OR "recreational fishing" OR "recreational angling" OR "sport fishing" OR "commercial fishing" OR "subsistence fishing" OR "artisanal fishing" OR "small-scale fisher\*" OR "fly fishing" OR spearfishing OR spearfisher\* OR "fishing gear\*" OR "fishing method\*" OR "fishing technique\*" OR "hook and line" OR "hook-and-line" OR longline\* OR gillnet\* OR "gill net\*" OR trawl\* OR "purse seine\*")  
**Why.** Anyone who fishes is a human predator, and the gear names mark the capture process. The words are broad on purpose, so HA-B carries the precision. The gear words also match invertebrate fisheries, which are removed at screening because the review concerns wild vertebrate prey.

### **HA-A2. Human hunting of marine vertebrates**

TS=(whaling OR ((harvest\* OR harpoon\* OR subsistence OR commercial OR traditional OR indigenous OR inuit OR "first nations" OR aboriginal OR quota\* OR licen\*) NEAR/5 (whale\* OR cetacean\* OR pinniped\* OR "marine mammal\*" OR walrus\* OR seal OR seals OR dolphin\* OR porpoise\* OR "sea turtle\*" OR "marine turtle\*" OR seabird\* OR "sea duck\*")))  
**Why.** Marine hunting is defined by the animal hunted, so habitat-group words are used here and only here. A human role or regulatory word must sit within five words, which keeps natural predators such as orcas hunting seals out. Hunt and hunting are not in the context list for that reason. If you want no taxon-group words in any human module, this set can be replaced by the fishing and gear words alone, at the cost of missing marine mammal harvest papers.

### **HA-B1. Encounter and search**

TS=(("encounter rate\*" OR "encounter probabilit\*" OR "encounter frequenc\*" OR "time to encounter" OR "gear encounter\*" OR "search time" OR "search effort" OR "detection probabilit\*" OR "sighting rate\*" OR "sightings per") NEAR/10 (angler\* OR angling OR fishing OR hook OR hooks OR hooked OR gear OR longline\* OR gillnet\* OR trawl\* OR hunter\* OR hunting OR hunted OR harvest\*))  
**Why.** Encounter is the first process in the fishing capture framework (Spence et al.). The generic phrases count only beside fishing, gear or hunting words, because detection probability and encounter rate are also core survey-ecology terms.

### **HA-B2. Contact, attack and hooking**

TS=(("bite rate\*" OR "bite probabilit\*" OR "strike rate\*" OR "strike probabilit\*" OR "attack rate\*" OR "hooking success" OR "hooking probabilit\*" OR "hooking rate\*" OR "hooking efficiency" OR "contact probabilit\*" OR "vulnerability to capture" OR "vulnerability to angling" OR "angling vulnerability") NEAR/10 (angler\* OR angling OR fishing OR hook OR hooks OR hooked OR hooking OR bait\* OR lure\* OR gear OR net OR nets OR trawl\* OR longline\* OR gillnet\*))  
**Why.** Contact and attack are the second process in the capture framework, and vulnerability to capture by hooks is defined as the probability of capture for a given fish (Lennox et al. 2017). The phrases need a fishing or gear word nearby because attack rate is also a predator functional-response term.

### **HA-B3. Retention, escape and loss**

TS=("bite-off\*" OR "bite off\*" OR "hooked and lost" OR "hooked-and-lost" OR "struck and lost" OR "struck-and-lost" OR "struck but lost" OR "struck-but-lost" OR "escape mortality" OR "unaccounted fishing mortality" OR "unaccounted mortality" OR "dropout mortality" OR "drop-out mortality" OR (("retention probabilit\*" OR "escape probabilit\*" OR "escape rate\*" OR "gear escape\*" OR "net escape\*" OR "landing success" OR "landing rate\*" OR "landing efficiency") NEAR/10 (angler\* OR angling OR fishing OR hook OR hooks OR hooked OR gear OR net OR nets OR trawl\* OR longline\* OR gillnet\* OR trap OR traps OR pot OR pots OR struck OR hunting OR hunter\*)) OR (landed NEAR/5 (struck OR hooked)))  
**Why.** This is the aquatic equivalent of wounding loss. Struck-and-lost and struck-but-lost are the standard terms for animals hit but not retrieved in walrus and whale hunts. Bite-off appears in longline capture models, and retention is the third process in the capture framework. Escapement is left out because it mainly means salmon spawners escaping a fishery.

### **HA-B4. Overall capture success and efficiency**

TS=(((catchability OR "gear efficiency" OR "capture efficiency" OR "capture probabilit\*" OR "probability of capture" OR "capture success" OR "catch success") NEAR/10 (angler\* OR angling OR hook OR hooks OR hooked OR gear OR longline\* OR gillnet\* OR trawl\* OR trap OR traps OR net OR nets OR hunter\* OR hunting)) OR ((fishing OR angling OR angler\* OR hunt OR hunts OR hunted OR hunting OR hunter\* OR harvest\*) NEAR/5 (success OR successes OR successful OR successfully OR unsuccessful OR fail\* OR efficien\* OR "kill rate\*" OR "capture rate\*")) OR (("catch rate\*" OR "catch per angler" OR "catch per hour" OR "fish per hour" OR "angler-hour\*" OR "angler hour\*" OR "catch per unit effort" OR CPUE) NEAR/5 (angler\* OR angling OR "hook and line" OR "hook-and-line")))  
**Why.** Catchability and gear efficiency summarise the whole capture process. Catch per unit effort counts only beside angling words, where it measures angler success. In commercial fisheries it is an abundance index and is left out on purpose.

### **HA exclusions**

HA-X: TI=(aquaculture OR poach\* OR cull\* OR falconry OR bycatch OR discard\*)  
HA-X2: WC=(Economics OR "Agricultural Economics & Policy" OR Business OR Management OR "Hospitality, Leisure, Sport & Tourism" OR "Infectious Diseases" OR Virology OR Microbiology OR Parasitology OR Immunology)

Block A: HA-A1 OR HA-A2  
Block B: HA-B1 OR HA-B2 OR HA-B3 OR HA-B4  
Final: (Block A) AND (Block B) NOT (HA-X OR HA-X2)  
**Why.** Farmed fish are not wild prey. Bycatch and discard titles describe non-target capture, which is not predation success, but this is a judgement call that is recorded under decisions.

## **Changes from the 26 October draft (HT)**

| Change | Reason |
| :---- | :---- |
| Removed hunting success, hunting efficiency and hunting effort from A1; removed hunting strategy, technique, method, bout and party | Natural predator papers use these constantly, and hunting success sat in both blocks. |
| Removed hunting pressure, hunting trip and hunting return from A1 | Exposure and effort terms, not actor terms. Hunting trip is common in expenditure surveys. |
| A2 context: removed human, humans, people, dog, dogs, bow, wildlife, vertebrate\*, quarry, wild animal\* and harpoon\* | Predators hunt near people and hunt wildlife and vertebrates. The rest have unrelated meanings. |
| Removed illegal hunt\*, poach\* in A4, game meat, humane and cull\* | Poaching and culling are out of scope. Game meat matches food-safety papers. Humane draws ethics and attitude papers. |
| A3: harvest success, hunter harvest\* and wildlife harvest\* removed; kill terms no longer sit near wildlife, recreational, sport or trophy | Duplicates of other clauses, and roadkill and fisheries matches. |
| B1: removed detect\*, spotting, sighting\* near hunting; generic phrases need hunting terms within ten words | detect\* matches pathogen detection. The generic phrases are core survey-ecology terms. |
| B2: removed ambush\* and pursuit as hunting-word partners; added pursuit success, post-encounter and probability of kill phrases | Ambush and pursuit hunting describe natural predators. Anthropological papers use pursuit success as a stage measure. |
| B4: removed struck and lost; added non-recovery, hunter inflicted and recovery rate phrases | Struck and lost belongs to HA. The added phrases appear in wounding-rate studies. |
| B5: removed productivity, yield per and hunting intensity; effort terms now need a yield term; added return rates, hunting ability and harvest probability | Productivity and yield match crops and fisheries. Effort terms alone matched economics surveys. |
| Added X and X2 exclusions, and four-module structure | Separates realms and removes economics and disease noise. |

## **Term provenance**

"Checked" means the term or its concept was found in the literature during this review of sources. "Domain knowledge" means standard terminology that was not re-checked and must be confirmed with the sentinel set.

| Terms | Evidence | Status |
| :---- | :---- | :---- |
| animals seen per hunter day, hunter observation\*, observation rate\* | Ericsson and Wallin (1999) define the observation rate as moose seen per hunter day, and later studies reuse the phrasing. | Checked |
| wounding rate and loss, crippling rate and loss, hunter inflicted wounding, non-recovery | Wounding-rate studies of archery and firearm hunting, including a 1998 study of deer wounded by traditional archery, use these terms. A Wildlife Society technical review, cited in a secondary source, notes they are used interchangeably. | Checked |
| post-encounter return rate, pursuit, probability of kill upon encounter, failure rate, hunting ability, hunting return rate, encounter hunting, intercept hunting | Anthropological papers on the Ache, Hadza and Martu decompose hunting into finding prey, pursuit and kill upon encounter and report return rates. | Checked |
| struck-and-lost, struck-but-lost, landed, hunting efficiency | Fay et al. (1994) for walrus; Born et al. for Greenland walrus; Alaskan bowhead harvest reports. | Checked |
| encounter, contact, retention, catchability, vulnerability to capture, bite-off, lip-hooked | Spence et al., Lennox et al. (2017) and a longline capture model. | Checked |
| predation sequence stages | Endler (1991) as set out in Hämäläinen et al. (2022). | Checked |
| days afield, gun-days, party-days, man-days, harvest per unit effort, HPUE, broadhead, blood trail, tracking dog, shot placement | Wildlife-agency and bowhunting terminology carried over from the 26 October draft. | Domain knowledge |
| hooking success, escape mortality, unaccounted mortality, dropout mortality, landing success, angling vulnerability | Standard fisheries terminology. | Domain knowledge |

## **Validation protocol**

> 1. **Build the test list first.** Livoreil et al. (2017) put an agreed list of known relevant records before the search. Aim for at least 30 per module from reference lists of reviews and from papers you already know. Use half to choose terms and hold the other half back to test the final string, so the recall figure is not circular. A starter list from this review is in the next section.  
> 2. **Mine the pilot results for missing terms.** You already have exports from the old string. Run litsearchr (Grames et al. 2019\) on them, together with the test list, to find synonyms the strings miss. Add a term only if it appears in several test records, and log each addition.  
> 3. **Report retrieval performance.** For each module, report how many held-back test records the final string retrieves, and investigate each miss.  
> 4. **Estimate precision by sampling.** Screen a random sample of 200 records per module by title and abstract. For each irrelevant record, note which set retrieved it, using the UT= method above, and tighten that set.  
> 5. **Check the exclusions.** Run (Block A AND Block B) AND X, and the same with X2, and skim 100 records from each. Any relevant record found means the exclusion is too wide.  
> 6. **Count every set and report the search.** Record the count for each set, then the date, platform, field codes and full strings for PRISMA-S, and consider a PRESS review by a librarian.

### **Starter test list**

These are records seen during this review. They are a start, not a sufficient test list.

| Record | Module and set it should reach |
| :---- | :---- |
| Ericsson and Wallin (1999), hunter observations as an index of moose population parameters | HT-A1, HT-B1 |
| Wounding rates of white-tailed deer with traditional archery equipment (1998) | HT-A1 or A2, HT-B4 |
| Age-dependency in hunting ability among the Ache of eastern Paraguay | HT-A1 or A5, HT-B2 or B5 |
| Fay et al. (1994), the struck-and-lost factor in Alaskan walrus harvests | HA-A2, HA-B3 |
| Born et al., walruses and the walrus hunt in West and Northwest Greenland | HA-A2, HA-B3 |
| Lennox et al. (2017), what makes fish vulnerable to capture by hooks | HA-A1, HA-B2 or B4 |
| Spence et al., a process-based theory of fishing | HA-A1, HA-B1 or B4 |

## **Gaps considered and left out**

> * **Vulnerability to harvest and selectivity in HT.** These describe which animals are taken, not how often a hunt succeeds.  
> * **Hunter satisfaction and motivation.** The topic is large and mostly outside the research question.  
> * **Harvest rate and exploitation rate.** These are population-level fractions, not stage success. Darimont et al. (2015) compile such rates, so that paper is a useful context record but not a test record for the stage sets.  
> * **Papers that say wildlife hunting but never use a hunter word.** A2 and A3 catch many, and the test list is the check for the rest.  
> * **Archaeological hunting and natural predator comparisons.** Search terms cannot separate these, so screening handles them. Natural predator records that reach HT are not wasted, because they duplicate the NT module and are removed when the modules are pooled.

## **Decisions**

> 1. Decided: bycatch and discard titles are excluded from HA, because non-target capture is not predation success.  
> 2. Decided: habitat-group words are used only where needed to separate a realm (HA-A2 now, and the natural predator modules later) and are kept to the fewest that work.  
> 3. Pending: X2 is not applied by default. Run the final search with and without it, skim 100 records that only X2 would remove, and apply it only if none are relevant.  
> 4. Decided: invertebrate gear is handled at screening by the eligibility rule (wild vertebrate prey), not with search terms, so that the search stays sensitive.

## **Next modules**

NT and NA will use the same stage framework and Block B concepts with a natural predator anchor in Block A: vertebrate predator group words (carnivore, raptor, shark, pinniped, odontocete and similar), gated by attack, kill-rate and capture-success measures, with invertebrate predators excluded. Their vocabulary needs its own literature check, which is the next step.

## **References**

> * Darimont CT, Fox CH, Bryan HM, Reimchen TE (2015). The unique ecology of human predators. Science 349(6250): 858-860. doi:10.1126/science.aac4249  
> * Endler JA (1991). Interactions between predators and prey. In: Behavioural Ecology: An Evolutionary Approach, 3rd edition.  
> * Ericsson G, Wallin K (1999). Hunter observations as an index of moose Alces alces population parameters. Wildlife Biology 5(3): 177-185. doi:10.2981/wlb.1999.022  
> * Fay FH, Burns JJ, Stoker SW, Grundy JS (1994). The struck-and-lost factor in Alaskan walrus harvests, 1952-1972. Arctic 47(4): 368-373. doi:10.14430/arctic1310  
> * Grames EM, Stillman AN, Tingley MW, Elphick CS (2019). An automated approach to identifying search terms for systematic reviews using keyword co-occurrence networks. Methods in Ecology and Evolution. doi:10.1111/2041-210X.13268  
> * Hämäläinen L, Rowland HM, Mappes J, Thorogood R (2022). Social information use by predators: expanding the information ecology of prey defences. Oikos 2022(10): e08743. doi:10.1111/oik.08743  
> * Lennox RJ, Alós J, Arlinghaus R, Horodysky A, Klefoth T, Monk CT, Cooke SJ (2017). What makes fish vulnerable to capture by hooks? A conceptual framework and a review of key determinants. Fish and Fisheries. doi:10.1111/faf.12219  
> * Livoreil B, Glanville J, Haddaway NR, et al. (2017). Systematic searching for environmental evidence using multiple tools and sources. Environmental Evidence 6: 23\. doi:10.1186/s13750-017-0099-6  
> * Spence MA, Pace MC, Minto C, Bartos TIJ, Dolder PJ. A process-based theory of fishing. Natural Resource Modeling. doi:10.1111/nrm.70040  
> * Born EW, Heilmann A, Holm LK, Laidre KL, Iversen M. Walruses and the walrus hunt in West and Northwest Greenland: an interview survey about the catch and the climate. Monographs on Greenland, Man and Society 44\.