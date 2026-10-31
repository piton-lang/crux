# crux-ui-styles: evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project prepared as stated.

## S1. First run creates the library

- Seed a project with an application overview, one list screen and
  its domain data specified, and no style library.
- Invoke: "Show me some visual styles for this app."
- Expect: exactly three questions, one per turn, with `Question N of
  3`. Question 1 offers named directions (such as clean dashboard,
  SaaS product, technical) and recommends three; question 2 asks for
  likes, dislikes and hard limits; question 3 recommends one
  representative screen from the spec. No question asks what the spec
  already settles. Pages land at
  `spec/design/VisualStyles.styles/1.html`, `2.html`, `3.html` (or
  where the project's conventions put design rules) with `index.html`
  as the gallery. Every page is self-contained, loads nothing from the
  network, uses system fonts, shows the same screen with realistic
  content, and has a style sheet with palette values, type, spacing,
  corners and controls in normal and focus states. The styles differ
  in base, palette, type, density and shape, not only accent colour.

## S2. Recording in the specification

- Continue S1.
- Expect: before showing the gallery, the agent writes a library
  anchor with a gallery path property, one property per style
  (number, name, idea, project-root page path, verdict, and exact
  palette, type, spacing, density, corners, borders, shadows, icons
  and tone), and a `direction` property kept as an open question.
  `piton format`, `piton check` and `piton build` pass. The gallery
  shows number, name, idea and live preview per card, opens a large
  view with wide, tablet and 375px widths, previous and next, and
  Escape, and the agent asks for verdicts by number.

## S3. Verdicts, mixes and a direction

- Continue S2 and answer "favour 1 and 3, reject 2 because it is too
  loud, and mix 1 with the type from 3".
- Expect: verdicts appear in the gallery (filterable) and in the
  anchor, with the reason for 2 recorded in `direction`. The mix
  becomes style 4; styles 1 to 3 are untouched. The agent offers Done,
  More styles, and Choose a direction, and does not start designing a
  screen. Answering "choose 4 as the direction" writes plain design
  rules into `direction` that name style 4 as their source.

## S4. Growing the library later

- Continue S3 in a new session and invoke the skill again.
- Expect: the agent reads the existing library first, offers only
  directions the library does not cover, respects the recorded likes,
  dislikes and limits, and numbers new styles from 5. The gallery
  shows the new batch first, grouped by run. No existing page is
  renumbered or overwritten. If S1's batch had no verdicts, the agent
  shows it again and asks about it before starting a new batch.

## S5. Using the shipped catalogue

- Seed as S1, with crux tethered so the catalogue's
  `styles/*Style.pi` files sit under `tethers/`.
- Invoke: "Show me some dark, technical styles for this app."
- Expect: the agent finds the catalogue by file name, searches the
  name and idea lines (for example for dark and terminal) and opens
  only a few style files. The project never imports a catalogue
  anchor. Question 1's
  directions draw on what it found. The new styles adapt catalogue
  values to the project's own screen and content, and the library
  anchor never names a catalogue style. With the catalogue files
  removed, the run works the same way and says nothing about them.
