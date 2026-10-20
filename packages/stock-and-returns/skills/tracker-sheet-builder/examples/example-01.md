# Example 01: order and prep sheet (fictional)

**Owner:** "I run Sample Café in Panjim. People order cakes and loaves on WhatsApp for the next day and I lose track of how much to bake. I fill it in myself on my phone."

**Your orders and prep sheet** (tabs: Orders and Prep)

**Table** for the Orders tab (copy everything in the box, paste into cell A1)
```
Needed on	Order ref	Item	Qty	Ready by	Status	Notes
16/10/2026	Sample-201	Croissant	12	08:00	New	
16/10/2026	Sample-202	Sourdough loaf	3	09:30	New	Sliced
16/10/2026	Sample-203	Croissant	6	10:00	New	
```
The rows starting with "Sample" are examples. Delete them when you add your own.

**Formulas** (on the Prep tab)
- A1: type `Prep for`. B1: `=TODAY()+1` shows tomorrow's date (or type a date).
- A3: `Item`, B3: `Total`. Type each item you bake in A4, A5 and down.
- B4: `=SUMIFS(Orders!D:D,Orders!C:C,A4,Orders!A:A,$B$1,Orders!F:F,"<>Cancelled")` adds up how many of that item are needed. Copy it down the column. (With the sample rows, Croissant shows 18.)

**Colors** (Orders tab)
- Column F: text is exactly "Ready" → green fill.
- Whole row needed today but not Ready → orange fill (select columns A to G; custom formula `=AND($A1=TODAY(),$F1<>"Ready")`).

**Set it up on your phone** (Google Sheets app)
1. Open the Google Sheets app, tap +, then New spreadsheet. Rename it "Orders and prep". **Before you paste:** open this sheet once in a browser (Chrome on your phone works): File → Settings → Locale: India → Save.
2. Back in the app, tap cell A1, tap again, choose Paste. If everything lands in column A, select column A and use Split text to columns. (If you pasted before setting the locale and the dates look wrong, set it now and paste again.)
3. Add a second tab (tap + at the bottom), rename it "Prep", rename the first tab "Orders", then type the Prep formulas in B1 and B4 and copy B4 down.
4. On the Orders tab, tap the letter F, tap the Format icon (the letter A), then Conditional formatting, and add the green rule. Then select columns A to G and add the orange rule the same way.
5. Tap row number 1 and choose Freeze, so headings stay on top. Share only with people who need it.
