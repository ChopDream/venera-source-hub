---
name: venera-source-builder
description: Create, repair, validate, and maintain Venera comic-source repositories from real website evidence. Use for Venera repository URLs, new comic sources, broken-source fixes, website-to-source conversion, source indexing, or scheduled validation.
---

# Venera Source Builder

Route: `practice_distill` → `Practice skill` → `BEST_OF`.

## Operating card

`Confirm Venera schema → collect live evidence → classify responses → implement source → update index → run static checks → validate search/detail/chapter/images → publish → record gaps`.

Never invent selectors, API fields, chapter IDs, image URLs, HTTP responses, or playback success. Unknown evidence stays `UNKNOWN`; an unrun check is `NOT EXECUTED`.

## Intake

Record the target website URL, source name/key, test keyword, existing source and observed failure, and Venera app version when relevant. A concrete target is required for a real source; otherwise create only a template and tooling.

## Venera format

Use Venera's current source documentation and config examples as primary evidence. The repository index is a JSON array with synchronized `name`, `fileName`, `key`, and `version`; `description` is optional. A source defines a class extending `ComicSource`, metadata such as `name`, `key`, `version`, `minAppVersion`, and an update `url` when supported.

Do not copy old field names blindly. Keep the index and source metadata synchronized.

## Evidence collection

Fetch homepage and a real search request for a user keyword. Trace `search result → comic detail → chapter list → chapter page/API → image URLs`. Prefer actual responses over guessed patterns. Save credential-free samples under `evidence/<host>/`: URL/method, sanitized headers, status, HTML/JSON, selected links/IDs/titles/chapter keys/image fields, timestamp, and keyword.

Classify each stage as HTML, JSON API, mixed, dynamic/blocked, login-required, or site-side unavailable. Search and chapter loading can use different mechanisms.

## SMIB rule extraction

For each parser decision write:

- **State**: observed response or failure;
- **Mechanism**: selector, JSON path, URL construction, header, or decoding logic;
- **Illustration**: evidence file and exact fragment;
- **Boundary**: layout variant, login, rate limit, region block, or unverified case.

Tag claims `OBSERVED`, `INFERRED`, `EXTRAPOLATED`, or `UNKNOWN`. Release only evidence-supported rules.

## Implement or repair

Preserve unrelated behavior and change the smallest failing module: metadata/index, search/pagination, detail/cover, chapter IDs, then image extraction/order/decoding/headers. Handle accounts/cookies only when evidence requires it.

Use documented Venera APIs (`Network.get/post/sendRequest`, HTML parsing, `Comic`, `ComicDetails`, and the source lifecycle). Never put cookies, tokens, API keys, or personal credentials in files, evidence, commits, logs, or URLs.

## Validation and maintenance

Structural gates: valid JSON; indexed files exist; unique file names/keys; metadata agrees; source extends `ComicSource`; syntax/delimiter checks; source URL points to the intended path.

Behavior gates: search returns title/ID; detail opens; chapters are non-empty; two chapters work when available; images are non-empty and ordered; pagination or an alternate work is checked when available. Report `PASS`, `FAIL`, or `NOT EXECUTED`. Static checks do not prove playback; distinguish parser correctness, HTTP reachability, and media availability.

Failure loop: `reproduce → save minimal evidence → isolate stage → patch one module → static checks → behavior checks → increment version → record gap`. Do not fabricate repairs from scheduled URL checks. Retry at most twice without new evidence, then request the smallest missing sample.

A repository URL points directly to raw `index.json`:

```text
https://raw.githubusercontent.com/OWNER/REPO/main/index.json
```

Delivery states changed files, index URL shape, source name/key/version, verified evidence, residual gaps, and next required input.

## GitHub credential rule

Never persist or echo access tokens. A token pasted into chat is compromised; instruct revocation before any remote operation. Prefer local diff/commit review and the narrowest permission. Never use a pasted token in commands or files.

## Boundaries and tensions

- A source can be structurally valid while the website blocks requests or its media has expired; report these separately.
- A fast guessed selector may restore one page but is weaker than a slower evidence-backed parser; choose the latter for release.
- A scheduled URL check can detect breakage but cannot infer a safe repair; require fresh HTML/JSON evidence.
- A source may support search while chapter images require login, region access, or a client-only API; preserve partial status instead of claiming full success.
- If the target site is unavailable or protected, stop at the last verified stage and mark later stages `UNKNOWN`.
