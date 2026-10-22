# Setups with no AI

For owners, on your phone. These tools are free and do most of the daily work. AI only helps you write the words once. Your customers' details stay in your own apps.

**Menus change.** Names below are as of October 2026. If a step doesn't match your phone, look for a similar word in the app, or check the app's own help pages.

Need help at a table? A builder can sit with you ([COACHING.md](COACHING.md)). Ready-made routines that use these tools: [customer messages](../skills/customer-messages-routine/), [weekly posts](../skills/weekly-posts-routine/), [staff checklists](../skills/staff-checklist-routine/), [get paid on time](../skills/get-paid-routine/).

## 1. WhatsApp Business (about 20 minutes)

Use the free **WhatsApp Business** app (its icon has a "B"). Moving from plain WhatsApp? Back up your chats first, then follow the app's own steps. Moving your main number is your choice.

The settings live under **Business tools**: on Android, tap the three dots, then **Business tools**; on iPhone, **Settings**, then **Business tools**. Some phones show a **Tools** tab instead.

**Quick replies** (answers you send with a shortcut)
1. Business tools, then **Quick replies**, then **+**.
2. Type your real answer to one question you get every day. Add a shortcut word, for example `price`.
3. Save. In any chat, type `/` and the shortcut, then check it and send.
4. Make one for each of your 3 to 5 most-asked questions: price, hours, area, how to book.

**Labels** (sort chats without reading them twice)
1. Press and hold a chat, then tap the label icon (or the three dots, then **Label chat**).
2. Make up to six: **New**, **Replied**, **Follow up**, **Booked**, **Not now**, **Payment due**.
3. Tap a label in the chat list to see only those chats.

**Greeting message** (first message to a new customer)
1. Business tools, then **Greeting message**, switch it on.
2. Keep it short. Don't promise a reply time. For example: "Thanks for writing to [business]. Tell us what you need and we'll reply soon."

