# quizmia
Terminal based quizmaster, written in python

## Requirements 
`pip install tabulate`

## Usage
```shell
python3 quizmia.py
QuizMIA - Your terminal quizmaster
Loading questions..

What is the purpose of the 'safe mode' in windows?
┌─────────┬──────────────────────────────────────────────────────────┐
│   Index │ Answer                                                   │
├─────────┼──────────────────────────────────────────────────────────┤
│       0 │ To boot the operating system normally                    │
├─────────┼──────────────────────────────────────────────────────────┤
│       1 │ To install new applications                              │
├─────────┼──────────────────────────────────────────────────────────┤
│       2 │ To troubleshoot issues with minimal drivers and services │
├─────────┼──────────────────────────────────────────────────────────┤
│       3 │ To run a complete system backup                          │
└─────────┴──────────────────────────────────────────────────────────┘
[c]: Change question set
[p]: Pass
[q]: Quit
Answer (enter index): 2
[+] Correct!


What does RAID stand for?
┌─────────┬────────────────────────────────────────┐
│   Index │ Answer                                 │
├─────────┼────────────────────────────────────────┤
│       0 │ Redundant Array of Inexpensive Disks   │
├─────────┼────────────────────────────────────────┤
│       1 │ Random Access Internet Drive           │
├─────────┼────────────────────────────────────────┤
│       2 │ Redundant Application Interface Driver │
├─────────┼────────────────────────────────────────┤
│       3 │ Random Array of Independent Devices    │
└─────────┴────────────────────────────────────────┘
[c]: Change question set
[p]: Pass
[q]: Quit
Answer (enter index): q

=== RESULTS ===
[1/1] Correct answers (100%)
```

## Quiz data format
Custom quizes can be generated by creating a JSON file with the following format:

```json
[
    {
      "question": "ENTER QUESTION HERE",
      "options": ["ANSWER_1", "ANSWER_2", "ANSWER_3", "ANSWER_4"],
      "answer": ["ANSWER_1"]
    },
]
```
Then simply place the quiz file in the `data` dir and then add its path to `SETS` dict with a display name as the key and the path as the value.

```python
SETS = { "My Custom Quiz" : "./data/my_quiz.json" }
```

You can also set the initial quiz loaded by changing the value of:

```python
INITIAL_SET = "./data/my_quiz.json"
```
