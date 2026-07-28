# 11 — Forms & Lead Capture

## Principle

**The phone is the primary channel.** In this market, most people who want a roof estimate will call. The form exists for the people who won't — after hours, at work, or those who just prefer not to talk to a stranger. Build the form well, but never let it crowd out the phone number.

---

## The estimate form

### Fields — five, maximum

| Field | Type | Required | Notes |
|---|---|---|---|
| Name | text | ✅ | Single field. Not first + last. |
| Phone | tel | ✅ | `inputmode="tel"`. The most important field — this is how the owner follows up. |
| Email | email | ❌ | Optional. Requiring it costs submissions. |
| Town | select | ✅ | Dropdown of service-area towns + "Other" |
| What do you need? | select | ✅ | Metal roof · Roof repair · Board & batten siding · Metal siding · Pole barn / building · Commercial · Not sure yet |
| Tell us about it | textarea | ❌ | Optional. Optional fields get filled by motivated leads and skipped by everybody else — which is useful signal. |

**Every field beyond five measurably reduces submissions.** Do not add "How did you hear about us," "Best time to call," "Property type," or a budget range. The owner can ask on the callback.

### Behavior

- Real `<label>` above every field. Never placeholder-as-label.
- Inline validation on blur, not on every keystroke. Errors below the field, in `--error`, with an icon, announced via `aria-live="polite"`.
- Submit button says **"Get My Free Estimate"** — not "Submit."
- Loading state on submit; disable the button to prevent double-posts.
- On success: redirect to `/thank-you/` (a real URL, so it's trackable as a conversion event).
- On failure: keep the entered data, show a clear error, and display the phone number as a fallback. Never silently drop a lead.
- No CAPTCHA. It suppresses real submissions more than it stops spam at this volume.

### Spam handling

1. **Honeypot field** — a hidden input named something plausible like `company_website`, visually hidden with CSS (not `display:none`, which some bots detect). If it's filled, silently discard.
2. **Time trap** — record form render time; discard submissions completed in under 3 seconds.
3. **Host-level spam filtering** — Netlify Forms and Cloudflare Turnstile both offer invisible filtering. Turnstile is preferable to reCAPTCHA: no user interaction, better privacy, no Google dependency.

That combination handles essentially all form spam at this scale without ever asking a homeowner to identify a traffic light.

---

## Delivery

**The lead must reach the owner within seconds, on the device the owner actually uses.**

Recommended: form → host's form handler → email **and** SMS notification.

```
Primary:   Email to {{EMAIL}}, subject: "New estimate request — [Name], [Town]"
Secondary: SMS to {{PHONE}} — "New lead: [Name], [Town], [Service]. [Phone]"
```

SMS matters here. A contractor on a roof will see a text hours before an email. If the host doesn't support SMS directly, a Zapier/Make webhook to Twilio, or a simple email-to-SMS gateway, works.

**Also:** auto-reply to the customer if they provided an email —
> "Thanks — we got your request. We'll call you back within `{{RESPONSE_TIME}}`. If you need us sooner, call `{{PHONE}}`."

Managing expectations here directly reduces the number of leads who call three competitors while waiting.

### Implementation options (developer's choice)

| Host | Approach | Cost |
|---|---|---|
| Netlify | Netlify Forms — `data-netlify="true"`, zero backend | Free to 100/mo |
| Cloudflare Pages | Pages Function → email API (Resend, MailChannels) | Free tier generous |
| Any static host | Formspree, Web3Forms, Basin | Free tiers available |

All are fine. Choose based on the host. **Do not build a custom server for a contact form.**

---

## Phone-first design

- **Header:** phone number visible on every page, tap-to-call on mobile, formatted `(276) XXX-XXXX` for readability.
- **Sticky mobile bar:** 50% `📞 Call Now`, 50% `Free Estimate`. Present on every page below 768px.
- **Every CTA band:** phone button first, form button second.
- **Footer:** phone, prominent.
- **`tel:` link format:** `<a href="tel:+12765550100">(276) 555-0100</a>` — E.164 in the href, human-readable in the text.
- **Track every `tel:` click** as an analytics event. Without call tracking, this is the only visibility into phone conversions — and phone will be the majority of leads.

---

## Conversion tracking

| Event | Trigger | Why |
|---|---|---|
| `phone_click` | Any `tel:` link click | Primary conversion proxy |
| `form_submit` | `/thank-you/` pageview | Secondary conversion |
| `estimate_page_view` | `/free-estimate/` view | Funnel top |
| `email_click` | Any `mailto:` click | Minor |
| `gallery_engagement` | Gallery filter or lightbox use | Interest signal |

Mark `phone_click` and `form_submit` as key events (conversions) in GA4. Reviewing which pages precede them tells the owner where to invest content effort next.

---

## Lead follow-up (owner-side, but it affects rankings)

Worth telling the owner explicitly, because it's the highest-leverage thing outside the website itself:

**Speed of response is the single biggest determinant of whether a lead closes.** In home services, calling back within an hour dramatically outperforms calling back the next day — most homeowners contact two or three contractors and go with whoever calls first and seems competent. A slow callback loses jobs the website already earned.

It also matters for Google specifically: response speed and engagement on Google Business Profile messages and calls feed into local ranking signals. Missed calls that never get returned are a visible negative.

Practical suggestions: return every call the same day. If the owner can't answer during work, set a voicemail greeting that states a callback window, and check it at lunch and at end of day. Enable messaging on the Google Business Profile only if it will actually be monitored — an unanswered message channel is worse than a disabled one.
