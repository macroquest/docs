# MQ2MoveUtils:v11 FAQ

\_\_NOTOC\_\_

## Common Issues

### Every few seconds your character jerks his heading to one side and then resets \("jitters"\)

This is caused by stucklogic settings being set incorrectly to the speed of your CPU. You can confirm this is the problem by temporarily disabling stucklogic with _/stick set stucklogic off_. If the stuttering ends, you will need to tweak your stucklogic settings \(see the main article\).

### Your character runs into walls or off into illogical directions

* If you are using WinEQ, you should disable true movement. \(_/stick set wineq on_\)
* If you are not using WinEQ, you may have stucklogic disabled or your stucklogic settings need to be configured

  properly.

### Your character spins in circles while jumping up and down

* You are likely using wineq2 while trying to use true movement. set wineq support on
* Otherwise, your framerate is really, really bad and you need to adjust your stucklogic settings by a very large

  amount

* OR, see the AdvPath comment below

### Common Issues with MQ2AdvPath and ModBot ala Master Kroak

* it was "stuck" i.e. turning and jumping.

```text
That's the plugin trying to get to the point your leader was at when the follow command was actually started..
It doesn't work like this plugin, ie - you get stuck behind a wall, leader moves back and you unstick..
It won't do that if it's last recorded follow point is past the wall... You have to turn off following to get a new follow path.
```

* After issuing the /bc follow, with an ini setting of /stick 20 hold uw, the bots will follow, but every 2-3 secs,

  they "adjust"

trying to move forward a bit or something, even though their distance is less than 20, and the master isn't even moving.

```text
This happens if you have DoSit on and using AdvPath plugin to follow. Your stick setting is not used, and MQ2AdvPath has no setting to change it's follow distance.
Not sure why MQ2Advpath is coded this way, but it will force your toon to stand if your distance is over 10 from your leader...
The modbot macro is just trying to force your position so it's possible to sit without standing back up every second or so..
I'll increase the delay that's used there, and see if I can make one smooth movement..

P.S. If you WANT to use this plugin and not MQ2AdvPath for following, either unload MQ2AdvPath, or change this line at the top of modbot.mac to FALSE. 
/declare AdvPlug bool outer TRUE
```

### Your character looks straight up or down when underwater

This happens from having the _autouw_ feature enabled and sticking from a great distance.

### StuckLogic sucks underwater

Yes, this is true. Do not attempt to stick from large distances while underwater unless you have a clear path. Water swimming motion is not easily measured like walk/run on dry land.

### You cannot manually break from a stick

* You use MQ2Melee

  You will need to enable breakonkb in MoveUtils and also set stickbreak=1 in MQ2Melee

* You do not use MQ2Melee

  You will need to enable breakonkb in MoveUtils.

### You use MQ2Melee and any time you issue a /stick with hotkey or macro, it gets changed

This happens from not having 'stickcmd' set to anything in MQ2Melee while still having MQ2Melee set to use a stickrange

* it will use its own default parameters.

### You setup a camp but have problems returning to it

The most common cause of this is having a target. By default, automatic camp returns require nothing on target.

Verify what camp settings you have enabled. Certain features behave different ways, for example

```text
ReturnNoAggro will only return to the camp if you do not have aggro.
ReturnHaveTarget will allow you to return even if you have a target.
ReturnNotLooting will not return if you have an open corpse being looted.
```

### _/stick front_ does not work

You do not have HoTT data available. You either need the HoTT group leader AA or you need to enable nohottfront \(_/stick set nohottfront on_\)

### Your _/face_ commands are not working

You cannot use [_/face_](../../../commands/slash-commands/face.md) while a MoveUtils command is active. MoveUtils handles facing targets internally based on many different settings. Using _/face_ in your macros that rely on MoveUtils is a bad practice that causes nothing but problems and thus is no longer allowed by the plugin.

### NONE of your commands are working but you are sure the plugin is loaded and was working for a bit

Try \( _/stick imsafe_ \) if you have BreakOnSummon or BreakOnGM enabled Try \( _/stick unpause_ \) if you have PauseLock enabled

### I'm retarded and still use VC6. How do I compile this beast?

* Get a real compiler
* OR uncomment //\#define OLD\_COMPILER\_USER

## Configuration

### What are the different ways to handle manual keyboard and mouse movement ?

* Breaking \(_/stick set \[breakonkb \| breakonmouse\] on_\)
  * BreakOnKB - if you touch any keyboard movement related key \(forward, backward, left, right, strafeleft,

    straferight, autorun\) the current command will end

  * BreakOnMouse - if you use mouselook \(default is hold right-click\), the current command will end
