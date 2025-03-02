# Postmortem

![Flogging a dead horse](post-mortem-meetings.jpg)

## Issue Summary

Shortly after deploying a new feature to our recently launched Ruby on Rails site, we encountered a significant issue. Five minutes post-deployment, users began reporting that they were unable to sign in or sign up to our platform. This was unexpected, as the feature had been thoroughly tested and worked flawlessly in our development environments. We received a total of 127 complaints via email, which was alarming given the importance of user retention for our newly launched platform. Determined to resolve the issue promptly, we cloned the repository from GitBug and attempted to set up the site locally. To our surprise, the site failed to start. The root cause was quickly identified: we had neglected to update the project requirements. The site was down from 9:55 AM GMT+1 to 11:20 AM GMT+1 today.

## Timeline

+ 03-03-2025 9:55 AM GMT+1 - Initial user complaint about inability to sign in.
+ 03-03-2025 10:20 AM GMT+1 - Winus, a backend developer, replicated the issue.
+ 03-03-2025 10:35 AM GMT+1 - Investigation of controllers and views for inconsistencies began.
+ 03-03-2025 10:40 AM GMT+1 - Initial assumption that the bcrypt gem was either faulty or misused, based on error messages indicating invalid hash issues.
+ 03-03-2025 10:42 AM GMT+1 - Checked if views were incorrectly binding form fields to model fields; this was not the case.
+ 03-03-2025 10:45 AM GMT+1 - Misled by the possibility that controllers were generating incorrect hashes for valid admin passwords.
+ 03-03-2025 10:50 AM GMT+1 - Winus hypothesized that the password was not being hashed correctly.
+ 03-03-2025 11:00 AM GMT+1 - The issue was escalated to the backend development team.
+ 03-03-2025 11:20 AM GMT+1 - The issue was resolved by updating the bcrypt gem version in the Gemfile.lock and reinstalling the gems.

## Root Cause And Resolution

The problem stemmed from using an outdated version of the bcrypt gem, which was incompatible with the hash generation method we employed. This incompatibility caused the gem to reject valid hashes stored in our database. Winus resolved the issue by updating the bcrypt gem to a newer version in the Gemfile.lock and reinstalling the necessary gems, which restored full functionality to the site.

## Corrective And Preventative Measures

+ Implement a continuous integration pipeline to automatically test builds on every pull request, ensuring that only passing builds are merged into the deployment branch.
+ Establish a monitoring system for both the database and application servers to detect and alert on issues in real-time.
+ Develop and enforce a comprehensive testing protocol for all new features, requiring that all tests pass before any feature is merged into the deployment branch.

---
