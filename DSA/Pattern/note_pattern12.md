This is one of the most important concepts in Python loops. Once you understand range(start, stop, step), you'll never have to memorize it again.

Let's break it down.

First, how does range() work?

Most beginners only know:

range(5)

which means

range(start=0, stop=5, step=1)

So Python generates

0 1 2 3 4

Notice:

Starts at 0
Stops before 5
Increases by 1
The full syntax is
range(start, stop, step)

where

start → where to begin
stop → stop before this number
step → how much to move each time
Example 1
for i in range(2, 8, 1):
    print(i)

Output

2
3
4
5
6
7

Python starts at 2 and keeps adding 1.

Example 2
for i in range(2, 8, 2):
    print(i)

Output

2
4
6

Because it jumps by 2.

Now let's reverse

Suppose

range(5, 0, -1)

Let's see what Python does.

Start at

5

Move by

-1

So

5
4
3
2
1

Will it print 0?

No.

Because range() stops before the stop value.

The stop value is

0

so Python stops before reaching it.

Output

5
4
3
2
1