# Week 11 – Day 1: Advanced Django ORM

## Guided Lab – Catalogue Summary Report

This lab focuses on advanced Django ORM queries using relationships and aggregation.

### Topics Covered

- Relationship queries
- `values()`
- `annotate()`
- `aggregate()`
- `Count()`
- `Avg()`
- `Sum()`
- Filtering annotated results
- Ordering QuerySets

## Category Summary Report

The query:

- Filters active products only.
- Groups products by category ID and category name.
- Calculates:
  - Product count
  - Average price
  - Total stock
- Keeps categories with at least 3 active products.
- Orders results by product count descending, then category name.

## Overall Product Summary

The aggregate query calculates:

- Total number of active products
- Average price of active products

### Result Types

`category_report` returns multiple dictionaries because the query produces one result for each category.

`overall_summary` returns one dictionary containing the overall aggregate values.

## Exit Ticket

### Why must `values()` appear before `annotate()` in the category report?

`values()` defines the grouping fields first. Then `annotate()` calculates the aggregate values for each group.