**Away message** (when you're closed)
1. Set your hours first: Business tools, then **Business profile**, then **Hours**.
2. Business tools, then **Away message**, switch it on, choose **Outside of business hours**.
3. For example: "Thanks for your message. We're closed now and will reply when we're back: [your hours]."

**Catalog** (what you sell, with photos)
1. Business tools, then **Catalog**, then **Add new item**.
2. Add a photo you took, a name, a short description and a price if you publish one.
3. Items may be reviewed by the app before they show. Some kinds of goods aren't allowed; the app says which.
4. Share an item into a chat instead of typing the same description again.

**Short link** (one link people tap to message you)
1. Business tools, then look for **Short link** or a **Share** option in your business profile.
2. Copy it into your Google profile, your Instagram bio and printed cards.
3. If your app doesn't show one, a link in the form `wa.me/` followed by your full number with country code (no plus sign, no spaces) works the same way.

**Where AI helps:** "Make this answer shorter and friendlier, under 300 characters: [your answer]." Never paste a customer's message with their name or number.

## 2. Google Forms for bookings or inquiries (about 20 minutes)

A form collects the same few facts from every customer, straight into your own sheet.

1. On your phone's browser, open forms.google.com and sign in with your own Google account. Tap **+** (blank form).
2. Title: "Book a [service]" or "Ask us a question".
3. In the description, add a consent line, for example: "We use your answers only to reply to this request. They stay in our own records and we delete them after [blank] months. Please don't send ID, health or payment details here."
4. **Ask only what you need.** Usually: what service, which date, what time, which area, how many people or rooms, and how to reach you (WhatsApp or email). Use multiple choice or dropdowns where you can.
5. **Never add questions for:** Aadhaar, PAN, passport or Form C details, health or medical details, bank, UPI or card details, age, religion, caste or marital status. Don't add a file upload question; it asks people to sign in and stores their files in your account.
6. Open **Settings** (the gear or **Settings** tab). Under **Responses**, set **Collect email addresses** to **Do not collect** unless you really need it.
7. Open **Responses** and choose **Link to Sheets**. Answers now land in your own Google Sheet.
8. Tap **Send**, then the link icon, tick **Shorten URL**, and copy. Add it to your quick replies and your Google profile.
9. Test it once with made-up details, then delete that test row.

The form never books anything by itself. You read each answer, confirm by message, and then mark it in your sheet. Never paste form answers into an AI.

## 3. Google Sheets with a "due today" view (about 15 minutes)

One sheet shows what you must do today: follow-ups, payments due, returns, renewals.

1. Open the Google Sheets app and create a blank sheet. Name it "My jobs".
2. Row 1 headings: **Date added**, **Job**, **Due**, **Status**.
3. **Job** is the work, never the customer's name: "2BHK deep clean, Calangute", "Cake order, Saturday", "Deposit for room 2". Use dates in the **Due** column. **Status** is "Open" or "Done".
4. Add a second tab (the **+** at the bottom) and name it "Today". In cell A1, type:

   ```
   =IFERROR(FILTER('Sheet1'!A2:D, 'Sheet1'!C2:C<>"", 'Sheet1'!C2:C<=TODAY(), 'Sheet1'!D2:D<>"Done"), "Nothing due today")
   ```

   If your first tab has another name, use that name instead of Sheet1. This shows every open job due today or earlier.
5. Check dates read the way you write them: on a laptop, **File**, then **Settings**, then **Locale** (for example India).
6. **Share with no one.** Never "Anyone with the link". If staff need it, share only with their own accounts, and never put names or numbers in it.
7. Each morning, open the **Today** tab. Do each job, then type "Done" in **Status** on the first tab.

Money records (sales, takings, money owed) belong in your accounts book or software, with your accountant. This sheet is for jobs and due dates only.

**Where AI helps:** the [tracker-sheet-builder Skill](../skills/tracker-sheet-builder/) can design columns for your job. Describe the job; never paste the rows.

## 4. Google Calendar reminders to yourself (5 minutes)

1. Open Google Calendar and tap **+**, then **Event**.
2. Title it with the job, never a name or number: "Follow up: sofa clean quote", "Open Payment due label", "Post 3 photos".
3. Set the day and time. Tap **Add notification** and pick when you want reminding.
4. For routines, tap **Does not repeat** and choose **Every week**.
5. Keep it in your own calendar, shared with no one.

Good weekly reminders: check the **Follow up** label, check the **Today** tab, update quick replies, post this week's photos.

## 5. Google Business Profile basics (30 minutes, plus waiting for verification)

This is how people find you on Google Search and Maps.

1. Open Google Maps and search for your business name. If it shows, tap **Own this business?** or **Claim this business**. If not, open your profile picture menu and look for **Add your business**.
2. Follow the steps to verify. Google picks the method (for example a short video of your place, a phone call or a text message). Don't film people. Verification can take days.
3. Once verified, check and fill in:
   - **Category:** the main thing you do.
   - **Hours,** plus special hours for holidays and festivals.
   - **Phone and website:** your business number, and your short WhatsApp link or one-page shop link.
   - **Services or products,** with prices only if you publish them.
   - **Photos:** your place, your work, your products. No faces without the person's permission, never children's faces.
4. Reply to reviews, short and polite. Never mention the customer's booking dates, room, order, payment or refund in public.
5. Once a month, check that hours, phone and links are still right, and add two new photos.

**Where AI helps:** the [get found on Google](../packages/get-found-on-google/) package writes your description, services and review replies. Paste a review without the reviewer's name.

## Never type into any AI

Customers' names and phone numbers, passport, Form C, Aadhaar or PAN details, bank, UPI or card details, passwords and OTPs, health information, staff ID numbers and wages, family members' details, money records, photos of people. Full list: [PRIVACY.md](PRIVACY.md).

Free to use and adapt (CC0).
