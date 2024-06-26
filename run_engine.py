import extract_data, load_formula_mapping, load_other_mapping, load_data, calculate_metrics, calculate_ranking,update_cloud

print('****** Valuation Engine is triggered *****')
print('=== Refreshing Mapping ===')
load_formula_mapping.run()
load_other_mapping.run()
print('=== Mapping Refreshed ===')

print('=== Extract data ===')
extract_data.run()
print('=== Data extracted ===')

print('=== Start Loading Data ===')
load_data.run()
print('=== Data Load Completed ===')

print('=== Start Calculating Metrics ===')
calculate_metrics.run()
print('=== Metrics Calculation Completed ===')

print('=== Start Calculating Ranking ===')
calculate_ranking.run()
print('=== Ranking Calculation Completed ===')

# print('=== Update Cloud Database ===') 
# update_cloud.run()
# print('=== Cloud Database Updated ===')
# print('****** Load has been completed successfully *****')
