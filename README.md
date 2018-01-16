# Karel the Robot in OSORI
## INDEX

1. [What is Karel?](#what-is-karel)
2. [Karel OSORI Description](#karel-osori-description)
3. [Project tasks](#project-tasks)
4. [Reference](#reference)
5. [License](#license)



## What is Karel?

**Karel** is an [educational programming language](https://en.wikipedia.org/wiki/Educational_programming_language) for beginners, created by [Richard E. Pattis](https://en.wikipedia.org/wiki/Richard_E._Pattis) in his book *Karel The Robot: A Gentle Introduction to the Art of Programming*. Pattis used the language in his courses at Stanford University, California. The language is named after [Karel Čapek](https://en.wikipedia.org/wiki/Karel_%C4%8Capek), a [Czech](https://en.wikipedia.org/wiki/Czech_people) writer who introduced the word *robot*.

 A program in Karel is used to control a simple **robot** named Karel that lives in an environment consisting of a grid of streets (left-right) and avenues (up-down). Karel understands five basic instructions: `move` (Karel moves by one square in the direction he is facing), `turnLeft`(Karel turns 90 ° left), `putBeeper` (Karel puts a beeper on the square he is standing at), `pickBeeper` (Karel lifts a beeper off the square he is standing at), and `turnoff` (Karel switches himself off, the program ends). Karel can also perform boolean queries about his immediate environment, asking whether there is a beeper where he is standing, whether there are barriers next to him, and about the direction he is facing. A programmer can create additional instructions by defining them in terms of the five basic instructions, and by using conditional control flow statements `if` and `while` with environment queries, and by using the `iterate` construct.  [[출처]](https://en.wikipedia.org/wiki/Karel_(programming_language))



## Karel OSORI Description

 Karel the Robot in OSORI (referred to as "Karel OSORI") is based on Python3 environment. 

### World

 The **world** is made up of avenues and streets. These correspond to Cartesian X and Y coordinates respectively. Avenues are vertical lines, increasing to the East. Streets are horizontal lines increasing to the North. In the world file, coordinates are always described as avenues then street just as in geometry, where coordinates are described as x, y.

 Directions are defined as enumeration. [North, East, South, West]

 In Project, world file is saved as [`pickle`](https://docs.python.org/3/library/pickle.html) format which can serialize python object. The file contains number of streets, number of avenues, positions and directions of walls, beepers on world and its position, default position and direction of robot, number of beepers in robot's bag.

### Robot

 The **robot** has five primitive **actions**.

 move(), turnleft(), pickbeeper(), putbeeper(), turnoff()

 And robot can check some **conditions** about its status and surroundings.

front_is_clear(), front_is_blocked(),

left_is_clear(), left_is_blocked(),

right_is_clear(), right_is_blocked(),

back_is_clear(), back_is_blocked(),

next_to_a_beeper(), not_next_to_a_beeper(),

any_beepers_in_beeper_bag(), no_beepers_in_beeper_bag(),

facing_north(), not_facing_north(),

facing_south(), not_facing_south(),

facing_east(), not_facing_east(),

facing_west(), not_facing_west()

### errors

* Execution of move() when that move would cause Karel to hit a wall, or get outside the world range.
* Execution of pickbeeper() when there are no beepers on the field Karel is standing on.
* Execution of putbeeper() when Karel has no beepers in his bag.
* Missing of the last turnoff() statement at the end of the program body.



## Project tasks

TBD



## Usage

TBD




## Reference

[Karel the robot : a gentle introduction to the art of programming](https://www.amazon.com/Karel-Robot-Gentle-Introduction-Programming/dp/0471597252)

[Introducing Python : modern computing in simple packages](https://www.amazon.com/Introducing-Python-Modern-Computing-Packages/dp/1449359361)



## License

[MIT License](https://github.com/HyOsori/KareltheRobot/LICENSE)
