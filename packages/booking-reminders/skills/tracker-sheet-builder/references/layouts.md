# Ready-made sheet layouts

Pick the closest layout, change column names to the owner's words, and keep the same pattern. Every table is tab-separated: paste it into cell A1. Rows starting with "Sample" are made-up examples for the owner to delete. Formula columns are left empty in the table: the owner types the formula once in row 2 and copies it down.

Dates are typed as day/month/year (14/10/2026). Times as 10:30. Set the sheet's locale to India before pasting (setup step 1), or dates can be read the wrong way round.

Color rules: the owner selects whole columns, which start at row 1, so every custom formula uses row 1 (`=$E1="Lost"`). Header text never matches these rules, so the header row stays uncolored. If a step selects a smaller range instead (layout 9), the formula uses that range's first row.

Contents
1. Client and lead tracker (tab: Clients)
2. Booking availability (tab: Bookings)
3. Staff task list (tab: Tasks)
4. Daily job tracker (tab: Jobs, plus a Today tab)
5. Delivery log (tab: Deliveries)
6. Stock sheet with reorder and expiry (tab: Stock)
7. Vendor list and new-vendor checklist (tab: Vendors)
8. Order and prep sheet (tabs: Orders and Prep)
9. Simple dashboard (tab: Dashboard)
10. Tidying a contact list (steps only, the owner does it in their own sheet)

---

## 1. Client and lead tracker (tab: Clients)

```
Client	Came from	Wants	Fit	Stage	Last contact	Follow up on	Due?	Notes
Sample Client A	Instagram	Wedding shoot	Hot	Quote sent	01/10/2026			Asked for 2 options
Sample Client B	Referral	Café menu photos	Warm	Talking	05/10/2026			
Sample Client C	Walk-in	Family portrait	Cold	New	10/10/2026			
```

Setting cell: type `Follow up after (days)` in K1 and the owner's number in K2. If the owner has not said, write `[blank]` in K2 and tell them to replace it.

Formulas
- G2 `=IF(OR(F2="",NOT(ISNUMBER($K$2))),"",F2+$K$2)` gives the follow-up date.
- H2 `=IF(G2="","",IF(AND(G2<=TODAY(),E2<>"Won",E2<>"Lost"),"Follow up",""))` says "Follow up" when it is due.

Colors
- Column H: text is exactly "Follow up" → orange fill.
- Column D: "Hot" → green fill, "Cold" → grey fill.
- Whole row when Stage is "Lost" → grey text (select columns A to I; custom formula `=$E1="Lost"`).

Dropdowns: Fit (Hot, Warm, Cold); Stage (New, Talking, Quote sent, Won, Lost); Came from (Instagram, WhatsApp, Walk-in, Referral, Google).

Note: "Client" can be a business name or a first name. If the owner wants a phone column, they type numbers only in their own sheet, never in the chat.

## 2. Booking availability (tab: Bookings)

```
Booking ref	Room	Check-in	Check-out	Nights	Came from	Status	Clash?	Notes
Sample-001	Room 1	18/10/2026	21/10/2026		Direct	Confirmed		
Sample-002	Room 2	19/10/2026	20/10/2026		Airbnb	Confirmed		Late arrival
Sample-003	Room 1	20/10/2026	22/10/2026		Direct	Held		
```

Formulas
- E2 `=IF(OR(C2="",D2=""),"",D2-C2)` counts nights.
- H2 `=IF(OR(B2="",C2="",D2=""),"",IF(COUNTIFS($B:$B,B2,$C:$C,"<"&D2,$D:$D,">"&C2,$G:$G,"<>Cancelled")>1,"Clash",""))` flags two bookings in the same room on the same night (sample rows 1 and 3 will show "Clash").

"Is it free?" box: K1 `Check date`, L1 the date; K2 `Room`, L2 the room; K3 `Answer`, L3:
`=IF(OR(L1="",L2=""),"",IF(COUNTIFS(B:B,L2,C:C,"<="&L1,D:D,">"&L1,G:G,"<>Cancelled")=0,"Free","Booked"))`

