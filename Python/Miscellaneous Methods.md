# Foreword
This is a collection of small problems solved either for fun or as school work

# 1
```python
def dirReduc(list):
    """
    @Method: dirReduc
    @Description:
        Accepts a list of cardinal directions and removes
        directions that cancel eachother out
    @Returns: A simplified list of directions
    """

    #A dictionary to hold each cardinal direction and the ammount of times
    #   it is in the list
    d = {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
    L = []

    #changes the key to the number of occurences
    d["NORTH"] = list.count("NORTH")
    d["SOUTH"] = list.count("SOUTH")
    d["EAST"] = list.count("EAST")
    d["WEST"] = list.count("WEST")

    #Simplifys North and South
    if d["NORTH"] > d["SOUTH"]:
        d["NORTH"] = d["NORTH"] - d["SOUTH"]
        del d["SOUTH"]
    elif d["NORTH"] == d["SOUTH"]:
        del d["NORTH"]
        del d["SOUTH"]
    else:
        d["SOUTH"] = d["SOUTH"] - d["NORTH"]
        del d["NORTH"]

    #Simplifys East and West
    if d["EAST"] > d["WEST"]:
        d["EAST"] = d["EAST"] - d["WEST"]
        del d["WEST"]
    elif d["EAST"] == d["WEST"]:
        del d["EAST"]
        del d["WEST"]
    else:
        d["WEST"] = d["WEST"] - d["EAST"]
        del d["EAST"]

    #Puts anything left in the dictionary into the new list
    for i in d:
        L.append(i)

    return L
```

# 2
```python
def dupLetters(s):
    """
    @Method: dupLetters
    @Description:
      Method accepts a string of letters
      This method is not case sensitive
    @Returns: the number of letters which are repeated
      NOT THE NUMBER OF TIMES THEY ARE REPEATED
    """

    s = s.lower()
    repeats = 0


    for i in s:
        if s.count(i) > 1:
            repeats += 1
            s = s.replace(i, "")

    return repeats
```

# 3
```python
def dupLetters(s):
    """
    @Method: dupLetters
    @Description:
      Method accepts a string of letters
      This method is not case sensitive
    @Returns: the number of letters which are repeated
      NOT THE NUMBER OF TIMES THEY ARE REPEATED
    """

    s = s.lower()
    repeats = 0


    for i in s:
        if s.count(i) > 1:
            repeats += 1
            s = s.replace(i, "")

    return repeats
```

# 4
```python
def consecutive(L):
    """
    @Method: consecutive
    @Description:
        Locates the first value in the array which is not consecutive
    @Returns: the first inconsecutive value or none if there isn't one
    """

    for i in range(len(L) - 1):
        #the check is not preformed for the first value
        if i != 0:
            if L[i] != L[i - 1] and L[i] != L[i-1] + 1:
                return L[i]

    return None
```
