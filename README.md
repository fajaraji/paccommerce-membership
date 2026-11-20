# PacCommerce – Membership Prediction & Benefits (Python)

A small, self-contained Python demo for **PacCommerce** that:
- **Predicts** a user’s membership tier (`Silver`, `Gold`, `Platinum`) from **Monthly Expense** and **Monthly Income** using **Euclidean distance**.
- **Auto-saves** new users into an in-memory “database” (a Python dict).
- **Displays** tier benefits & requirements in clean tables (via `tabulate`).
- **Calculates** final price after membership-based discounts.

This mirrors the spec in the slides:
- Tiers & benefits:
  - **Silver** — 8% discount, Food Voucher
  - **Gold** — 10% discount, Silver benefits + Online Ride Voucher
  - **Platinum** — 15% discount, Silver + Gold benefits + Holiday Voucher + Cashback up to 30%
- Tier “centroids” (reference points) used for classification:
  - **Silver** → Expense **5** (IDR million), Income **7** (IDR million)
  - **Gold**   → Expense **6**, Income **10**
  - **Platinum** → Expense **8**, Income **15**

---

## Explore the implementation

Run the examples to see how a new member is classified by Euclidean distance and how the tier changes a basket total.

- [Membership rules and worked examples](main.py)

## How it works

1. **Data Model**
   - `data`: dict of existing users → membership (e.g., `{"Sumbul": "Platinum", ...}`).
   - `benefit`: table data for the public tier comparison.
   - `requirement`: the reference expense/income per tier (used as centroids).

2. **Core Class: `Member`**
   - `predict_membership(expense, income)`  
     Builds a map `{tier: distance}` where  
     `distance = sqrt((expense - expense_ref)^2 + (income - income_ref)^2)`  
     Picks the tier with the **minimum** distance, **saves** it to `data[self.username]`, and returns the predicted tier.
   - `check_membership(username)`  
     Looks up the user in `data` and prints a single-row benefit table for their tier.
   - `show_benefit()` / `show_requirement()`  
     Print the full comparison tables.
   - `calculate_price(membership, price_list)`  
     Sums the items and applies the tier discount (Platinum 15%, Gold 10%, Silver 8%).

> Note: we keep `sqrt` for clarity; you could drop it (compare squared distances) with identical results.

---

## Run the examples

```bash
python -m pip install tabulate
python main.py
```

The script prints worked examples using its in-memory records. Edit the sample calls in `main.py` to try other inputs.