Colors
- Column H: "Clash" → red fill.
- Column G: "Held" → yellow fill, "Cancelled" → grey text.

Note: use a booking ref, not the guest's name. Passport, Form C and phone details never go in this sheet.

## 3. Staff task list (tab: Tasks)

This lists tasks, not people. No scores, ratings or "who missed most" columns.

```
Task	Area	Who (role)	How often	Due date	Done	Overdue?	Notes
Sample: wipe display fridge	Kitchen	Morning helper	Daily	15/10/2026	Yes		
Sample: change towels	Rooms	Housekeeping	Daily	15/10/2026			
Sample: order gas cylinder	Store	Owner	Weekly	17/10/2026			
```

Formula
- G2 `=IF(OR(E2="",F2="Yes"),"",IF(E2<TODAY(),"Overdue",""))`

Colors
- Column G: "Overdue" → light orange fill.
- Whole row when Done is "Yes" → grey text (select columns A to H; custom formula `=$F1="Yes"`).

Dropdowns: Done (Yes, blank); Area (the owner's areas).

## 4. Daily job tracker (tab: Jobs, plus a Today tab)

```
Date	Job	Place	Assigned (role)	Start time	Status	Notes
15/10/2026	Sample: garden clean-up	Assagao	Team A	09:00	To do	
15/10/2026	Sample: AC service	Panjim	Team B	11:30	In progress	Bring filter
16/10/2026	Sample: deep clean	Mandrem	Team A	10:00	To do	
```

Today tab (morning summary)
- A1 `=TODAY()`
- A2 `=COUNTIFS(Jobs!A:A,TODAY(),Jobs!F:F,"Done")&" done, "&COUNTIFS(Jobs!A:A,TODAY(),Jobs!F:F,"<>Done")&" to go"`
- A4 `=IFERROR(FILTER(Jobs!A2:G,Jobs!A2:A=TODAY()),"No jobs today")` shows today's jobs.

Colors (Jobs tab): Status "Done" → green fill; "In progress" → yellow fill.

## 5. Delivery log (tab: Deliveries)

For planning routes and fuel, not for judging riders.

```
Date	Order ref	Area	Out time	Back time	Minutes	Km	Result	Notes
15/10/2026	Sample-101	Mandrem	10:00	10:40		12	Delivered	
15/10/2026	Sample-102	Beach road	11:15	12:05		18	Delivered	Gate locked, called
15/10/2026	Sample-103	Morjim	14:00	14:30		9	Returned	Nobody home
```

Formula
- F2 `=IF(OR(D2="",E2=""),"",ROUND((E2-D2)*24*60,0))` gives minutes.

Daily totals (anywhere, e.g. K1/K2)
- Km today `=SUMIF(A:A,TODAY(),G:G)`
- Delivered today `=COUNTIFS(A:A,TODAY(),H:H,"Delivered")`

Colors: Result "Returned" → orange fill.

## 6. Stock sheet with reorder and expiry (tab: Stock)

```
Item	Unit	In stock	Reorder at	Reorder?	Expiry date	Days left	Supplier	Last checked
Sample butter	kg	2	3		20/10/2026		Sample Dairy	14/10/2026
Sample flour	kg	25	10		15/01/2027		Sample Mill	14/10/2026
Sample cream	litre	4	2		16/10/2026		Sample Dairy	14/10/2026
```

Formulas
- E2 `=IF(OR(C2="",D2=""),"",IF(C2<=D2,"Reorder",""))` (the core is `=IF(C2<=D2,"Reorder","")`; the outer part keeps empty rows quiet).
- G2 `=IF(F2="","",F2-TODAY())` gives days to expiry.

Colors (add in this order)
- Column E: text is exactly "Reorder" → red fill.
- Column G: days left below 0 (already expired) → grey fill (custom formula `=AND(ISNUMBER($G1),$G1<0)`).
- Column G: 3 days or less left → red fill (custom formula `=AND(ISNUMBER($G1),$G1<=3)`).
- Column G: 7 days or less left → yellow fill (custom formula `=AND(ISNUMBER($G1),$G1<=7)`).

The owner sets "Reorder at" for each real item. Never guess it.

## 7. Vendor list and new-vendor checklist (tab: Vendors)

```
Vendor	Supplies	How to order	Order days	Lead time (days)	Sample checked	Rate agreed in writing	Last order	Days since order	Notes
Sample Dairy	Butter, cream	WhatsApp	Mon, Thu	1	Yes	Yes	10/10/2026		
Sample Mill	Flour	Call	Monthly	3	Yes	No	01/10/2026		Ask for written rate
Sample Packaging	Boxes	Visit shop	As needed	2	No	No			New vendor
```

Formula
- I2 `=IF(H2="","",TODAY()-H2)`

Colors
- Columns F and G: "No" → yellow fill (checklist not finished).

Note: bank, UPI and payment amounts stay off this sheet. Settling vendor bills is money record-keeping: keep it on paper.

## 8. Order and prep sheet (tabs: Orders and Prep)

Orders tab
```
Needed on	Order ref	Item	Qty	Ready by	Status	Notes
16/10/2026	Sample-201	Croissant	12	08:00	New	
16/10/2026	Sample-202	Sourdough loaf	3	09:30	New	Sliced
16/10/2026	Sample-203	Croissant	6	10:00	New	
```

Prep tab
- A1 `Prep for`, B1 `=TODAY()+1` (tomorrow; or type a date).
- A3 `Item`, B3 `Total`. Type each item name in A4, A5…
- B4 `=SUMIFS(Orders!D:D,Orders!C:C,A4,Orders!A:A,$B$1,Orders!F:F,"<>Cancelled")` then copy down.

Colors (Orders tab): Status "Ready" → green fill; whole row needed today but not Ready → orange fill (select columns A to G; custom formula `=AND($A1=TODAY(),$F1<>"Ready")`).

## 9. Simple dashboard (tab: Dashboard)

Counts only. No cash, sales money or per-person totals here.

```
What	Number
Items to reorder	
Items expiring in 7 days	
Follow-ups due	
Overdue tasks	
Deliveries today	
Km this week	
Check-ins in the next 7 days	
Orders for tomorrow	
```

Formulas for column B (use only the tabs the owner has)
- `=COUNTIF(Stock!E:E,"Reorder")`
- `=COUNTIFS(Stock!G:G,">=0",Stock!G:G,"<=7")`
- `=COUNTIF(Clients!H:H,"Follow up")`
- `=COUNTIF(Tasks!G:G,"Overdue")`
- `=COUNTIF(Deliveries!A:A,TODAY())`
- `=SUMIFS(Deliveries!G:G,Deliveries!A:A,">="&(TODAY()-6))`
- `=COUNTIFS(Bookings!C:C,">="&TODAY(),Bookings!C:C,"<="&(TODAY()+6),Bookings!G:G,"<>Cancelled")`
- `=COUNTIF(Orders!A:A,TODAY()+1)`

Colors: select B2 to B5 only, then any number above 0 → orange fill (custom formula `=$B2>0`, because this range starts at row 2).

Easier data entry: add dropdowns (select cells → Data validation → Dropdown) so staff tap instead of type.

## 10. Tidying a contact list (the owner does this in their own sheet)

Never take the list into the chat. Give these steps. Assume names in A and numbers in B.
1. C2 `=PROPER(TRIM(A2))` tidies names (extra spaces, capitals).
2. D2 `=RIGHT(REGEXREPLACE(TO_TEXT(B2),"[^0-9]",""),10)` keeps the last 10 digits (removes spaces, +91, dashes).
3. E2 `=IF(D2="","",IF(COUNTIF(D$2:D2,D2)>1,"Duplicate",""))` marks the second and later copies of the same number. Rows with no number stay blank, so they are never marked.
4. Copy C2:E2 down. Filter column E for "Duplicate", check each one, then delete those rows. On a laptop you can also use Data → Data cleanup → Remove duplicates, or `=UNIQUE(C2:D)` on a new tab.
5. To sort into groups, add a "Group" column with a dropdown (Regular, New, Wholesale) and filter by it. Only message people who agreed to hear from the business.
