# openbank-funnel 🏦📉

A Django library that gives any bank 1-click funnel analysis on digital banking chaanels, onboarding, KYC, loan applications. 

**Reduce onboarding drop-off for digital banks in 3 lines of code**

Banks lose 30-40% of users during KYC and account opening.
`openbank-funnel` tells you exactly which step is killing conversion.

**1-line funnel analytics for Django banking apps**

Stop losing users in onboarding. Track where they drop off, run A/B tests, get alerts.

### The Problem
32% of users abandon digital banking onboarding. Banks don't know which step kills conversion.

### The Solution
```python
pip install openbank-funnel

from openbank_funnel import track_step, get_funnel

track_step(user, "kyc_upload") 
funnel = get_funnel(["signup", "kyc_upload", "kyc_verify", "account_open"])
funnel.dashboard() # shows drop-off %

# 1. Track users
tracker.track_step(user_id=123, step="kyc_upload")

# 2. See your funnel
funnel = Funnel(steps=["signup", "kyc_upload", "kyc_verify", "account_open"])
print(funnel.get_conversion())
# Output: {'signup': 100%, 'kyc_upload': 68%, 'kyc_verify': 55%, 'account_open': 52%}

# 3. Find the leak
print(funnel.biggest_dropoff())
# Output: "kyc_upload" - Fix this first