* Pausing \(_/stick set \[mpause \| mousepause\] on_\)
  * mpause - if you touch any keyboard movement key, the current command will pause to let you move and then resume

    after a configurable delay

  * mousepause - if you use mouselook, the current command will resume after a configurable delay

You may only have a Break or a Pause on for a single option, but not both. However, you may have a pause for one option and a break for a different option on. That is: Keyboard can either be breakonkb or mpause, and mouse can either be breakonmouse or mousepause, but you may not have breakonkb AND mpause Thus, you may have breakonkb and mousepause or mpause and breakonmouse.

Results:

```text
MoveUtils:
mpause on - pressing a movement key pauses stick for a defined amount of time
(resume timer starts when all movement keys have been let go)
breakonkb on - pressing a movement key breaks stick entirely
both off - stick will not break from movement key input (i.e. it will fight you to stay locked onto target)

MoveUtils with MQ2Melee
mpause on - pressing a movement key pauses stick for a defined amount of time (resume timer starts when all movement keys have been let go)
breakonkb on - pressing a movement key breaks stick entirely. MQ2Melee then turns it back on instantly if MQ2Melee's attack is on
and you are within MQ2Melee's stickrange of the target.
both off - stick will not break from movement key input, MQ2Melee's attack key will toggle stick state
```

### How do I make the plugin output less or more ChatWnd messages

See the Verbosity section at the bottom of the main article.

## Movement & Heading

### What is the difference between fast, loose, and true heading?

The three types of heading changes are a question of legitimacy versus efficiency.

**Fast** heading instantly changes your heading to the desired location. If you are facing North, target a mob that is South of you, and issued a stick command with fast heading enabled, your character would instantly face the mob and begin running. This works like MQ2's [/face](../../../commands/slash-commands/face.md) command with the _fast_ parameter. Repeated _fast_ turns can be quite noticeable to other players and thus, the other options exist.

**Loose** heading rotates your heading changes using a fixed size turn increment to look more legitimate. You are able to set this increment size between 1 and 100. These numbers represent the actual number of degrees you will turn per pulse, not any sort of scaling system.

**True** heading rotates your heading changes using the same method EQ does if you were to hold down the _right_ or _left_ key. This is comparable to [/keypress](../../../commands/slash-commands/keypress.md) with _right hold_ as parameters. This is the most legitimate method of turning available. It is also the slowest.

### Why do I move backwards often? It looks crazy and unnatural.

Either your _backupdist' is set way too high \(10.0 is reasonable, 50.0 is not\) or you should just disable_useback''

### When using loose or true heading, my character orbits around the destination/target rather than arriving smoothly

This happens due to bad frame rate and you should tighten up the AllowMove setting. Default is 32.0, you can lower it down to 16.0 or even 8.0

### When I dismount, my characters appear to be spinning in circles

This is an EQ bug and has nothing to do with MQ2 nor MoveUtils

== StuckLogic ==

### What is stucklogic?

When a character runs into an object, it will continue running forward because there is no awareness that the object exists. People with stucklogic disabled can often be seen running into walls or rocks or failing to navigate through twists and turns of tight areas \(smart ones use AdvPath\).

Stucklogic is an effort to overcome this problem by measuring an average distance moved per pulse based on Y X location. When the average distance declines dramatically, the plugin is able to be aware that forward motion is no longer happening and attempts to correct this.

### Explain what stucklogic values do

TryToJump - will jump every few pulses to attempt scaling over small rocks and stumps \(very helpful to **food races** such as gnomes that frequently get stuck\) TurnHalf - if stucklogic has turned half way around \(256 deg\) without making any progress, it will reset heading to the starting point and try turning the other direction

```text
/stick set pulsecheck #
-pulsecheck defaults to 4
-this value is sort of what "stuckcheck" was before.
-it serves as the size of your pulse history to be used to calculate your average movement distance.
the largest you can set this value to is 32 (defined by MAXRINGSIZE).
The higher you set this number, the less often stucklogic would misfire (so if you are getting the
"jittery" problem you will want to increase this value). This also means it will take longer to know
that it is stuck, so if you are getting stuck and not responding fast enough, you would do the opposite and lower this value.

/stick set pulseunstuck #
-pulseunstuck defaults to 5
-this value is new
-this is the amount of pulses you have successfully moved forward before hard-forcing stucklogic to be considered unstuck.
this serves the purpose in that if you were stuck for 20 pulses, your stuck counter would normally try to move forward
for 20 more pulses before considering itself free. there was some handling for this that had some issues so now you can set a value
such as this one to force a faster "im unstuck" process.
-the higher your framerate, the higher you want this value. 5 may not be enough on better computers and you may end up
getting restuck again, it will look like what we are calling "snaking". If you notice yourself "snaking" then this would be the first value to try increasing.

/stick set diststuck #.##
-diststuck defaults to 0.5
-this is similar to before in that it is the amount of distance you need to have moved versus your average pulse rate in order to not be stuck
-this value should properly scale for all speeds of computers. you may want to set it higher or lower, play with it and
find what works best (and please let us know!!), but keep in mind setting this value to something tiny such as 0.001 as
we did in the old logic should no longer be necessary. deadchicken has determined that mindset was only working because
of some incorrect math in the formulas. try to stick with more logical values and then reporting back your results would be appreciated.
```

