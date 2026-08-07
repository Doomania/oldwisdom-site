# Reserve a separate Teen Guide stream

The existing Playbooks remain the live teen-facing product system. Parent
Growth publishing is intentionally parent-only, so `scripts/site.py` rejects
any non-parent manifest. Future teen articles or exercises will use
`content/teen-guides/` with an independent contract and renderer rather than
sharing Parent Hub templates, taxonomy, calls to action, or review gates.

This preserves the distinction between a teen tool and parent education while
leaving a clear, code-free seam for the next teen-growth surface.
