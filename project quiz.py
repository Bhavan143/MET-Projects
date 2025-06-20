
questions=[
    {
    "question": "What is the capital of France?",
    "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    "answer": "C"  
    },
    {
    "question": "What is the capital of INDIA?",
    "options": ["A. Delhi", "B. Madrid", "C. Paris", "D. Rome"],
    "answer": "A"
    },
    {
    "question": "What is the capital of USA?",
    "options": ["A. Berlin", "B. Washington D.C", "C. Paris", "D. Rome"],
    "answer": "B"
    }
]
count=0
for i in questions:
    print(f"""
    Question:{i["question"]}
    Options:{i["options"]}
    """)
    your_answer=input("enter your answer:")
    if your_answer in i["answer"]:
        print("Correct!")
        count+=1
    else:
        print("Incorrect!")
print(f"your score is :{count}")