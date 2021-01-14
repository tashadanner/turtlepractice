{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!\n",
      "1. Star\n",
      "2. Square\n",
      "3. Hexagon\n",
      "Select a number: 3\n",
      "Excellent choice! Go to the result tab to see your creation.\n"
     ]
    }
   ],
   "source": [
    "import turtle as turtle\n",
    "import random\n",
    "\n",
    "print(\"Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!\")\n",
    "\n",
    "turtle.penup()\n",
    "turtle.left(90)\n",
    "turtle.forward(250)\n",
    "turtle.left(90)\n",
    "turtle.forward(300)\n",
    "turtle.pendown()\n",
    "\n",
    "turtle.write(\"Drawing App!\", font=(\"Arial\", 16, \"normal\"))\n",
    "\n",
    "turtle.penup()\n",
    "turtle.left(90)\n",
    "turtle.forward(50)\n",
    "turtle.pendown()\n",
    "\n",
    "turtle.write(\"To draw a shape, go to the Console tab and choose an option!\", font=(\"Arial\", 16, \"normal\"))\n",
    "\n",
    "turtle.penup()\n",
    "turtle.forward(150)\n",
    "turtle.left(90)\n",
    "turtle.forward(150)\n",
    "turtle.pendown()\n",
    "\n",
    "def star():\n",
    "  turtle.pencolor(\"purple\")\n",
    "  for i in range(5):\n",
    "    turtle.forward(110)\n",
    "    turtle.left(216)\n",
    "\n",
    "def square():\n",
    "  turtle.pencolor(\"blue\")\n",
    "  for i in range (4):\n",
    "    turtle.forward(100)\n",
    "    turtle.right(90)\n",
    "\n",
    "def hexagon():\n",
    "  turtle.pencolor(\"green\")\n",
    "  for i in range(6):\n",
    "    turtle.forward(100)\n",
    "    turtle.right(60)\n",
    "\n",
    "selection = input(\"1. Star\\n2. Square\\n3. Hexagon\\nSelect a number: \")\n",
    "if selection == \"1\":\n",
    "  print(\"Excellent choice! Go to the result tab to see your creation.\")\n",
    "  star()\n",
    "elif selection == \"2\":\n",
    "  print(\"Excellent choice! Go to the result tab to see your creation.\")\n",
    "  square()\n",
    "elif selection == \"3\":\n",
    "  print(\"Excellent choice! Go to the result tab to see your creation.\")\n",
    "  hexagon()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
