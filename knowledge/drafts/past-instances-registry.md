# Past Instances: Registry Entries

Two already-taught instances are prepared as delivered profiles under `workshops/` and are ready for the register. The entries below use the field schema of `docs/data/workshops.json` unchanged and are meant to be pasted into the `workshops` array. Every value is taken from the source export that lies in the respective workshop folder as `workshop-script.txt`; where a value is an inference rather than a statement of the source, the profile of that instance says so.

## ÖAW AI Winter School 2026, taught 2026-02-17

```json
{
  "id": "2026-02-17-oeaw-ai-winter-school",
  "dates": "2026-02-17",
  "title": "Vibe Coding & Promptotyping",
  "event": "ÖAW AI Winter School 2026, Vienna",
  "audience": "winter-school participants doing computer-based research, with heterogeneous coding experience",
  "focus": "asymmetric amplification as the running thesis, Promptotyping hands-on core, reflection on research integrity and governance",
  "language": "en",
  "status": "delivered",
  "slides": "https://tinyurl.com/vibing-26",
  "script": "https://tinyurl.com/vibing-26-notes",
  "cover": null
}
```

## VetMedAI Workshop 1, taught 2026-04-22

```json
{
  "id": "2026-04-22-vetmedai-workshop-1",
  "dates": "2026-04-22",
  "title": "Grundlagen Generativer KI und Prompt Engineering",
  "event": "VetMedAI, Veterinärmedizinische Universität Wien",
  "audience": "university staff in an institutional AI-competence programme",
  "focus": "German LLM fundamentals and prompt engineering, EU AI Act block with a knowledge-document hands-on",
  "language": "de",
  "status": "delivered",
  "slides": null,
  "script": null,
  "cover": null
}
```

## Before applying

1. `status` gains the value `delivered`, which the register has not carried before, and both entries sort ahead of every planned instance by date, so the front of the array changes if the list stays chronological.
2. The ÖAW instance was co-taught and its audience is inferred from the self-assessment block rather than stated in the source; the schema holds no field for either fact, so both live in `workshops/2026-02-17-oeaw-ai-winter-school/profile.md` alone.
3. Link fields are copied verbatim from the title slides, meaning two unresolved short links for the ÖAW instance and no live surface at all for the VetMedAI instance, and neither instance has a cover, so `cover` stays null and no file is expected under `docs/assets/covers/` for these two ids.
