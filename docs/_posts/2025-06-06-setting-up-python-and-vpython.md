---
title: bb08-setting-up-development-environment
categories:
- engineering
- robotics
layout: post
---

bb-08 1.00 robotics posts

*Disclaimer. I am learning in real time.* 

Since this is the first post in this long series of more related posts, I'll briefly explain what all this is. In this series I'll attempt to build bb-8, the robot from star wars.

| ![BB-08]({{ '/assets/images/BB8.png' | relative_url }}) |
| :--: |
| Image of BB-08 - A robot from Star Wars |

Yep, super ambitious. I'll update the picture with a more 'realistic' model later but let's keep it detached from 'reality' for now.

We'll keep shifting between programming to physics to maths to 3d rendering to  kinematics to AI and to a  whole lot of other topics. By the time we get done, which will hopefully be after it has been built the robot, even if we don't do that successully, we'll have learnt quite a lot of stuff. That, for me, is exciting.. !!! 

In this first post,  I'll focus only on development environment setup. Installing python and some important libraries we shall need.

Alright, let's get straight into it. 

Open up a terminal window or the equivalent of that on your OS and type this  to confirm you have python installed.

```
python --version
```
That should output the python version you have if python is installed on your system. I am running python 3.13.3 as per the time I am writing this.
If that throws an error then python is probably not installed or not added to PATH. You can open up a gpt window to get that fixed. 
I also recommend that if you are using windows, you find out how to run a linux subsystem using wsl.  ChatGPT or your gpt of choice can ge a good hand holder for that. 

Now let's setup a virtual environment for this project. It's going to take quite some time until we are done, most probably years. But yeah. 

```
python -m venv ~/robotics
```
Then activate the environment by running.
```
source ~/robotics/bin/activate
```
Next install vpython via `pip install` command.
```
pip install vpython
```

After that's successully installed, test `vpython` . Create a simple script to display a sphere. In a new script named `test_vpython.py`, add the following code snippet.

```python
from vpython import *
sphere(pos=vector(0,0,0), radius=0.5, color=color.red)
```

Save the script and run it. If all went well, it should open up a browser window and output something like this;

| ![Red sphere with radius 0,5]({{ '/assets/images/redshere.png' | relative_url }}) |
| :--: |
| _Output from running vpython script_ |

Alright. If you ran into any errors for this initial setup, please use gpts and stack overflow to figure out what went wrong.  Otherwise, can't wait to see you in the next.
