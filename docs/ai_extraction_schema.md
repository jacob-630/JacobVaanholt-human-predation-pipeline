# AI Extraction Schema
# This is the JSON structure the AI Agent will output for every paper.

{
  "study_id": "unique_id",
  "citation": "Author, Year, Title",
  "taxon": "Species name (if mentioned)",
  "geography": "Province/State, Country",
  "method": "Hunting type (e.g., bow, rifle, spear, hook, net)",
  
  "stage_counts": {
    "available": null, 
    "detected": null,
    "attempted": null,
    "hit_or_captured": null,
    "recovered_or_kept": null,
    "harvest": null
  },
  
  "denominator_type": "hunter-days OR angler-hours OR attempts OR shots",
  "notes": "Any specific limitations or data gaps"
}
