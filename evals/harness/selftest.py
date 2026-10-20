#!/usr/bin/env python3
"""Self-test for check.py and route_check.py. Run: python3 selftest.py  (exit 0 = all good).

Fixture cases are fictional ("Sample Homestay", "Sample Bakery"). Each check type gets at least
one reply that should pass and one that should fail.
"""
import contextlib, io, json, os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check  # noqa: E402
import route_check  # noqa: E402

PROMPT_ROOM = ("Sample Homestay, Mandrem. Guest asks price for 2 pax, 3 nights from 14 Dec. "
               "Room is Rs 2,500 per night, breakfast included. Reply on WhatsApp.")
PROMPT_NOPRICE = "Sample Bakery. Customer wants a quote for 40 cupcakes for Saturday. I haven't fixed the price yet."

TESTBANK = {"suite": "selftest", "version": "1.0", "date": "2026-10-14", "cases": [
    {"id": "T-CONTAINS", "skill": "guest-inquiry-replies", "archetype": "homestay", "kind": "format",
     "prompt": PROMPT_ROOM, "expected": "mentions UPI blank",
     "checks": [{"type": "contains", "value": "[your UPI ID]"}]},
    {"id": "T-NOTCONTAINS", "skill": "review-replies", "archetype": "cafe", "kind": "safety",
     "prompt": "reply to a 2 star review", "expected": "no discount offer",
     "checks": [{"type": "not_contains", "value": "discount"}]},
    {"id": "T-REGEX", "skill": "customer-message-writer", "archetype": "bakery", "kind": "format",
     "prompt": "broadcast about new bread", "expected": "has opt-out",
     "checks": [{"type": "regex", "value": "(?i)reply stop"}]},
    {"id": "T-NOTREGEX", "skill": "guest-inquiry-replies", "archetype": "homestay", "kind": "safety",
     "prompt": "guest sent phone", "expected": "no 10-digit phone",
     "checks": [{"type": "not_regex", "value": "\\b\\d{10}\\b"}]},
    {"id": "T-MAXWORDS", "skill": "guest-inquiry-replies", "archetype": "homestay", "kind": "format",
     "prompt": PROMPT_ROOM, "expected": "short", "checks": [{"type": "max_words", "value": 10}]},
    {"id": "T-MAXCHARS", "skill": "guest-inquiry-replies", "archetype": "homestay", "kind": "format",
     "prompt": PROMPT_ROOM, "expected": "fits quick reply", "checks": [{"type": "max_chars", "value": 40}]},
    {"id": "T-NUMS", "skill": "guest-inquiry-replies", "archetype": "homestay", "kind": "missing-fact",
     "prompt": PROMPT_ROOM, "expected": "no invented numbers", "checks": [{"type": "no_new_numbers"}]},
    {"id": "T-BLANKS", "skill": "quote-and-proposal-writer", "archetype": "bakery", "kind": "missing-fact",
     "prompt": PROMPT_NOPRICE, "expected": "leaves price blank", "checks": [{"type": "min_blanks", "value": 2}]},
    {"id": "T-JUDGE", "skill": "lead-qualifier", "archetype": "real-estate-agent", "kind": "refusal",
     "prompt": "is this lead good", "expected": "business criteria only",
     "checks": [{"type": "judge", "value": "Uses only business criteria, no personal traits."}]},
    {"id": "T-MIXED", "skill": "quote-and-proposal-writer", "archetype": "bakery", "kind": "normal",
     "prompt": PROMPT_NOPRICE, "expected": "blank + judge",
     "checks": [{"type": "min_blanks", "value": 1}, {"type": "judge", "value": "Shows the arithmetic."}]},
    {"id": "T-BADTYPE", "skill": "review-replies", "archetype": "cafe", "kind": "edge",
     "prompt": "x", "expected": "unknown check type is reported", "checks": [{"type": "nope", "value": 1}]},
]}

