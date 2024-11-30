---
date: 2024-02-10 00:00:00
title: Bottlenecks and Pull Requests
---

Let me start by saying my thinking is actually more of a belief. There is some pseudo science and anecdata baked in, but it's more based on gut checks than any cold hard facts. Bad news for you, changing someone’s belief is harder than changing someone’s thinking based on fact. Worse news for you: this is belief ive had about teams and git process for like 8 years lol.

I have two main goals with my process things. 1. engineering morale fueled by real felt delivery, progress, impact, unblocked-ness, etc. and 2. Consistency of team delivery (even over shipping a lot). funnily enough, consistency, in my experience on many teams, is one of the easiest ways to improve engineering morale.

It makes it easier to plan, easier to set goals, and then to hit them (all consistently).

Ok so how do you drive consistency for engineering? My preferred method is to follow most of the things in [[Things To Follow|here]]

Make an epic that represents some meaningful progress towards a change in the system. An epic should be able to be described to non engineers and they should understand that chunk of work’s value

A project team should be able to complete at least one epic a week, in terms of sizing of the epic. You could achieve this by making all epics roughly two weeks large, and offsetting them such that at least one epic gets done per week. This is hard to do, but not for the reason you might think. Its hard to do because it requires thinking about the Work To Be Done differently than if you were just going to write a bunch of tickets (or worse, get handed a bunch of tickets by PMs).

With the constraint of needing to think about how to Right Size epics, planning your projects, especially very long/big ones, becomes an exercise in and of itself. A few project teams on sage have done this to great effect over the past couple years.

Doing this well, or even kinda well, enables a project team to plan an entire quarters worth of work, and get pretty damn close to hitting every single deadline.

Being able to celebrate an epic (or two, or three) getting completed every week, to look at the plan and what we’ve finished already reduces the chances of big projects having that “no end in sight” problem that usually creeps in at the end. “the last 20% of a project takes 80% of the total time”

So we’ve got the epics. They're planned. We think they are roughly a week or two of work with maybe one or two or even three engineers working on each at a time.

Sidenote: My preference is always for epics that can be swarmed on rather than multiple epics in flight at a time. Two epics, the first completed in week 1 and the second completed in week 2, is 100% more preferable than both being worked on simultaneously, neither getting done in week one, and both getting completed sometime in week 2.

Now its time to think about how to do the work involved in completing a particular epic.

**The biggest bottleneck in the product development lifecycle is the pull request.** Giving a solid code review takes a lot of time. Usually the code reviewer needs to look at the same PR a couple times after various changes are made and comments are addressed. Time spent giving code review is time spent not working on new items, so the bottleneck has a doubly compounding effect on the rest of the system.

The part of the system with the highest throughput is the code writing portion. This means its quite easy for engineers to produce much more code that needs to be reviewed than there is time/resources to review the code and get it merged, resulting in a backup at the PR phase, making the bottleneck have an even even even larger affect on the throughput as now there is a backlog of things, causing engineers to spend much more time reviewing than normal.

Thinking about the entire product development lifecycle as a system, and applying the law that the maximum throughput of a system (a work item going all the way from the very beginning to the very end, ie in production) is capped by the throughput of the bottleneck. Said another way, the fastest we can actually ship can be measured simply by looking at how fast we can get PRs merged and shipped to prod.

Because your job is to put actual software into production, simply doing a lot of tickets and opening a lot of PRs gives you a false sense of progress and speed. You now need to wait for a lot of code review, you need to switch contexts for each ticket. The longer a PR stays open, the faster it rots, the harder it is to keep track of the state of it, the more time you're wasting not working on the next thing, and the worse your morale gets.

We do one ticket at a time until it is merged and in production. You arent going slower here, you are simply being realistic about the actual throughput of the system.

Again, the total throughput of the system is capped by PRs getting merged into main.

We all know many ways to get PRs reviewed faster. Add a great description, give it a review yourself before asking someone else to look at it to make sure they don't have to review it again after finding something silly, linters/tests, making the PR smaller.

Tools that handle complex dependent PRs like Graphite are great because they make big PRs smaller. I am completely unsurprised that the feedback from reviewers is positive. But it doesn't actually increase the throughput. It makes PRs easier to merge into other PRs, not `main`. When you’ve got a PR targeting another PR you’re stacking a bottleneck up behind another bottleneck. And thats not accounting for any potential rebasing shenanigans you’d need to account for along the long chain of related PRs as one or two or three of the PRs stays open for more days. You better pray you don't have consistent conflicts you need to address along the chain each time you rebase!

The goal here is engineering morale, and I am stoked that we found a very cool tool to break up PRs. And hey, sometimes a PR just has to be big, I hope more people on the team can use this tool to break up that once a year big PR.

But my challenge to you is this: plan the work in such a way that each ticket can independently get merged into `main`. Make the tickets right sized so that you can get a few merged a week. This means, when writing tickets, think about the size you estimate it to be. If you think a ticket will take longer than three days, turn it into two tickets at that point, not after youve done all the work and are trying to break it up into multiple PRs. Don't open more than one PR at a time because thats you stacking more work up behind the bottleneck in the system. Doing this consistently will feel great, will make it easier to predict when things are due, and will reduce the frustration/headache of managing multiple interrelated PRs.

**In summary, push the breaking up of the work into multiple PRs** _**before**_ **you do the work. Put that plan into separate tickets, and do one ticket at a time until it is merged to main.**