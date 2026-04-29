# Data Normalisation Tips

Review the following prompts if you're struggling to normalise the example data set.

- Step 1: Reach `1NF`
  - Get rid of the commas in `ItemsOrdered`.
  - What combination of columns makes a row unique now?

- Step 2: Reach `2NF`
  - Look for Partial Dependencies.
  - Does the `CustomerName` depend on what item was bought, or just the `OrderID`?
  - Split the data into a table for Orders and a table for OrderItems.

- Step 3: Reach `3NF`
  - Eliminate Transitive Dependencies.
  - Look at the `Barista`, `BaristaCertification`, and `Station`.
  - Does the `BaristaCertification` depend on the `OrderID`, or does it depend on the `Barista`?
  - If Sam gets promoted to "Manager" how many rows do we have to update in the original table?
  - Create a separate `Baristas` table.