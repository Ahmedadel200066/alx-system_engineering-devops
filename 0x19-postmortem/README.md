# Calculator App Postmortem

## Table of Contents
- [Issue Summary](#issue-summary)
- [Timeline](#timeline)
- [Root Cause and Resolution](#root-cause-and-resolution)
- [Corrective and Preventative Measures](#corrective-and-preventative-measures)
- [Conclusion](#conclusion)
- [Contact](#contact)

## Issue Summary

- **Duration:** The issue persisted from 08:00 UTC to 14:00 UTC on August 16, 2024.
- **Impact:** The calculator app produced incorrect results for arithmetic operations involving decimal numbers. This affected approximately 40% of users who relied on the app for financial and academic calculations.
- **Root Cause:** A bug introduced during a recent update, specifically in the floating-point arithmetic handling, led to rounding errors in calculations involving decimals.

## Timeline

- **08:00 UTC:** A customer complaint was received about incorrect calculation results with decimal numbers.
- **08:10 UTC:** The support team replicated the issue and confirmed that it affected all arithmetic operations involving decimals.
- **08:20 UTC:** The issue was escalated to the engineering team.
- **08:30 UTC:** The engineering team initiated a code review focusing on recent changes to arithmetic operations.
- **09:00 UTC:** Misleading investigation paths, such as UI-related issues, were explored and ruled out.
- **10:00 UTC:** The root cause was identified as a rounding error due to an optimization in the floating-point arithmetic code.
- **11:00 UTC:** A patch was developed to revert the optimization and correct the rounding error.
- **12:30 UTC:** The patch was tested, validated, and deployed to production.
- **14:00 UTC:** The issue was resolved, and users were notified of the fix.

## Root Cause and Resolution

The problem originated from a recent update aimed at optimizing the app's performance during floating-point arithmetic operations. The optimization inadvertently introduced a rounding error, leading to inaccurate results in calculations involving decimals. This affected users performing both simple and complex arithmetic operations.

To resolve the issue, the engineering team reverted the changes made during the optimization process. The original, stable method for handling floating-point arithmetic was reinstated. Extensive testing was conducted to ensure that the fix restored accuracy in all calculations before deploying the patch to production.

## Corrective and Preventative Measures

### Improvements:
- Enhance testing protocols to cover edge cases involving decimal numbers and floating-point arithmetic.
- Implement comprehensive unit tests for a wide range of arithmetic scenarios.
- Strengthen the code review process with a focus on changes related to core arithmetic functions.

### TODO:
- Develop and implement additional automated tests specifically for floating-point operations and rounding.
- Introduce monitoring tools to detect anomalies in calculation results and trigger alerts when they occur.
- Conduct a post-deployment audit of all arithmetic-related code changes to identify potential risks.
- Provide training sessions for the engineering team on handling floating-point arithmetic to prevent similar issues in the future.

## Conclusion

This postmortem highlights the importance of rigorous testing and careful consideration of changes to fundamental components like arithmetic operations. By implementing the corrective and preventative measures outlined above, we aim to enhance the reliability of the calculator app and prevent future issues.

## Contact

For further questions or concerns regarding this postmortem, please contact the project lead at [Click here](mailto:medo.adel200@gmail.com).
