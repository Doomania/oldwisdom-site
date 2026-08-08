# Old Wisdom // Retold Design System

## Visual Direction

Premium dark editorial strategy guide. The site should feel like a modern field manual: calm, sharp, readable, and credible to parents while still carrying enough game-language energy for teens. The existing live site is the visual north star.

Avoid turning the brand into a generic SaaS dashboard, neon gaming interface, self-help influencer funnel, or luxury-club parody.

## Colour Roles

### Foundation

- Deep canvas: `#0C0C0F`
- Primary card: `#151519`
- Raised card: `#1C1C22`
- Warm section: `#12110F`
- Primary text: `#F5F5F5`
- Body text: `#D4D4D8`
- Secondary text: `#8E8E96`
- Muted text: `#85858F` (keeps small text and placeholders above WCAG AA contrast on the dark surfaces)
- Hairline border: `rgba(255,255,255,0.06)`

### Meaningful Accents

- Gold `#D4A84B`: brand, primary action, wisdom, and premium emphasis.
- Gold soft `#E8C878`: hover and highlighted editorial text.
- Blue `#4D94FF`: The Social Playbook, connection, and teen path.
- Red `#CC2233` / `#E84455`: The War Playbook, conflict, and warning emphasis.
- Green `#3ECF8E`: completion and positive result states.
- Purple `#A78BFA`: anxiety/confidence quiz category only.

Use accents to communicate product or state. Do not decorate every surface with glow. Prefer hairline borders, subtle tonal shifts, and quiet lighting.

## Typography

- Display: Bebas Neue. Use for concise headlines, labels, book codes, and numeric emphasis.
- Body/UI: Outfit, weights 300–700. Use sentence case for body copy and controls unless an established branded label is intentionally uppercase.
- Hero display range: `clamp(2.8rem, 7vw, 5.5rem)`.
- Section display range: `clamp(2.2rem, 5vw, 3.8rem)`.
- Body copy: 16–18px with approximately 1.6–1.8 line height and readable line lengths.
- Do not introduce additional font families.

## Layout

- Content container: 1100px maximum with fluid side padding.
- Use strong vertical rhythm and a small number of large editorial sections.
- Primary responsive breakpoints are approximately 900px, 768px, 640px, and 480px.
- Mobile layouts collapse to one column, retain 44px minimum touch targets, and keep the primary action visible without crowding the header.
- Prefer grid for product and comparison structures; prefer a single clear reading column for quiz and legal content.

## Components

### Navigation

Fixed or sticky dark translucent header with a gold wordmark. Keep the number of primary destinations low. On the canonical homepage, preserve the book-and-quiz hierarchy and add one durable Parent Hub route; do not add a new homepage navigation item for every guide. Blue and red identify the two Amazon books, while gold identifies the primary action and Parent Growth editorial emphasis.

### Buttons

- Primary: gold fill, deep text, 48px minimum height, modest 8–10px corner radius.
- Secondary: transparent or dark fill with a quiet border.
- Social product action: blue where it identifies The Social Playbook.
- War product action: red where it identifies The War Playbook.
- Hover movement is subtle and never required to understand state.

### Cards

Dark surfaces with a hairline border and 10–16px radius. Use hierarchy through spacing, copy, and product colour. Avoid stacks of decorative containers and excessive side-tab accents.

### Forms

Inputs use a dark translucent surface, clear labels, visible gold focus rings, useful error text, and explicit consent/fine print. Never remove labels for visual convenience; visually hidden labels are acceptable when the placeholder repeats the same short prompt.

### Quiz Results

Profiles use colour plus text, never colour alone. Gap recommendations should name the skill, explain why it matters, give one small practice, and lead to one matched next action.

## Motion

- Use the existing smooth ease `cubic-bezier(0.23, 1, 0.32, 1)`.
- Reveal motion should be short, subtle, and optional.
- Support `prefers-reduced-motion`; content must never remain hidden when motion is reduced or scripts fail.
- Use transforms and opacity for animation. Avoid layout-property animation where practical.

## Imagery

Book covers and the three-book mockup are the primary brand imagery. Author photography is supporting credibility, not the visual centre of the site. Parent Hub imagery should be calm, specific editorial context rather than generic stock photography or abstract AI gradients.

## Decision Principles

- One dominant next step per viewport or decision block.
- For a Parent Guide, choose the next step because it helps the reader, not because it forces a product path.
- Use honest proof: book contents, sample pages, quiz fit, author context, sources, and specific practices.
- Keep Amazon Playbooks visible as relevant teen tools. They are never an automatic Parent Hub destination.
