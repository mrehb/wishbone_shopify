# CompatibilityFinder

The component this catalogue most needs. 22 of 27 products are spare parts named
`Component (MODEL)`, and a customer arrives knowing their trolley, not the part number.

Fits per model in the live catalogue today: **ONE 10 · NEO 14 · EON 5 · TWO 2 · THREE 2**, plus four
universal accessories (ball & tee holder, scorecard holder, umbrella holder, drink holder). The
store already has `spare_one` and `spare_neo` collections and per-model product templates, so this
component is surfacing structure that exists rather than inventing it.

Never hide a model with no parts. The empty state names the gap and offers a route — "contact us
with your serial number" — because a customer with an unlisted part is a repair, not a lost sale.
TWO and THREE currently return almost nothing; that is a catalogue gap worth closing, and the
component makes it visible instead of silently returning an empty grid.
