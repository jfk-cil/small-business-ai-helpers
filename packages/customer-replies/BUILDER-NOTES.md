# Customer replies: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with a working helper on their own phone, 2 or 3 quick replies saved in WhatsApp Business, three labels, and a daily routine they believe in.

## Before you sit down

- Open https://jfk-cil.github.io/small-business-ai-helpers/customer-replies/ on your own phone, ready to demo.
- Copy the made-up message batch below into a note on your phone.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- The owner uses their own phone and their own AI account. Not yours.

## 20-minute table script

| Time | What you do |
|---|---|
| 0:00 to 2:00 | Say what it is: "It sorts your messages and drafts the routine replies. You check and send every one. It can't read your WhatsApp or reply by itself." Ask what kind of business it is and roughly how many messages a day. If you want to take notes or record, say so out loud and ask first. Only go ahead on a clear yes. |
| 2:00 to 5:00 | Demo on your phone with the made-up example below. Show "Needs you" with its holding line, the routine drafts, the quick reply, and the count. |
| 5:00 to 9:00 | The owner opens the page and answers the 4 questions. Push gently for real facts: prices or how pricing works, hours, areas covered, how to book. These are what make the drafts useful. Mic and language picker help. |
| 9:00 to 13:00 | Owner copies the helper, opens their AI, pastes and sends. Then they copy 3 to 5 real messages from WhatsApp and change each name or number to Customer 1, 2, 3 before pasting. Read the result together. Check every price against what they told you. |
| 13:00 to 17:00 | WhatsApp Business: save 2 quick replies from the result, make the three labels (Needs me, Routine, Waiting for reply), and turn on the away message. |
| 17:00 to 19:00 | Save the helper in "Message yourself". Walk through "Every day" on the playbook. |
| 19:00 to 20:00 | Agree one move for this week. Check the AI chat has no names or numbers in it; if it does, delete that chat together. |

## Demo with a made-up example

Answers to type on your phone:
- Business: "Cleaning service in Margao"
- Facts: "2BHK deep clean Rs 4,500. 3BHK Rs [blank]. We bring all supplies. Monday to Saturday. North and South Goa. Book by WhatsApp."
- Tone: "Warm and short, always say thank you"
- Needs me: "Complaints, discounts, sofa or carpet jobs, anything over 3BHK"

Then paste this made-up batch:

```
Customer 1: hi how much for 2bhk deep cleaning
Customer 2: your team left the balcony dirty yesterday, I want money back
Customer 3: price for 2bhk full cleaning pls, are you free sunday?
Customer 4: ok thanks
```

What to point out:
- Customer 2 goes to "Needs you" with a calm line that admits nothing and promises nothing.
- Customers 1 and 3 get one draft, and the price comes from the facts. Sunday isn't confirmed, because the facts say Monday to Saturday.
- The repeated price question becomes a quick reply with a shortcut.
- Customer 4 needs no reply.

## Common snags

- **Wrong language.** Change the language on the page and make the helper again, or type "Write to me in Hindi" in the chat. Drafts follow the customer's language, including Hinglish. Translations are drafts; check with someone who reads it well.
- **The owner pastes names or numbers.** Very common: WhatsApp and WhatsApp Web copy the sender's name, number and time with each message. Stop. Delete that chat (three dots > Delete) and paste again with Customer 1, Customer 2. The page checks the answers for numbers, but it doesn't see what goes into the AI.
- **The AI promises things** (a slot, a discount, "we'll be there by 10"). The helper tells it not to. If a draft still does, the owner edits it before sending. Make sure the owner fills each [blank] from their own facts.
- **"Can't it just reply for me?"** Be honest. Not this helper, and not safely with unofficial apps. See "Going further" for what a real automatic setup needs.
- **Voice notes.** The AI can't hear them. The owner types what the customer said.
- **Quick reply too long.** Ask "Make it shorter, under 300 characters."
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turning a working helper into the owner's own Skill (laptop)

Only on the owner's laptop and the owner's own Claude account, on a paid plan with code execution turned on (Settings > Capabilities).

Easiest: download the three Skills from the package page (message-sorter, guest-inquiry-replies, quote-and-proposal-writer) and upload each in Settings > Capabilities > Skills. Then, in a chat, run "Learn my tone" and "Set up my facts" once and keep both notes.

To make a Skill that already knows the owner's business:
1. Make a folder with a short lowercase name, for example `my-cleaning-replies`.
2. Inside it, make a text file called `SKILL.md` that starts like this:
   ```
   ---
   name: my-cleaning-replies
   description: Sorts customer WhatsApp messages and drafts routine replies for my cleaning service in Margao. Use when I paste customer messages or say "sort my messages".
   ---
   ```
3. Under that, paste the helper text from the phone page, then the owner's "My tone" and "My business facts" notes. Prices and hours are fine. No customer names, phone numbers, UPI ID or passwords.
4. Zip the folder (the folder itself goes inside the zip) and upload it in Settings > Capabilities > Skills.
5. Test it in a new chat with the made-up batch above.

You can also paste the helper into a Claude chat and ask Claude to turn it into a Skill; with code execution on, it can make the zip for the owner to download.

A lighter option on a paid plan: a Claude Project with the helper, tone and facts as its instructions.

## Going further (builder projects)

Be clear with the owner about size and cost before you start any of these.

- **One facts document.** A Google Doc in the owner's account with prices, hours, areas, how to book. The owner updates it, then remakes the helper and quick replies from it. Small job.
- **Automatic WhatsApp replies.** A real bot needs the WhatsApp Business Platform, usually through an approved provider, in the owner's own business account. It needs each customer's opt-in, approved message templates for messages the business starts, and a person to take over anything in "Needs you". Free-form replies are generally only allowed for a limited time after the customer writes; check the provider's current rules. There are per-message costs, and moving a number to the Platform can change how the owner uses it in the phone app. Customer messages must stay in the owner's systems. This is weeks of work plus ongoing care, not an afternoon.
- **Never** set up unofficial auto-reply apps that read phone notifications or ask the owner to scan a WhatsApp QR code in another app. They can get the number banned and they expose customers' messages.
- **A daily count.** A Google Sheet in the owner's account: date, messages sorted, how many needed them, minutes spent. Counts only, no names. It helps the owner decide if the routine is worth keeping.

## Do not

- Put the owner's data in your own accounts. No owner or customer messages in your Claude, your notes app or your phone's photos.
- Record or photograph anything without saying so out loud first and hearing a yes.
- Post the owner's name, business, phone, screenshots or customers' messages anywhere public, including GitHub issues and social media.
- Ask for or touch the owner's passwords or OTPs. They log in themselves.
- Install anything on the owner's phone that reads their WhatsApp.
- Promise results.
