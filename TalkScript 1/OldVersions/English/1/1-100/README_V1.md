
***

# TalkScript as a programming language

This directory is an archive of the attempts of making TalkScript its own separate programming language. It was originally going to be both a programming language and an IDE, but I decided it was best to make it an IDE, as it doesn't need to be its own language, due to the discovery and invention of the click escape code system.

[Click/tap here to see the modern, up-to-date project (TalkScript as an IDE)](/TalkScript/)

## Still there?

I will now list TalkScripts original programming language design.

Here is the original plan, a sample program with all the ideas, located at [/TalkScript 1/talkscript guide.ts1proj](/TalkScript%201/talkscript%20guide.ts1proj)

```text
// talkscript guide \\
|: talkscript is specially designed for: 
<*> people with poor vision 
<*> people with hurt or broken arms
<*> people without arms 
<*> people with mental issues 
<*> people with little knowledge of computer science 
<*> special needs students 
:|

|: how to program :|
// this is a single line comment \\
|:
this
is
a 
multi- 
line 
comment 
:|

// About \\
|: Talkscript is a programming language made for people who can't see or don't have working arms. Talkscript is voice based, and currently only works on Linux :|

// Some commands \\

linout ("Hello, world")

|: Output:

Hello, world

:|

|: 

the voice command for linout is:

voicescript! Type line output and open then type "Hello"
pause 1 second 
type a comma and type "world" 
pause 1 second
then close the line :|

// It seems complicated at the moment, but we are working on a way to make a simple programming language for the handicapped \\ 

|: 

the voice command for single line comments is:

|:

voicescript! make a single comment on current line 
pause 1 second 
type "Test comment"
pause 1 second 
close comment 

|:
|: output 

// Test comment \\

:|


|: the voice command for section comments is:

:|

|:

voicescript! make a comment section on current line 
pause 1 second 
go to next line and type "line 1"
pause 1 second 
go to next line and type "line 2"
pause 1 second 
go to next line and type "line 3"
pause 1 second 
end comment section 

:| 

// output \\

|:
line 1 
line 2 
line 3 
:|

// the easier way to do this is to make a voice macro. To make it simpler, define a macro and run it \\
// example: \\

|:

voicescript! create new comment macro 
pause 1 second
name macro "section1"
pause 1 second 
in macro, go to first line and type "line" 
pause 1 second 
add integer x 
pause 1 second 
set x to 0
pause 1 second 
in macro, go back to first line, go to end of line, and add symbol: plus 
pause 1 second 
add x after plus 
pause 1 second 
add symbol: plus 
pause 1 second 
go to next line and type repeat 
pause 1 second 
add integer t 
pause 1 second 
set t to 25 
pause 1 second 
go back to line 2, go to end of line and put integer "t" 
pause 1 second 
add times 
pause 1 second 
go to next line and type "run macro"
pause 1 second 
save and close 
pause 1 second 
select macro "section1"
pause 1 second
run selected macro 

:|
// that was A LOT! It will be worth it later on. Here is the output from the macro we just created \\
// output: \\

|:line1
line2
line3
line4
line5
line6
line7
line8
line9
line10
line11
line12
line13
line14
line15
line16
line17
line18
line19
line20
line21
line22
line23
line24
line25:| 

// Add whatever you want as your comment section macro, and it should work if in the correct syntax \\

// But what if you were to make an error? Well, here are some commands to help \\ 

|: undo command 
voicescript! undo 1 action 
:|
|: This command will undo the current action. You can also change the number to anything you want. If you were to type a number 
bigger than how many moves you make, it will give this output:|

// x undo actions ignored, nowhere to undo to \\

// What if you undid something by mistake? There is a very similar command, and it is probably very predicabe right now: \\

|: redo command 
voicescript! redo 1 action 
:|

|: This command will redo an undo. Just like the undo command, you can change the number to anything you want. If you were to type a number bigger 
than how many moves you make, it will give you this output :|

// x redo actions ignored, nothing to fix \\

|: Helpful tip:
You can use a negative number with the undo command to redo that set amount of numbers 
You can use a negative number with the redo command to undo that set amount of numbers 
Whichever is easier and more enjoyable to say, it is your choice!
:|

|: Now to move on to packages
You will need to import packages to be able to do many tasks.
The way this is done is different from other programming languages, so be careful!
:| 
|: Packages 
import spoke.pack.basicpunc 
// this command adds in basic punctuatio to the program with the following symbols:\\
. , " ? / \ | - _ + = ! @ # $ % & * ( ) ^ ` ~ ' : ; > < [ ] { }  
// now there is another step! You only IMPORTED it. You haven't activated it yet. To activate, use this voice command \\
voicescript! go to next line and activate spoke.pack.basicpunc 
// the full voice command is listed above for this package: \\
voicescript! go to line 1 and import spoke.pack.basicpunc
wait 1 second 
voicescript! go to line 2 and activate spoke.pack.basicpunc 

