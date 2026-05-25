# Q1. Ask user for movies released in year 2025 and store as set. Ask user again for movies watched (any year) and perform following
# Find movies released in 2025 that user has watched
# Find movies released in 2025 that user has not watched
# Find movies watched by user that were not released in 2025
# Q2. Daaraz found that their top electronic gadget buyer's are ram, shyam, sita, hari. Cosmetic buyers are hari, sita, gita, rita. Top grocery buyer's are ram, hari, gita and rabi. Find:
# Customers are top buyers of all electronics, cosmetics and groceries
# Customers who are top buyer of single category only
# Customers who are top buyers of exactly two categories
# All unique customers who are top buyers of at least one category
# Customers who are top buyers of electronics but not cosmetics

# Q1. Ask user for movies released in year 2025 and store as set. Ask user again for movies watched (any year) and perform following
# Find movies released in 2025 that user has watched
# Find movies released in 2025 that user has not watched
# Find movies watched by user that were not released in 2025

movies_2025 = set(input("Enter movies released in 2025 (comma-separated): ").split(","))
movies_watched = set(
    input("Enter movies watched in 2025 (comma-separated): ").split(",")
)

# Find movies released in 2025 that user has watched
watched_2025 = movies_2025.intersection(movies_watched)
print("Movies released in 2025 that you have watched:", watched_2025)
# Find movies released in 2025 that user has not watched
not_watched_2025 = movies_2025.difference(movies_watched)
print("Movies released in 2025 that you have not watched:", not_watched_2025)
# Find movies watched by user that were not released in 2025
watched_not_2025 = movies_watched.difference(movies_2025)
print("Movies you watched that were NOT released in 2025:", watched_not_2025)

# Q2. Daaraz found that their top electronic gadget buyer's are ram, shyam, sita, hari. Cosmetic buyers are hari, sita, gita, rita. Top grocery buyer's are ram, hari, gita and rabi. Find:
# Customers are top buyers of all electronics, cosmetics and groceries
# Customers who are top buyer of single category only
# Customers who are top buyers of exactly two categories
# All unique customers who are top buyers of at least one category
# Customers who are top buyers of electronics but not cosmetics

electronics = {"ram", "shyam", "sita", "hari"}
cosmetics = {"hari", "sita", "gita", "rita"}
groceries = {"ram", "hari", "gita", "rabi"}

# Customers are top buyers of all electronics, cosmetics and groceries
all_top_buyers = electronics.intersection(cosmetics, groceries)
print("Customers who are top buyers of all three categories:", all_top_buyers)

# Customers who are top buyer of single category only
elec_only = electronics - cosmetics - groceries
cos_only = cosmetics - electronics - groceries
gro_only = groceries - electronics - cosmetics
single_category_only = elec_only.union(cos_only, gro_only)
print("Customers who are top buyers of a single category only:", single_category_only)

# Customers who are top buyers of exactly two categories
elec_cos = electronics.intersection(cosmetics) - all_top_buyers
elec_gro = electronics.intersection(groceries) - all_top_buyers
cos_gro = cosmetics.intersection(groceries) - all_top_buyers
exactly_two = elec_cos.union(elec_gro, cos_gro)
print("Customers who are top buyers of exactly two categories:", exactly_two)

# All unique customers who are top buyers of at least one category
at_least_one = electronics.union(cosmetics, groceries)
print("All unique top buyers:", at_least_one)

# Customers who are top buyers of electronics but not cosmetics
elec_not_cos = electronics - cosmetics
print("Customers who are top buyers of electronics but not cosmetics:", elec_not_cos)
