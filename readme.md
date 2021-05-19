# RBC Statements

> Great pains, small gains for those who ask the world to solve them; it cannot solve itself.  
>
> **Herman Melville**, *Moby Dick*

Ever wonder how much money you spent on Amazon? RBC Statements is an open-source Python repository that can help you figure that out. Download your credit card statements from the bank website, put them in the `files` directory, open a terminal window in the project directory RBC Statements is in and type:

```
python start.py
```

and wait for the CSV! Well, it's not quite so easy... you in fact will have to change the input and output directories in `RBC Statements\CCParse\parse.py` manually to the input and output folders you prefer, but I suppose this is a free tool after all.
