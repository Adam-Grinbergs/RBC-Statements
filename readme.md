# RBC Statements

> Great pains, small gains for those who ask the world to solve them; it cannot solve itself.  
>
> **Herman Melville**, *Moby Dick*

Ever wonder how much money you spent on Amazon? RBC Statements is an open-source Python repository that can help you figure that out. Download your credit card statements from the bank website, put them in the `files` directory, open a terminal window in the project directory RBC Statements is in and type:

```
python start.py
```

and take a look at your output CSV in the project directory! Some future work on this repo will involve creating a report or formatting the CSV through pivot tables so you can determine what percentage went to food, eating out, alcohol, gas, Amazon, etc. without you having to filter the output CSV manually.

## Installation
1. Clone or download this repository
2. Go to the RBC website and download your credit card statements. They only keep them going back 7 years, so make sure you get them all!
3. Copy the credit card PDF statements into `~\CC\files` 
## Using the tool
1. Open your command line and navigate to the project root folder (`CC`)
2. Type `python start.py`
3. Look for `output.csv` in your root directory folder!
