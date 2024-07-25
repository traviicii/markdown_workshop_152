
# Markdown Workshop Lecture

---

## Basic Markdown Syntax

## 1. Headers

There are 6 sizes of headers denoted by 1-6 consecutive `#` symbols

**Example**:

> # header size 1
> ## header size 2
> ### header size 3
> #### header size 4
> ##### header size 5
> ###### header size 6

**Syntax**

```md
# header size 1
## header size 2
### header size 3
#### header size 4
##### header size 5
###### header size 6
```


## 2. Emphasis

We can make things **bold**

```md
**bold**
```

We can make things *italic*
```md
*italic*
```

We can also strike ~~through text~~
```md
~~through text~~
```

We can ~~***also do this***~~
```md
~~***also do this***~~
```

We can also make things ***bold and italic***
```md
***bold and italic***
```


## 3. Lists

### Ordered

1. first thing
    - this is important
    - another important thing
        - important about this other thing
            - another thing?!
1. second thing
1. third thing

### Unordered

- One thing
- another thing
- last thing


## 4. Links and Images

### Inserting Links
[Back to the Top](#basic-markdown-syntax)

[PokeAPI](https://pokeapi.co/ "Link to the PokeAPI website")

### Inserting Images

![An image of Ditto](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/132.svg)

![](132.svg)

---

## Advanced Features

### Tables

**Syntax**
```md
| Parameter | Type | Description |
|-----|----|----|
| `first_name` | `string` | Required |
| `email` | `string` | Required |
```

**Result**
| Parameter | Type | Description |
|-----|----|----|
| `first_name` | `string` | Required |
| `email` | `string` | Required |

### Code `Blocks`

```
simple code block
pip install this
```

```python
def solution():
    this = "that"
    for i in range(0, 20, 2):
        print(i)
    return this
```

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin <link>
```

### Block Quotes

> A block quote could be a side note, further info about a certain step, perhaps a definition for something.

### Definitions

What is an ORM?
: An ORM is an Object Relational Mapper that helps us relate a coding language like Python into SQL queries

**What is an ORM?**
> An ORM is an Object Relational Mapper that helps us relate a coding language like Python into SQL queries