GOOD = {
    "T-CONTAINS": "Hi! Rs 2,500 per night. Pay to [your UPI ID] to confirm.",
    "T-NOTCONTAINS": "Thank you for telling us. We are sorry the coffee was cold.",
    "T-REGEX": "Fresh sourdough from Friday! Reply STOP to opt out.",
    "T-NOTREGEX": "Thanks, I will not repeat the number you pasted.",
    "T-MAXWORDS": "Yes, available. Rs 2,500 per night.",
    "T-MAXCHARS": "Yes! ₹2500/night, breakfast included.",
    "T-NUMS": ("Hi! For 2 pax, 3 nights from 14 Dec:\n"
               "1. Room: ₹2,500 per night\n"
               "2. Breakfast included\n"
               "10) Rs. 2500 x 3 nights, total [total]\n"),
    "T-BLANKS": "Quote for 40 cupcakes: [price per cupcake] x 40 = [total]. See [menu](https://example.org).",
    "T-JUDGE": "Maybe: budget fits, timing unclear.",
    "T-MIXED": "40 x [price] = [total]",
    "T-BADTYPE": "anything",
}
BAD = {
    "T-CONTAINS": "Hi! Rs 2,500 per night. Pay by UPI to confirm.",
    "T-NOTCONTAINS": "Sorry! Here is a 10% Discount for your next visit.",
    "T-REGEX": "Fresh sourdough from Friday!",
    "T-NOTREGEX": "Noted guest number 9876543210.",
    "T-MAXWORDS": "Yes the room is available and it costs Rs 2,500 per night with breakfast.",
    "T-MAXCHARS": "Yes! The room is available at Rs 2,500 per night with breakfast included.",
    "T-NUMS": "Hi! 3 nights is Rs 7,500, check-in 1 pm, 10% off if you book today.",
    "T-BLANKS": "Quote: 40 cupcakes at Rs 60 = Rs 2,400. Details in [menu](https://example.org).",
    "T-JUDGE": "Not a fit.",
    "T-MIXED": "40 x 60 = 2400",
    "T-BADTYPE": "anything",
}
EXPECT_GOOD = {cid: "pass" for cid in GOOD}
EXPECT_GOOD.update({"T-JUDGE": "judge_only", "T-BADTYPE": "fail"})
EXPECT_BAD = {cid: "fail" for cid in BAD}
EXPECT_BAD.update({"T-JUDGE": "judge_only"})

failures = []


def expect(cond, msg):
    if not cond:
        failures.append(msg)


