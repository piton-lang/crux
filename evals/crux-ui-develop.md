# crux-ui-develop: evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project prepared as stated.

## U1. Interview kickoff and target

- Seed a project with a list page and a card component specified, and
  no mockups.
- Invoke: "Let's prototype the UI."
- Expect: the agent offers a short list of UI parts by what they are
  (not file names) and lets the user name another. Then it asks how
  many questions to use, default 5. Neither counts as a question.
  Questions arrive one per turn with `Question N of M`, never ask
  what the spec already settles, and stop at the budget. The learned
  decisions and open questions are written into the target anchor and
  `piton check` passes before any mockup is made.

## U2. A mockup round

- Continue U1, or seed a project with a specified card.
- Expect: the agent asks how many variations, default 3, and makes
  exactly that many. Files land at `<Spec>.mockups/round-1/1.html`,
  `2.html`, `3.html` next to the spec file, with `round-1/index.html`
  as the gallery and a top-level `<Spec>.mockups/index.html`. Every
  file is self-contained and loads nothing from the network. The
  gallery shows each variation's number, name, idea and a live
  preview, and opens a large view with wide, tablet and 375px widths,
  previous and next, and Escape back to the grid. Variations differ in
  layout or behaviour, not just colour, and use realistic project
  content. The agent shows the gallery path and asks which number the
  user likes.

## U3. Picking records and references

- Continue U2 and answer "2".
- Expect: the top-level index marks 2 as the pick of round 1; the
  target anchor gains or updates a `mockups` property naming the index
  and `round-1/2.html` as project-root paths; what the pick settled is
  also written as plain requirements. `piton format`, `piton check`
  and `piton build` pass. The agent offers Good enough, Another round,
  and More questions, and does not start building the UI.

## U4. Dive deeper and resume

- Continue U3, answer "dive into 2 with 4 variations", then end the
  session before picking.
- Expect: round 2 is a new folder with exactly 4 variations built on
  round 1's pick, and its gallery links back to `round-1/2.html`.
  Round 1 is untouched. In a new session, invoking the skill finds
  round 2 without a pick, shows its gallery again and asks for a
  number, without repeating answered questions.
