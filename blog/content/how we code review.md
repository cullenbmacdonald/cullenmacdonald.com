---
lastmod: '2024-11-27 13:22:51'
title: How We Code Review
---

> This has been written and rewritten a couple times for a handful of different teams. Consider it a starting place/template

All of our engineering work makes it to production by first passing through a code review. No line of code is too small or inconsequential to bypass this part of our product lifecycle. We should be aiming for quick turn around on code review and merging/deploying. Firstly, it feels great to have momentum on work. Secondly, it prevents existing work from getting stale, rotting away in a PR. But most importantly, work isn’t done until it is merged, so helping your coworkers get their things across the line is the most important thing you can be doing!

## Opening a Pull Request
When opening a pull, a few things will help get quick and actionable feedback.
1. Use the PR template that is added by default
	1. . Reference the ticket
	2. provide a test plan with relevant login info and environment preparation
2. Give yourself a code review. How embarrassing would if be if you've been complaining that no one is looking at your PR and then there's a really silly oopsie daisy right there you could have found if you looked?
    1. Test your own test plan line for line.
    2. Go through your diff, add some comments for the other reviewers if there is some noise they can "ignore" or things worth calling out.
    3. If your PR contains a migration, ensure it doesn’t conflict with migrations other folks are working on. Made changes to the API? Make sure they wont break support for employee app or tools
3. Add at least two code reviewers. We’re still building all new stuff and it's important to make sure more than just one other person sees the foundations you're building.

## Giving a Code Review
A code review is our first line of defense when it comes to shipping high quality software. It also ensures a ticket soars through any non-engineering testing and goes to production faster. Reviewing code should be ~50% of your "code related duties" and you should feel a sense of accomplishment if you spend a whole afternoon just reviewing pull requests.

1. Look at the ticket the work was for. Having an understanding of the goal of the ticket is the first step to making sure the work was done correctly
2. Go through the test plan in the ticket. Make sure it works! This is before you've even looked at any code at all.
3. Review the code
	1. Provide helpful comments on syntax, organization, and performance
	2. We are still a small team, sometimes its ok to ask someone to answer a question in person instead of leaving a comment on their pull
4. If you are assigned, you need to review!
	1. Please don't let 24 hours pass before completing the review
	2. If you are unable for any reason to give the code review, let the person know as soon as possible

## How to get feedback
1. Give it a second. People have other work they are probably finishing up, take the break you have to go give some rock solid code reviews. Earn some good will and bargaining chips!
2. Use standup. Standup is the premium opportunity to tell people you will need code review. If your ticket is on the critical path, they should be more than happy to prioritize code review that day
3. When all else fails, send an invite to block time on people’s calendars to code review your work.

---
Origin:  Wrote the first version at [[The Wing]]
References:  [[Code Review]]
Tags: #inbox/in-progress #blog/publish
Created: [[2024-04-15]]