---
date: 2026-01-28 00:00:00
title: Technical Debt is Not Always Debt
---

We love to talk about technical debt. Every codebase has it. Every team accumulates it. And everyone agrees we need to pay it down. But I think we misuse the metaphor more often than not.

Real financial debt has interest. You borrow money, and over time you pay back more than you borrowed. The longer you wait, the more expensive it becomes. Some technical debt works this way. That hack you put in to ship faster? It might cost you more and more as the codebase evolves around it. That's real debt.

But most of what we call technical debt is just code we don't like anymore. That older library version? That pattern we used before we learned a better one? That's not accumulating interest. It's working fine. The cost to change it is the same today as it will be next year. That's not debt, that's just old code.

The problem with calling everything debt is that it implies urgency. Debt demands to be paid. But old code can just sit there working perfectly well. Sometimes the right decision is to leave it alone.

I think we need better language for this. Maybe we have technical debt (the stuff that gets more expensive over time), technical legacy (the old stuff that works fine but we'd do differently now), and technical rot (the stuff that's actively making things worse). Each category deserves a different strategy.

Technical debt needs to be paid down before the interest kills you. Technical legacy can wait until you have a real reason to change it. Technical rot needs to be cut out immediately.

The next time someone says "we need to pay down technical debt," maybe we should ask: is this actually accumulating interest, or is it just old? The answer changes everything about how we should prioritize it.
