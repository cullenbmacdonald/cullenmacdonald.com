---
date: 2024-01-27 00:00:00
title: Things To Follow
---

- Getting PR’s merged and deployed takes a higher priority than coding
- A ticket is not done until it is in prod
- An epic is not done until all tickets in the epic are done
- A feature is not done until a customer is using it.
- Engineers shouldn’t have more than two Jira tickets in progress (in progress, in review, waiting for merge) at a time 
- One Jira ticket = One PR
    - If you find yourself needing to open a second PR, take a little extra time to make a separate ticket for the second PR.
- All PRs must target `main`
    - why? Read this: [Bottlenecks and Pull Requests](/bottlenecks-and-pull-requests)
- No free floating tickets. all tickets are part of an epic
    - Joanna Honikman: "if it’s not in Jira, it’s not happening. I’ve seen teams do a bunch of 'quick' things saying, 'We don’t need a ticket…' only to find they did 20 'quick' things and nothing else. If it’s important enough to do instead of all the other work, it should be in a ticket, and it should roll up to something tangible."
- Product managers are the arbiters of whether an epic contains enough value on its own to be an epic or not. (may not be correct)
- Squads set weekly epic delivery goals. (one epic per week eg). The goal is consistency however small, even over end-of-quarter massive goals being hit. Consistency is the easiest path to predictability. (momentum, trust, ease of planning). - All tickets from an epic should be brought into the sprint. 
- Big projects getting to 95% done by Friday are worthless. a small project to 100% done by the end of the week is everything. (hyperbolic…)
- We don’t use story points on tickets.
    - why? Read this: [Velocity and Story Points](/velocity-and-story-points)
- No ticket should be estimated to take longer than three business days to merge. 
    - If you have a ticket that takes longer than three days, figure out how to get what youve done so far merged, and make a new ticket for the rest. Try to avoid “one more day and then _today_ it gets merged. 
    - A PR with a single concept is much easier to review accurately & quickly than one with several things all smooshed together even if they are part of the same feature. Atomic commits are also very, very helpful for reviewers.