---
layout: post
author: Luna Y
title: Welcome to the Moon
postName: 10 Games Challenge
tags:
    - Projects
    - Game Dev
---

Something that I've heard being talked about when it comes to learning game development is the
["20 Games Challenge"](https://20_games_challenge.gitlab.io/), where you create 20 games
(as the name implies) of increasing complexity, and by the end, the goal is to be at a point
where you hopefully know what you're doing, and can set out to make whatever project you wanted
but couldn't at the beginning.

For this blog, I'm going to attempt the first 10 games of the challenge that have prompts already
give, and save the last 10 for my other handle that I use for online communities.

I've actually already started on the challenge, and for the first game out of the 10 I'm planning to
showcase here, I made a singleplayer version of Pong, where the side you don't control is run by a
basic game AI. You can see an example of gameplay in the video below.

<video width="100%" controls muted loop>
<source src="/assets/video/pong.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

One of the caveats that the prompt mentioned about including an AI script was that the simplest possible
implementation of an AI would make the game impossible to win, so to balance that out, I made the AI paddle
slightly slower than the human player's, and added a short delay before it actually follows the ball,
to try and emulate a human's reaction time. The second part was probably the most difficult part of actually
coding this project, and even now I'm not entirely happy with how it works.

Other than that, there isn't really much to write about. It's Pong. If you want to take a look for yourself,
check out the [project repo](https://github.com/lyao6104/SinglePlayerPong).
