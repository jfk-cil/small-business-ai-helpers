# Example 01: a water testing lab's booking set (fictional)

**Owner types:**
> I run Sample Water Lab in Margao. People call to book a water test but then don't confirm or don't bring the sample. Customers collect a sample bottle from us, fill it at home and drop it at the lab, Monday to Saturday, 9 am to 1 pm. Remind them the day before at 6 pm and on the morning of the drop. Results go on WhatsApp in 3 working days. To change, they reply a day before. Add a review request at the end.

**Helper replies:**

I left [blank] for how much water and how to keep the sample, because those must come from your lab. If you haven't written them down yet, fill in the prep template once and paste it next time.

**Confirmation** (send only after you've checked the slot is free)
```
Hi! Your water test is booked.
Drop-off: [day and date], [time]
Where: [location link]
Please fill the sample bottle we gave you with [blank] of water.
Keep it [blank] until you bring it.
We take samples Monday to Saturday, 9 am to 1 pm.
To change it, reply here a day before.
[your business name]
```

**Reminder, the day before** (send at 6 pm)
```
Hi! A reminder: please drop your water sample tomorrow, [day and date], at [time].
Use the sample bottle we gave you, with [blank] of water.
Reply YES to confirm, or tell us if you need a new time.
[your business name]
```

**Reminder, on the day** (send in the morning)
```
Hi! See you today at [time] with your water sample.
Map: [location link]
[your business name]
```

**Please confirm** (one nudge if there's no reply)
```
Hi! We haven't heard back about your water sample drop on [day and date] at [time].
Please reply YES to keep it, or tell us a better time.
[your business name]
```

**Reschedule reply**
```
Hi! No problem. Which day and time suit you? We take samples Monday to Saturday, 9 am to 1 pm.
Let me check and confirm shortly.
[your business name]
```

**Cancellation reply**
```
Hi! Thanks for letting us know. Your water test on [day and date] is canceled.
Message us here anytime to book again.
[your business name]
```

**No-show follow-up**
```
Hi! We missed you today. Would you like a new time to drop your sample? Just reply with a day that suits you.
[your business name]
```

**After-service**
```
Hi! Thank you, we've received your water sample.
Your results will come here on WhatsApp in 3 working days.
For what your results mean, please speak to a qualified person.
If you were happy with our service, a short review would help us: [review link]
[your business name]
```

**Daily booking routine**
1. Morning: filter today's drop-offs in your sheet.
2. Morning: send each one the on-the-day reminder (/today) and mark "Reminder sent?" Yes.
3. When someone replies YES, mark "Confirmed?" Yes. No reply by [time you choose]: send /pls-confirm once.
4. Evening, 6 pm: filter tomorrow's drop-offs and send /tomorrow to each.
5. After each drop-off: mark "Done?" and send /thanks. If nobody came, send /missed.

**Save as quick replies**
- `booked` Confirmation
- `tomorrow` Reminder, the day before
- `today` Reminder, on the day
- `pls-confirm` Please confirm
- `reschedule` Reschedule reply
- `cancel` Cancellation reply
- `missed` No-show follow-up
- `thanks` After-service

How to save: in WhatsApp Business, tap ⋮ (Android) or Settings (iPhone) > Business tools > Quick replies > +. Paste the message, type the shortcut, save. In a chat, type / and the shortcut. (Menus differ a little by phone.) Labels help too: "Waiting YES", "Confirmed", "Done".

**Your booking sheet** (Google Sheet)
```
Booking code	Service	Date	Time	Where	Confirmed? (Yes/No/Waiting)	Reminder sent?	Done?	Notes
```
Use a booking code, not the customer's name. Want a name or phone column? Add it yourself in your own sheet; never type them into this chat. Tomorrow's drop-offs: select row 1, Data > Create a filter, tap the filter icon on Date, tick only tomorrow's date. To build it with formulas and colors, use **tracker-sheet-builder**.

Optional: a daily Google Calendar event for yourself, "Send tomorrow's reminders", at 6 pm. (This helper can't send anything itself.)

**Fill in before saving:** how much water goes in the bottle, how to keep the sample until drop-off, your business name, your location link and your review link.

It's a draft: you check it and send it yourself.

(Messages run from 93 to 297 characters, all under 500.)
