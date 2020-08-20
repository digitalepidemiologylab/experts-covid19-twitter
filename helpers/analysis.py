import numpy as np


def caliper_matching(groups, propensity, caliper=0.05, replace=False):
    """
    Implements greedy one-to-one matching on propensity scores.

    Inputs:
    groups = Array-like object of treatment assignments.  Must be 2 groups
    propensity = Array-like object containing propensity scores for each observation. Propensity and groups
                should be in the same order (matching indices)
    caliper = a numeric value, specifies maximum distance (difference in propensity scores or SD of logit propensity)
    replace = Logical for whether individuals from the larger group should be allowed to match multiple
            individuals in the smaller group. (default is False)

    Output:
    A series containing the individuals in the control group matched to the treatment group.
    Note that with caliper matching, not every treated individual may have a match.
    """

    # Check inputs
    if any(propensity <= 0) or any(propensity >= 1):
        raise ValueError('Propensity scores must be between 0 and 1')
    elif not (0 <= caliper < 1):
        if caliper > 1:
            raise ValueError('Caliper for "propensity" method must be between 0 and 1')
        elif caliper < 0:
            raise ValueError('Caliper cannot be negative')
    elif len(groups) != len(propensity):
        raise ValueError('groups and propensity scores must be same dimension')
    elif len(set(groups)) != 2:
        raise ValueError('wrong number of groups: expected 2')

    # Code groups as 0 and 1
    groups = groups == 1
    N = len(groups)
    N1 = groups[groups == 1].index;
    N2 = groups[groups == 0].index
    g1, g2 = propensity[groups == 1], propensity[groups == 0]
    # Check if treatment groups got flipped - the smaller should correspond to N1/g1
    if len(N1) > len(N2):
        N1, N2, g1, g2 = N2, N1, g2, g1

    # Randomly permute the smaller group to get order for matching
    morder = np.random.permutation(N1)
    matches = {}

    for m in morder:
        dist = abs(g1[m] - g2)
        if (dist.min() <= caliper) or not caliper:
            matches[m] = N2[dist.argmin()]  # Potential problem: check for ties
            if not replace:
                g2 = g2.drop(matches[m])
                N2 = N2.drop(matches[m])
    return (matches)
