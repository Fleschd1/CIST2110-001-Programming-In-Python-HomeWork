import numpy as np
from scipy.stats import t

def pooled_t_test_and_confidence_interval(x1_bar, s1, n1, x2_bar, s2, n2, alpha, confidence_level):
    # Calculate the pooled standard deviation (sp)
    sp_squared = (((n1 - 1) * s1**2) + ((n2 - 1) * s2**2)) / (n1 + n2 - 2)
    sp = np.sqrt(sp_squared)
    
    # Calculate the standard error of the difference in means (se_diff)
    se_diff = sp * np.sqrt((1/n1) + (1/n2))
    
    # Calculate the t-statistic
    t_statistic = (x1_bar - x2_bar) / se_diff
    t_statistic_rounded = round(t_statistic, 4)
    
    # Degrees of freedom for the t-distribution
    df = n1 + n2 - 2
    
    # Calculate the two-tailed p-value
    p_value = 2 * t.sf(np.abs(t_statistic), df)
    p_value_rounded = round(p_value, 4)  # Round to four decimal places

    # Find the critical t-value for the confidence interval
    t_critical = t.ppf((1 + confidence_level) / 2, df)
    
    # Calculate the margin of error for the confidence interval
    margin_of_error = t_critical * se_diff
    
    # Calculate the confidence interval for the difference of means
    ci_lower = (x1_bar - x2_bar) - margin_of_error
    ci_upper = (x1_bar - x2_bar) + margin_of_error

    ci_lower = round(ci_lower, 3)
    ci_upper = round(ci_upper, 3)
    confidence_interval = (ci_lower, ci_upper)
    
    # Decide whether to reject the null hypothesis
    reject_null = p_value < alpha
    
    return {
        't_statistic': t_statistic_rounded,
        'p_value': p_value_rounded,
        'confidence_interval': confidence_interval,
        'reject_null_hypothesis': reject_null
    }

# Example usage with the given data:
results = pooled_t_test_and_confidence_interval(
    x1_bar=98.194, s1=25.83, n1=35,
    x2_bar=83.179, s2=23.55, n2=30,
    alpha=0.05,
    confidence_level=0.95
)

print("\n""\n""\n",results, "\n")