# openbank-funnel 🏦📉

A Django library that gives any bank 1-click funnel analysis on digital banking chaanels, onboarding, KYC, loan applications. 

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
