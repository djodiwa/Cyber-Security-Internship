# Cyber Security Internship - Task 6 — Creating and Evaluating Strong Passwords (Personal Report)

## Purpose

I explored what makes a password strong by experimenting with different password types and testing them against a password-strength checker. My aim was to see how length, character variety and patterns affect strength scores and to draw practical conclusions for better password practice.

## Approach

I generated several example passwords that vary in length, use of uppercase/lowercase, inclusion of digits and symbols, and overall structure. I then tested each one with a password strength checker (using an algorithm matching the general rules used by popular checkers) and recorded the scores and the tool’s feedback. Alongside testing, I reviewed common attack methods — such as brute-force and dictionary attacks — to connect the scores to real-world risk.

## Example passwords and results

| Password                    | Score | Complexity (tool feedback)                                      |
| --------------------------- | ----: | --------------------------------------------------------------- |
| `1234`                      |    22 | Weak — numbers only, sequential                                 |
| `password`                  |    12 | Very weak — common word, all lowercase                          |
| `Password1`                 |    54 | Good — mixed case + digit but still short/patterned             |
| `Tr0ub4dor&3`               |   100 | Very strong — length, mixed types, low patterning               |
| `CorrectHorseBatteryStaple` |    85 | Very strong (long passphrase) but some repeat-letter deductions |
| `X7#kL9pQ2$mT4&`            |   100 | Very strong — random mix, meets all variety requirements        |

## Observations & insights

* **Length matters most.** Adding characters increases the search space exponentially, so longer passwords are far harder to crack by brute force.
* **Character diversity helps.** Mixing uppercase, lowercase, numbers and symbols dramatically increases the difficulty for both brute-force and dictionary-style attackers.
* **Patterns and repeats weaken even long passwords.** Consecutive characters, common words, repeated letters, or predictable substitutions lower the effective strength.
* **Passphrases are useful but not foolproof.** Long word-based passphrases score high due to length, but they can be vulnerable if they use common phrases or many repeated letters. Adding some non-dictionary elements or mixing case/symbols improves them.
* **Placement of digits and symbols matters.** Numbers/symbols placed in the middle of a password (not only at the end) tend to reduce predictable patterns and score better on many checkers.

## Practical recommendations (best practices)

* Prefer passwords of **at least 12–16 characters**; longer is better.
* Use a **mix of uppercase, lowercase, numbers, and symbols** to expand the character set.
* Avoid common words, obvious substitutions, and obvious patterns (e.g., `1234`, `password`, `qwerty`).
* Use **randomly generated passwords** for high-value accounts, and consider **passphrases** (well-chosen words with some randomness) for memorable, strong passwords.
* Use a **password manager** to generate and store unique passwords per site, and enable **multi-factor authentication (MFA)** wherever available.
* Change passwords promptly after a breach and avoid reusing passwords across sites.

## How this relates to attack methods

* **Brute-force attacks** are slowed enormously by length and diversity: every extra character multiplies the number of combinations an attacker must try.
* **Dictionary attacks** rely on lists of likely words/phrases and common variations. Avoiding dictionary words and using randomness or uncommon passphrases reduces the effectiveness of those attacks.

## Conclusion

From the tests and feedback, the most effective way to increase password security is to combine length and randomness while avoiding obvious patterns. The strongest examples in my tests combined character variety with sufficient length and minimal repeatable structure. For strong account protection, pair strong unique passwords with a password manager and MFA.