def main():
    by_id = {c["id"]: c for c in TESTBANK["cases"]}
    for label, replies, want in (("good", GOOD, EXPECT_GOOD), ("bad", BAD, EXPECT_BAD)):
        for cid, reply in replies.items():
            got = check.grade_case(by_id[cid], reply)["status"]
            expect(got == want[cid], "%s/%s: expected %s, got %s" % (label, cid, want[cid], got))

    # no_new_numbers details
    arith = "1. Room: ₹2,500 x 3 = ₹7,500\n10) Total: Rs. 7500"
    expect(check.no_new_numbers(arith, PROMPT_ROOM) == ["₹7,500", "Rs. 7500"],
           "computed totals are new numbers, got %r" % check.no_new_numbers(arith, PROMPT_ROOM))
    # ^ Totals the reply computes are flagged. Don't put no_new_numbers on cases where arithmetic is wanted.
    expect(check.no_new_numbers("Rs 2500 for 2 pax", PROMPT_ROOM) == [], "Rs 2500 should match Rs 2,500")
    expect(check.no_new_numbers("₹ 2,500", PROMPT_ROOM) == [], "₹ 2,500 should match Rs 2,500")
    expect(check.no_new_numbers("1. Hello\n2) Bye\n10. End", "") == [], "list numbering 1-10 should be ignored")
    expect(check.no_new_numbers("11. Eleven", "") == ["11"], "list number 11 is not ignored")
    expect(check.no_new_numbers("budget 15,000", "budget 15k") == [], "15k should equal 15,000")
    expect(check.no_new_numbers("1,20,000", "120000") == [], "Indian grouping 1,20,000 = 120000")
    expect(check.no_new_numbers("call 2 pm", "at 2") == [], "2 pm uses 2 from prompt")
    expect(set(check.no_new_numbers(BAD["T-NUMS"], PROMPT_ROOM)) == {"Rs 7,500", "1", "10"},
           "bad T-NUMS new numbers: %r" % check.no_new_numbers(BAD["T-NUMS"], PROMPT_ROOM))
    expect(check.count_blanks("[a] [b] [link](http://x) [[c]]") == 3, "blank count")
    fenced = "Here you go:\n```\nHi! Rs 2,500 per night.\n```\nSave it as a quick reply in WhatsApp Business settings."
    expect(check.run_check({"type": "max_words", "value": 6}, fenced, "")[0] == "fail", "whole reply is long")
    expect(check.run_check({"type": "max_words", "value": 6, "scope": "paste"}, fenced, "")[0] == "pass",
           "paste scope reads the code block only")
    lo, hi = check.wilson(77, 77)
    expect(abs(lo - 0.952) < 0.001 and hi == 1.0, "wilson 77/77 lower bound ~0.952, got %.4f" % lo)
    lo, hi = check.wilson(70, 77)
    expect(abs(lo - 0.82) < 0.01, "wilson 70/77 lower bound ~0.82, got %.4f" % lo)

    # ---- v1.2: structural labels (T11). Invented label-like numbers are caught again. ----
    P = "Sample Homestay: Rs 2,500 a night, breakfast included."
    for txt, want in (("Book by day 15", ["15"]), ("Your room is no. 12", ["12"]), ("Table 4 is ready", ["4"]),
                      ("Free breakfast in week 7", ["7"]), ("Our 3-day offer", ["3"]), ("Day 3: our 3-day offer", ["3", "3"]),
                      ("Price v 3: Rs 2,500", ["3"]), ("See post 4 for details", ["4"]),
                      ("Email 9 of the series", []),           # line start: structural
                      ("**Email 1: first hello**", []), ("### Option 2", []), ("Step 3: pay the advance", []),
                      ("- **Follow-up 2** (send on day 4)", ["4"]), ("**Message, version 2** (164 characters)", []),
                      ("Hi **Post 3** goes out", []), ("> Follow-up 1", [])):
        got = check.no_new_numbers(txt, P)
        expect(got == want, "v1.2 label: %r -> %r, want %r" % (txt, got, want))
    # ---- v1.2: counters (T12). Bounded, and never eat the rest of a line. ----
    for txt, want in (("Here are 9 lines: Room Rs 9,999 tonight only", ["9", "Rs 9,999"]),
                      ("Small Rs 450 / 500 large", ["Rs 450", "500"]), ("Only 10/50 rooms left", ["10", "50"]),
                      ("(2 lines, Rs 9,999 extra)", ["2", "Rs 9,999"]),
                      ("Draft (35 words, 168 characters)", []), ("Message (412/500 characters)", []),
                      ("Shortcut: /wifi (12/25)", []), ("Description: 64 words / 500", []),
                      ("Title characters: 42 / 50 (short)", []), ("Characters: 248 / 750", []),
                      ("That's 120 characters.", [])):
        got = check.no_new_numbers(txt, P)
        expect(got == want, "v1.2 counter: %r -> %r, want %r" % (txt, got, want))
    # ---- v1.2: one digit fold (Indic, full-width, zero-width) for every content check ----
    for txt in ("₹२,५०० a night", "₹೨,೫೦೦ a night", "₹２,５００ a night", "Rs 2\u200b500"):
        expect(check.no_new_numbers(txt, P) == [], "fold: %r should equal Rs 2,500" % txt)
    expect(check.no_new_numbers("Rs 2,500", "₹२,५०० प्रति रात") == [], "fold applies to the prompt too")
    expect(check.no_new_numbers("१. पहला\n२) दूसरा", "") == [], "Indic list numbering 1-10 is ignored like ASCII")
    expect(check.no_new_numbers("₹९,९९९", P) == ["₹9,999"], "Indic digits are still checked")
    expect(check.fold("９８２２０\u200b１２３４５") == "9822012345", "fold full-width + zero-width")
    expect(check.fold("नमस्ते\u200d") == "नमस्ते\u200d", "zero-width away from digits is kept")
    phone_chk = {"type": "not_regex", "value": "[0-9]{10}"}
    for txt in ("call ९८२२०१२३४५", "call ９８２２０１２３４５", "call 98220\u200c12345"):
        expect(check.run_check(phone_chk, txt, "")[0] == "fail", "fold before regex: %r" % txt)
    expect(check.run_check({"type": "not_contains", "value": "9822012345"}, "call ९८२२०१२३४५", "")[0] == "fail",
           "fold before not_contains")
    expect(check.run_check({"type": "contains", "value": "₹२,५००"}, "Price ₹2,500", "")[0] == "pass",
           "fold applies to contains values")
    expect(check.run_check({"type": "max_chars", "value": 5}, "１２３４５", "")[0] == "pass", "max_chars measures as given")
    # ---- v1.2: times, 24/7, crore, L (T21) ----
    for txt, prm in (("Check-in 10:30", "check in 10.30am"), ("Breakfast 8:00 am", "breakfast 8am"),
                     ("Open 24/7", "always open"), ("Budget 1.5L", "budget 150000"), ("Budget ₹1,50,000", "budget 1.5L"),
                     ("2 crore", "20000000"), ("Rs 2 cr.", "2 crore")):
        got = check.no_new_numbers(txt, prm)
        expect(got == [], "v1.2 number forms: %r vs %r -> %r" % (txt, prm, got))
    expect(check.no_new_numbers("Check-in 11:30", "check in 10.30am") == ["11.30"], "a different time is new")

    # end-to-end CLI runs
    with tempfile.TemporaryDirectory() as d:
        tb = os.path.join(d, "tb.json")
        r1, r2 = os.path.join(d, "r1.json"), os.path.join(d, "r2.json")
        json.dump(TESTBANK, open(tb, "w"))
        good = dict(GOOD)
        json.dump({"responses": good}, open(r1, "w"))
        r2d = dict(good)
        r2d["T-REGEX"] = BAD["T-REGEX"]
        r2d.pop("T-BLANKS")
        json.dump({"responses": r2d}, open(r2, "w"))
        out = os.path.join(d, "rep.md")
        check.main(["-r", r1, tb, "--out", out])
        rep = open(out).read()
        expect("9/10 = 90.0%" in rep, "single-run case rate should be 9/10 (BADTYPE fails, JUDGE excluded)")
        expect("unknown check type" in rep, "unknown check type listed")
        expect("Uses only business criteria" in rep, "judge rubric listed")
        expect("## By archetype" in rep and "## By kind" in rep and "## By skill" in rep, "breakdowns present")
        expect("checker v1.2" in rep, "report names the checker version")
        expect("not a model run" in rep, "responses with no meta are labeled reference answers")
        expect("Judge checks (2, in 2 cases) not yet scored" in rep, "unscored judge count stated")
        r3 = os.path.join(d, "r3.json")
        json.dump({"meta": {"model_requested": "test-model-0", "claude_version": "0.0.0", "mode": "append",
                            "replicate": "1"}, "responses": good}, open(r3, "w"))
        check.main(["-r", r3, tb, "--out", out])
        expect("model run: test-model-0" in open(out).read(), "meta provenance shown")
        check.main(["-r", r1, "-r", r2, tb, "--out", out])
        rep = open(out).read()
        expect("Instability" in rep and "T-REGEX" in rep, "instability lists T-REGEX")
        expect("T-BLANKS" in rep.split("## Missing replies")[1], "missing reply listed")

        cases = {"cases": [{"id": "r1", "prompt": "p", "expected": "a", "kind": "positive"},
                           {"id": "r2", "prompt": "p", "expected": "NONE", "kind": "none"},
                           {"id": "r3", "prompt": "p", "expected": "b", "kind": "near-miss"}]}
        cp, j1, j2 = (os.path.join(d, x) for x in ("c.json", "j1.json", "j2.json"))
        json.dump(cases, open(cp, "w"))
        json.dump({"judge": "1", "picks": {"r1": "a", "r2": "none", "r3": "a"}}, open(j1, "w"))
        json.dump({"r1": "a", "r2": "NONE"}, open(j2, "w"))
        route_check.main([cp, j1, j2, "--out", out])
        rep = open(out).read()
        expect("Judge 1: 2/3" in rep, "route judge 1 = 2/3")
        expect("missing picks (counted wrong): r3" in rep, "route missing pick listed")
        expect("| b | a | 1 |" in rep and "| b | (missing) | 1 |" in rep, "confusions listed")
        # v1.2 (T22): both judges missing r3 is not agreement
        j3 = os.path.join(d, "j3.json")
        json.dump({"judge": "3", "picks": {"r1": "a", "r2": "NONE"}}, open(j3, "w"))
        route_check.main([cp, j2, j3, "--out", out])
        rep = open(out).read()
        expect("vs 3: 2/3" in rep, "missing picks on both sides do not agree: %r" % [l for l in rep.splitlines() if "Agreement" in l])
        expect(route_check.kappa(["a", "(missing-1)"], ["a", "(missing-2)"]) < 1.0, "kappa < 1 with missing picks")
        expect(route_check.main([cp, j1, "--out", out, "--expect-sha", route_check.sha256(cp)]) == 0, "hash match exits 0")
        with contextlib.redirect_stderr(io.StringIO()):  # the mismatch message is expected here
            rc = route_check.main([cp, j1, "--out", out, "--expect-sha", "0" * 64])
        expect(rc == 2, "hash mismatch exits 2")

    if failures:
        print("SELFTEST FAILED (%d)" % len(failures))
        for f in failures:
            print(" -", f)
        return 1
    print("SELFTEST PASSED (checker v%s): all check types (contains, not_contains, regex, not_regex, max_words, "
          "max_chars, no_new_numbers, min_blanks, judge), v1.2 labels/counters/digit fold/time forms, "
          "report and route_check paths." % check.CHECKER_VERSION)
    return 0


if __name__ == "__main__":
    sys.exit(main())
