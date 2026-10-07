# Lab 4 – Vibe Coding

## High-Low Card Predictor

**Name:** Chaithanya N   
**SRN:** PES1UG24CS124  
**Assignment:** Lab 4 – Vibe Coding    
**Vibe Coding Tool:** ChatGPT

## 1. Objective
Fix the existing bugs in the High-Low Card Predictor and implement the features specified in the repository README using Vibe Coding.

## 2. Repository Links

**Assigned Repository:**  
https://github.com/SETAPESU26/55_card_predictor

**Individual Repository:**  
https://github.com/chaithanya2810/55_card_predictor

## 3. Tasks Completed

### Task 1 – Card Rank Comparison
Fixed the rank comparison bug by using `numeric_rank` instead of string comparison.

Card order: 2 < 3 < ... < 10 < J < Q < K < A  

Commit: 28de9cd

### Task 2 – Win Streak Multipliers 
Added consecutive win streak tracking and increasing score multipliers. Wrong guesses reset the streak and multiplier.
Commit: 3d09bfd

### Task 3 – Tie / PUSH
Added tie handling for equal-rank cards. A tie displays PUSH, keeps the score unchanged, and preserves the streak.
Commit: 454e103

### Task 4 – Side-by-Side Card Reveal
Added a brief reveal showing the previous and newly drawn cards side-by-side before the new card becomes active.
Commit: a32871c

## 4. Testing

The game was tested before and after the changes.

Task 1: Numerical card comparison tested.  

Task 2: Streak, multiplier, and reset behavior tested.  

Task 3: Equal-rank PUSH behavior tested.  

Task 4: Side-by-side reveal tested.  


## 5. Evidence

**BEFORE VIDEO**  

This video shows the original High-Low Card Predictor application before making any changes.   
https://drive.google.com/file/d/1hk89N13aUNrVI1nAjNT0PR8Xrdip7OL6/view?usp=drivesdk  
  
**AFTER VIDEO**  

This video shows the application after fixing the bug and implementing all required features.  
https://drive.google.com/file/d/1xlNWQt7jShY9S2aW8alI44_N13H711S8/view?usp=drivesdk  


**Chat History:** https://chatgpt.com/share/6ac63151-3368-83ee-aeac-7751ecd27ddb 

**Details/Evidence PDF:**  
The comprehensive project report and evidence can be found in the accompanying PDF:  

[Details PDF](Lab4/Lab4_VibeCoding_Evidence.pdf)

## 6. Final Commit History
a32871c Add side-by-side card reveal   
454e103 Add tie evaluation rules  
3d09bfd Add consecutive win streak multipliers  
28de9cd Fix card rank comparision from str to numeric  
70644f6 Update game_engine.py

## 7. Submission Contents
```text
Lab-4/
├── README.md
└── Lab4_VibeCoding_Evidence.pdf
```
All four tasks were implemented, tested, committed separately, and pushed to the individual repository.
