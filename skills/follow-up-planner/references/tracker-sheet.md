# Tracker sheet: follow-up-planner

Give this when the owner asks for a tracker or a "due today" view. For the full build (sample rows, phone setup steps, locale), hand off to **tracker-sheet-builder**. Names and phone numbers live only in the owner's own sheet, never in the chat. The owner types only codes (S1, M3) into Claude.

## Columns (tab name: Tracker)

```
Code	Group	First message date	Step	Last message date	Next follow-up date	Status	Notes
```

- A Code: S1, S2... (one per person; the sheet can have a name column further right, typed only by the owner).
- B Group: Donors, Members, Volunteers, Leads.
- C First message date, E Last message date: dates (set the sheet's locale to India so they read day/month).
- D Step: 1, 2 or 3 (dropdown).
- F Next follow-up date: formula, below.
- G Status: Waiting, Replied, Yes, No, Stop (dropdown).
- H Notes: "call back Friday, October 23", "Do not contact".

## Settings
- J1 `Days after step 1`, J2 the owner's number.
- J3 `Days after step 2`, J4 the owner's number.
- If the owner gave no number, write [blank] and tell them to type theirs in J2 and J4. Never pick one.

## Formulas
- Simple version (same wait every time, for example 3 days): F2 `=E2+3`.
- Guarded version, F2: `=IF(OR(E2="",G2<>"Waiting",D2>=3),"",E2+IF(D2=1,$J$2,$J$4))`. It stays empty once someone replies, says no, asks to stop, or has had step 3. Copy it down.
- "Due today" tab: copy the header row into row 1, then in A2:
  `=IFERROR(FILTER(Tracker!A2:H, Tracker!F2:F<>"", Tracker!F2:F<=TODAY(), Tracker!G2:G="Waiting"),"Nothing due today")`
  (The short form `=FILTER(Tracker!A:H, Tracker!F:F<=TODAY(), Tracker!G:G="Waiting")` works too, but it also lists a Waiting row whose date is empty, and shows an error when nothing is due.)
- Optional count for a summary cell: `=COUNTIFS(Tracker!F2:F,"<="&TODAY(),Tracker!G2:G,"Waiting")`.

## Colors (conditional formatting)
- Due or overdue: select columns A to H, custom formula `=AND($F1<>"",$F1<=TODAY(),$G1="Waiting")` → orange fill.
- Stop: select columns A to H, custom formula `=$G1="Stop"` → grey text.
- Yes: column G, text is exactly "Yes" → green fill.

## Daily routine
1. Open "Due today". Each row tells you the code and the step it is on; send the next step.
2. Change Step to the new step and Last message date to today. Next follow-up date updates by itself.
3. When someone replies, change Status (Replied, Yes, No or Stop). They drop off "Due today".
4. A daily Google Calendar reminder to yourself ("Follow-ups: check Due today") at a time you choose helps.
