# Lab 5 — Reflection on Static Code Analysis

## 1. What is the purpose of static code analysis?

Static code analysis examines source code without executing it to identify potential defects, security vulnerabilities and coding-style violations. It helps developers identify problems early, before they cause issues during program execution.

## 2. What did Pylint, Bandit and Flake8 help identify?

Pylint helped identify code-quality problems, such as the mutable default argument, naming conventions, missing docstrings and unnecessary expressions. Bandit identified security risks involving SSL certificate verification, request timeouts, shell execution and TLS configuration. Flake8 identified formatting issues, unused imports and excessively long lines.

## 3. Which issues were most important to fix?

The security issues were important because disabled certificate verification and unsafe shell execution can introduce security risks. The mutable default argument and attendance-calculation issues also needed attention because they could cause unintended behaviour or incorrect results. I addressed these defects and then corrected the remaining formatting issues.

## 4. How did I verify the fixes?

I compiled and executed the updated program and reran Pylint, Bandit and Flake8. I saved separate reports before and after the changes so the findings could be compared. I also documented the identified issues and their fixes in a table.

## 5. What are the limitations of static analysis?

Static analysis cannot guarantee that a program is completely correct or secure. Some errors depend on runtime data, and tools may miss defects that require human judgement to identify. Static analysis should therefore be used together with execution testing and code review.