### I am in a boxed room with only a single doorway and stucklogic wont get me out

It can eventually with turnhalf off, but it will take hours. Use MQ2AdvPath or a combination of /moveto loc Y X to get out of rooms like this. Stucklogic is helpful but it doesn't create miracles.

## Stick

### When I gain aggro, my character spins in circles

You do not have access to the HoTT group leader AA while using /stick behind/!front/pin You can correct this by enabling DelayStrafe with a minimum value of at least 1500 before strafing

### When I lose aggro, my character spins in circles

You do not have access to the HoTT group leader AA while using /stick front You can correct this by enabling DelayStrafe with a minimum value of at least 15000 before strafing You can also _/stick set nohottfront off_ and stick front will be disabled if you do not have HoTT data

### When using MQ2Melee, I have to clear my target to stop sticking because turning off attack does not work

You need to create a MQ2Melee attack hotkey and NOT USE the eq attack on/off key. They are not the same thing.

### My character stays at a fixed range when sticking even though I try to move closer manually

This is due to _moveback_ repositioning. Take that parameter out of your stick command.

### What is a snaproll?

Basically if you issue /stick snaproll it will plot the movement location as an X behind the mob. No matter where you are relative to the mob, it will turn to face directly at the X and then run there in a straight line.

If you issue /stick snaproll face the X is plotted in front of the mob. /stick snaproll left and it will go to your left aka the mob's right shoulder, and /stick snaproll right and it will go to the mob's left shoulder.

This is mainly for hidden rogues to use their opening strike disc without strafing into position to maximize DPS.

## MakeCamp

### What is camp scattering and how do you use it?

This is a bit complex but when configured properly it is amazing. The idea behind this is that instead of returning to a random location within your camp radius, you can define a specific bearing, distance, and scatter radius from the center of your camp. This way you could configure your characters to return to specified areas all the time. The INI supports values on a character by character basis as well, so you could configure your tank to return to the center, your casters to return behind the tank, and your melee to return to the sides of the tank.

## MoveTo

### I am rotating in place when i use /moveto y x z

You supplied an unreachable Z axis destination. Either use /moveto y x, or supply an accurate z destination that can be reached

### Moveto never arrives at a destination, even ignoring z parameter

Your arrival distance is set too low. 5.0 is the absolute minimum but 10.0 is recommended.

## Circle

### What is this command for?

Bard circle kiting.

## Calc Angle

### What does any of this mean?

Angular Dist - what moveutils uses to determine pin/behind/front/!front, useful for configuring your !frontarc and behindarc settings. Adjust - this is how much adjustment is required in order to be facing your current target. This value relates to the new allowmove setting. Dist - the distance to your target provided by GetDistance \(what stick and some moveto, campreturns use\), useful in configuring your ArrivalDist values Dist3D - the distance to your target provided by GetDistance3D \(what snaproll, stucklogic and some moveto parameters use\), useful in configuring your ArrivalDist values

## MQ2Melee

### What changes did you make that are not found in the normal melee wiki

```text
stickrange=75
sticknorange=1
stickdelay=whatever
stickmode=1
stickcmd=8 !front
strikemode=1
strikecmd=snaproll 

this way you can use normal paramaters for stickmode/stickcmd and then setup a custom strikecmd and
use strikemode=1. strikemode=1 only relates to using a custom strike stick parameter and does not integrate
with whatever other methods turn strike on and off.

sticknorange=0 (default behavior you are used to)
sticknorange=1 (no range checking takes place for stick to happen automatically via mq2melee) 

update on sticknorange: MQ2Melee does not allow for attacking anything greater than 250 range away
regardless of any settings, and sticknorange does not overcome that (though maybe it should be possible?).
So sticknorange is effectively "stick at 250 or less", without checking the stickrange value
(which defaults to 75 if you do not set it). 


stickbreak=1  - allows breakonkb to work with new mq2melee changes
```

