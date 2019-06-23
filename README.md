# Wikipedia Philosophy

A simple python script to reach the [Philosophy](https://en.wikipedia.org/wiki/Philosophy) article.

Thankfully this task was easy to come about, the main problem I ran into was grabbing the first paragraph to access the anchor tag within but luckily I found a snippet that does exactly that!

To run it simply type:

```
python3 index.py
```

You can also define an article to start out with:

```
python3 index.py https://en.wikipedia.org/wiki/Lateef_and_the_Chief
```

When the script reaches the afforementioned article its output is like so:

```
EUREKA! - You've reached Philosophy
```

Please note there is not a set limit for the amount of hops performed by the script; it'll run as many times as it needs to!