:|
// the output will be as follows \\
|:
import spoke.pack.basicpunc
activate spoke.pack.basicpunc 
:|

|: Note
You cannot ignore saying the periods. It will also not accept periods at the moment, you have to say "dot" instead
:|

// Copy, pasting, and cutting \\
|: To make sure you have the full functionality of the keyboard, you can also cut copy and paste 
before talkscript lets you cut copy or paste code, for safety reasons, it will create a snapshot first. This will let you undo actions if you overwrite, move, or paste something 
in a place that you don't want it 
There is a limit of 1463874688992 snapshots, which will last you a VERY long time, probably a lifetime or two, or many, depending on the user and the project 
:| 
// to copy, say as follows \\
|:
Voicescript! Go to line 1
pause 1 second 
go to column 1
pause 1 second
turn selection on 
pause 1 second 
go to column 28
pause 1 second 
copy
:|
// cutting is almost exactly the same, just say as follows \\
|:
Voicescript! Go to line 1
pause 1 second 
go to column 1
pause 1 second
turn selection on 
pause 1 second 
go to column 28
pause 1 second 
cut
:|
// pasting is a little different, but still easy, just say as follows \\
|:
Voicescript! go to line 7 
pause 1 second 
go to column 7
pause 1 second 
paste my selection 
:|

|:

|: current pros and cons
Pros
<*1> People with disabilities will be able to be more productive in computer science 
<*2> People who are blind can make software easier 
<*3> People who have no arms or no logs or both can use a computer with full functionality and be more productive in computer science 
<*4> programming will be easier 
<*5> the language is simplified
<*6> the language is capable of powerful things 
<*7> the language has 64 bit and 128 bit support 
Cons 
<*1> People with lisps may have a harder time 
<*2> The voice recognition isn't perfect yet, and may require assistance
<*3> different language support is not yet available 
<*4> different accent support is not yet available 
Good idea! 7/11 (not the convenience store, that is entirely different, and already WAS a good idea)
Bad idea! 4/11  
:|

|: Syntax errors
There will be heavy support for Syntax errors, as they are confusing to the majority of programmers. The language is already written in a simple way
so you can do both a grammar check, and a syntas check.
To do so, use these voice commands 
:| 
|: 

voicescript! Check the grammar of all lines 

:|

// or \\

|: 

voicescript! check the grammar of the current line 

:|

// to accept changes, the user must say either "yes that is correct" or "no that is incorrect" and it will go to the next available option \\

// for syntax errors, the same process, but with more debugging. The script is as follows \\

|:

voicescript! Check my syntax on all lines

:| 
 
// or \\

|:

voicescript! check my syntax on the current line

:| 

|: Current language support 
English - Limited support 
Spanish - NO SUPPORT 
French - NO SUPPORT 
Japanese - NO SUPPORT 
Italian - NO SUPPORT
Zulu - NO SUPPORT 
Chinese - NO SUPPORT 
Korean - NO SUPPORT 
German - NO SUPPORT 
Russian - NO SUPPORT 
Greek - NO SUPPORT
Norwegian - NO SUPPORT 
Other - NO SUPPORT

:|

|: Current accent support 
Northern American Accent - Limited support 
Southern American Accent - Limited support 
British accent - Limited support 
Russian accent - Poor support 
German accent - Poor support
Other - Unknown 

:|

// the end of a program follows the script at the bottom: \\

|: to end a program, say this:

voicescript! write the final line of the program 

|: 
// the output is as follows: \\

// end of program :|
```

***
