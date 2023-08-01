# lists in python

## What is a list?

A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.

In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas. Here’s a simple example of a list that contains a few kinds of bicycles:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

For example, let’s pull out the first bicycle in the list bicycles:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

This code returns the first item in the list, which is the string 'trek':

```python
trek
```
<span style="color: #ff0000;">Python lists are always starting from 0 not 1 so the first element index is always 0</span>

You can also use string methods on any element in this list. For example, you can format the element 'trek' more neatly by using the title() method:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
```

This code returns the first item in the list, which is the string 'Trek':

```python
Trek
```

now lets try to print the last element in the list

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

This code returns the last item in the list, which is the string 'specialized':

```python
specialized
```
<span style="color: #ff0000;">list[-1] means the last element of the list</span>

## Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list.

Let’s try pulling the first bicycle from the list, and composing a message using that value. Here’s the code:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
```

This code returns the following output:

```python
My first bicycle was a Trek.
```

## Changing, Adding, and Removing Elements

Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. Each time a new alien appears on the screen, you add it to the list. Your list of aliens will increase and decrease in length throughout the course of the game.

### Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

For example, let’s say we have a list of motorcycles, and the first item in the list is 'honda'. How would we change the value of this first item? The following example changes the name of the first motorcycle in the list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

This code returns the following output:

```python
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### Adding Elements to a List

You might want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you’ve built. Python provides several ways to add new data to existing lists.

#### Appending Elements to the End of a List

The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list. Using the same list we had in the previous example, we’ll add the new element 'ducati' to the end of the list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

This code returns the following output:

```python
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of append() statements. Using an empty list, let’s add the elements 'honda', 'yamaha', and 'suzuki' to the list:

```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```

This code returns the following output:

```python
['honda', 'yamaha', 'suzuki']
```
