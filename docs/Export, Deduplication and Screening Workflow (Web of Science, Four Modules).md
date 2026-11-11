# **Export, Deduplication and Screening Workflow (Web of Science, Four Modules)**

Companion to the search strategy document. Version of 10 November 2026\. The Web of Science menus and ASReview features below were checked against library guides and the ASReview documentation, but not on your own installation, so confirm each dialog as you go.

## **Sequence**

> 1. Run and record the searches (HT, HA, NT, NA).  
> 2. Export each module's final set from Web of Science in batches.  
> 3. Merge and deduplicate across modules, keeping a record of which modules found each paper.  
> 4. Screen each module in its own ASReview project.  
> 5. Classify the included records with tags, then move to full text and extraction.

## **Step 1\. Run and record**

> * Run each set as its own search so you get a count per set, then combine them as described in the search strategy. Record every count and the date for PRISMA-S.  
> * For the exclusion X2 (the category filter), run the final search twice: with X2 and without it. The records that only X2 removes are the final search without X2 AND X2. Skim 100 of them before deciding to apply it.  
> * Copy the exact final query string of each module into the search strategy document at the time you run it.

## **Step 2\. Export from Web of Science**

> * From the results list of a module's final search, choose Export, then Tab delimited file.  
> * Under Record Options, choose Records from 1 to 1000\. Under Record Content, choose Full Record. Full Record keeps the accession number (UT), DOI, abstract, keywords and Web of Science categories, which the merge script and the classification need.  
> * Repeat for 1001 to 2000 and so on until the last record. Most library guides give 1,000 records per export, and some older guides give 500, so use whatever limit your dialog states.  
> * Name each file with the module and range, for example HT\_0001-1000.txt, and put each module in its own folder: data/HT, data/HA, data/NT, data/NA.  
> * Do not use Fast 5K for screening. It exports up to 5,000 records but only basic fields (author, title, source), so there is no abstract.  
> * Check that the rows across a module's files add up to the count Web of Science reported. If they do not, redo the export in smaller batches.

## **Step 3\. Merge and deduplicate**

The script merge\_wos\_exports.py (delivered with this document) reads the four folders and does the following:

> * Matches duplicates by accession number, then DOI, then normalised title plus year, and collapses them into one record.  
> * Keeps a modules column such as HT\|NT, so you know every module that retrieved a paper. A paper retrieved by a human module and a natural module is likely a direct human-versus-natural comparison, which is the most valuable kind for your question. Tag these as comparative when you screen them.  
> * Assigns each record to one screening project, in the order HT, HA, NT, NA, so nothing is screened twice.  
> * Flags records with no abstract and prints counts of raw, unique and overlapping records for the PRISMA flow diagram.  
> * Writes one CSV per module (asreview\_HT.csv and so on) with title and abstract columns, which ASReview reads.

It was tested on small synthetic files in the same column format, not on a real export. Run it on one real batch first and compare the row counts it prints with your export.  
`pip install pandas`  
`python merge_wos_exports.py --data data --out screening`  
Records with no abstract: ASReview needs a title or an abstract and combines them when both exist, so these records can still be screened on the title alone. Decide in advance whether to screen them that way or retrieve abstracts first.

## **Step 4\. One ASReview project per module**

Earlier I suggested pooling all four modules into one project. I now recommend one project per module instead, for three reasons. The stopping rule and recall check are then per search, so a sparse module such as NA cannot be stopped early by a dense one. Each module has its own test list. And the vocabulary and relevance density differ between modules, which affects how the model learns. The modules column keeps the cross-module information, so nothing is lost.

## **Step 5\. Set up each ASReview project**

> 1. Install ASReview LAB (the current release line needs Python 3.10 or later) with pip install asreview, and start it with asreview lab.  
> 2. Create a project and import the module's CSV. Duplicate records are hidden automatically in the current version, but you have already deduplicated, so the PRISMA counts come from the script.  
> 3. Add prior knowledge: a handful of relevant records from the training half of your test list, and several irrelevant ones. The three false positives you sent (barn owl movement ecology, hunting practices and disease transmission between dogs, and the deer hunter economics survey) make good irrelevant priors.  
> 4. Keep the other half of the test list unseen by the model. It is the check that the model finds known relevant papers on its own.  
> 5. Write the eligibility rule and the stopping rule below into your protocol before screening begins.

## **Eligibility rule for title and abstract screening (proposal)**

Label a record relevant if it reports, or is likely to report, a quantitative measure of success or failure of predation at one or more stages (encounter, pursuit or attack, capture or kill, loss, retrieval, overall), with a denominator such as per encounter, attempt, shot, hunter day or unit effort. The predator is a human or a non-human vertebrate. The prey are wild vertebrates. Empirical studies and reviews that synthesise such measures both count, and reviews are tagged for citation chasing.  
Label a record irrelevant if the prey are domestic, farmed or invertebrate (this is how invertebrate gear in the fishing searches is handled), if there is no success measure (attitudes, economics, disease, regulation), if it reports only population-level exploitation or mortality rates, or if it is a pure simulation with no empirical data. When unsure at this stage, label it relevant and decide at full text.

## **Classification tags**

Add tags while screening, or in the first full-text pass, so that the extraction table starts organised. The current ASReview version lets you create and edit tags on the Collection screen.

| Tag group | Values |
| :---- | :---- |
| Realm | terrestrial, aquatic, both |
| Predator | human, natural, both (comparative) |
| Stage reported | encounter, pursuit or attack, capture or kill, loss, retrieval, overall |
| Measure type | per encounter, per attempt, per shot, per unit effort, other |
| Flags | review (for citation chasing), no abstract, needs full text |

## **Stopping rule**

Fix the rule before you start. The SAFE procedure (Boetje and van de Schoot 2024\) combines several checks so that screening does not stop early. It has four phases: screen a random set for training, apply active learning, look for more relevant records with a different model, and evaluate quality. The combined rule uses a minimum percentage of records screened plus a run of consecutive irrelevant records. The experts consulted for the paper called 50 consecutive irrelevant records a safe and reasonable threshold, and said a higher number may be needed when relevant records are sparse or when missing one is costly. It also uses a visual check of the recall plot and a key-paper check, which here is the held-back half of your test list. Choose the minimum percentage and the run length yourself and write them down per module.

## **After screening**

> * Export the labelled dataset from each project, including tags.  
> * Retrieve full texts for the relevant records, apply the eligibility rule again, and record reasons for exclusion for PRISMA.  
> * Run LLM-assisted extraction with human verification on the included set, using the tags to build the extraction table.  
> * Report per module: records identified, duplicates removed, records screened, records included at title and abstract, and records included at full text.

## **References**

> * Boetje J, van de Schoot R (2024). The SAFE procedure: a practical stopping heuristic for active learning-based screening in systematic reviews and meta-analyses. Systematic Reviews 13: 81\. doi:10.1186/s13643-024-02502-7  
> * van de Schoot R, de Bruin J, Schram R, et al. (2021). An open source machine learning framework for efficient and transparent systematic reviews. Nature Machine Intelligence 3: 125-133. doi:10.1038/s42256-020-00287-7