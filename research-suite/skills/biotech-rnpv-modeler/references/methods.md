# Methodology

Formula: asset rNPV = sum over rows of cashflow_t × unconditional_probability_t / (1 + discount_rate)^t. Equity = asset rNPV + cash − debt − unallocated overhead PV. Price/share uses consistently scaled diluted shares.

Example: an immediate development outflow of 10 has p=1; a later outflow of 20 incurred only if the next stage is reached might use p=0.6; a commercial inflow conditional on approval might use cumulative p=0.3. Applying p=0.3 to all development costs would understate expected spending. A separate global approval multiplier would double-discount risk.

Conditional transition probabilities must be converted to unconditional probabilities before input. A scenario label is not a probability weight. The tool does not combine scenarios unless the user separately defines a justified distribution. Cross-asset correlation, option value, stochastic financing and patent litigation are not modeled automatically. No terminal value is silently added.
