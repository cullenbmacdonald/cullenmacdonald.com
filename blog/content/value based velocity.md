---
date: 2024-03-15 00:00:00
title: Value Based Velocity
---

Ok so we want to measure our velocity in terms of value shipped, but how do you do that? Here is one such way. I encourage you to to take this and create a new sprint process for your team or (better yet) fit it into your current process.

Core concepts:

- **Value** - Measured in t-shirt sizes (S, M, L) and in relation to other possible things we could be working on. We don’t mean “value to the customer.” You don’t have to do any mental trickery and tell yourself “this internal user is the customer!!!” No, we think value in terms of Value to the Business. You believe some new feature is the missing item to get a big group of new customers in the door? Sure that's valuable. Improvements to some tool operations uses prevents them from making mistakes or wanting to quit and open a coffee shop upstate? Seems valuable to me. Some refactor lets us build future features faster and better? That's value. Can you can articulate some work that prevents engineers from sitting around for hours a week? That's very high value considering engineers are a fairly high cost center to the business; giving them hours back a week is huge! Thinking this way lets you compare and contrast all units of work on the equal footing, removing the problem of Tech Debt vs Feature Work.
- **Effort** - Ok right off the bat I gotta be honest. I hate [story points]([[Velocity and Story Points]]). I hate how much time teams spend arguing about whether a ticket is a 3 or a 5. I hate how much anxiety comes from making sure you have pulled enough story points into a sprint. I hate how story points is an estimation of complexity or effort about a ticket and then we use that to measure how productive we are being. Basically, I hate how much emotional energy is lost to the heat sink that is story points. That being said, effort is still important to think about. We use effort, also measured in T-shirt sizes relative to the other thinks we could be working on, as a way to make sure we’re working on the right stuff or spending the right amount of effort for the resulting value.

“Cullen what the heck,” you say, “You haven't talked about velocity at all yet.” If you have read [this]([[Velocity and Story Points]]) you’ll remember that I made an argument that velocity should be a measurement of impact, not of effort. Let’s take our vocabulary and generate some metrics.

Let's give Large value work units (I like using Epics here) a score 1.0, Medium a 0.5, and Small 0.25. When all work related to that unit of work has been deployed to production, the team gets the points. This week’s velocity is measured by summing all the points of the completed work units this week. It's as simple as that.

So now we’re tracking velocity in terms of value shipped, what does goal setting or reporting look like? You can (and should!) set goals around consistently shipping some amount of value weekly. Theres probably another post worth of my thoughts on consistency and why shipping one small thing a week is better than shipping one giant thing a month, but basically it feels really good to ship things, and it becomes much easier to estimate delivery dates when you have proof that you know how long a particularly sized epic takes to fully ship (because you've been consistently breaking things down into S/M/L and shipping at least one M effort epic a week, for example).

Quarterly goals I’ve had squads set using this framework:

- Large value or Large Value Equivalent (two mediums, four smalls, one large, etc) 12/14 weeks this quarter. (or 1.5 value, or 2! you can make up goal value and what number of weeks after you get the hang of it).
    - I like this goal a lot for a bunch of reasons:
        - it measures consistency
        - has a really nice side effect of getting teams of engineers to focus on one thing at a time until it is done, even delaying the start of some new work because other engineers swarm on this thing (one done thing is better than two in progress things)
        - engineers spend Monday morning figuring out tactically what and how they will ship a Large Value Equivalent.
- Some goal around the arbitrage. Set the same points scoring for Effort as you do for Value, and measure the ratio of value points to effort shipped. Once you start measuring your (grumble) effort velocity, you can then begin to be tactical around the quarterly planning and estimating projects which span more than one work unit.
- Setting a goal around some percentage of the value coming from a specific initiative. Testing, tech debt, a new product or feature etc.

A bullet list of things I didn’t know how to turn into paragraphs:

- What this looks like is, instead of trying to figure out how to fill up your sprint with enough effort (story points), your mission is to try and figure out how to fill your sprint with value that you could actually finish and ship.
    - This has a knock on effect of forcing the team to break down large projects into small shippable chunks.
- If an an initiative has 7 tickets that got done this week and 1 ticket that is not yet started, the team doesn't get the points. On Monday, when that final ticket gets merged and deployed, all the points for that contribute to that new week’s score.
    - this ensures the team focuses on FINISHING things and not just jumping to new projects. one completed project is better than two in progress ones.
- This process creates a feedback loop. Engineers seek out work they could be doing that outputs value over effort, and have to (get to?) articulate tech debt cleanup in terms of value to the business.
- ==“Cullen this is gamifying sprints.” Yeah, and it's really fun to play this game.== And teams who play it end up shipping way more value and doing way less work than teams who don’t. (also, story points are gamifying too, but in the wrong direction).

Curious about how you might iterate your way towards this without dramatically changing everything? Have the lead engineer and the PM from a team get in a room. The PM lists out all the problems (or fully fledged features that are probably already designed) that they want to get worked on. The PM then assigns a Value estimation to each one. Try to be normally distributed here. Not all things can be Large value, because remember, this is a relative value. Then have the lead engineer go through and do a rough effort estimation. This does not have to be normally distributed. Now sort by Value (largest to smallest) and Effort (smallest to largest). Now look at the order. How does that feel? I bet not great. I bet someone (both of you) aren't feeling great.

Have the PM do their ideal ranking, ignoring effort. Make adjustments to the value so that it's still Largest to Smallest by increasing value estimates on things that were moved up, and decreasing things that were moved down. Now the engineer gets to ask questions. Why is _this_ large value? The engineer might be able to offer some reasoning behind why certain things are higher effort than the PM expected. Maybe this can turn into a conversation about other (easier) ways to get the same value.

These are baby steps in the direction and allows various leaders on the team to start getting comfortable with this way of thinking about work.